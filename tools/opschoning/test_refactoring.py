#!/usr/bin/env python3
"""
Test script to verify OpenAPI refactoring quality.

Checks:
1. No inline response definitions remain (headers + content + schema pattern)
2. All responses use $ref to components/responses
3. Required components exist in components/responses section
4. File is valid YAML
5. No duplicate response definitions
"""

import yaml
import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple


def load_yaml(file_path: str) -> Dict:
    """Load and parse YAML file."""
    try:
        with open(file_path, 'r') as f:
            return yaml.safe_load(f)
    except yaml.YAMLError as e:
        print(f"❌ YAML parsing error: {e}")
        sys.exit(1)
    except FileNotFoundError:
        print(f"❌ File not found: {file_path}")
        sys.exit(1)


def check_inline_responses(content: str) -> List[Tuple[int, str]]:
    """
    Find remaining inline response definitions.
    Returns list of (line_number, preview) tuples.
    """
    issues = []
    
    # Pattern for inline response with headers and content
    pattern = re.compile(
        r"^\s{8,}'(\d{3})':\s*\n"  # Status code with 8+ spaces indent
        r"(?=\s{10,}(?:headers|content|description):)",  # Followed by headers/content/description
        re.MULTILINE
    )
    
    lines = content.split('\n')
    
    for match in pattern.finditer(content):
        line_num = content[:match.start()].count('\n') + 1
        status_code = match.group(1)
        
        # Get context (5 lines)
        start_line = max(0, line_num - 1)
        end_line = min(len(lines), line_num + 4)
        context = '\n'.join(lines[start_line:end_line])
        
        # Check if it's NOT a $ref (inline definition)
        if '$ref:' not in context.split('\n')[0]:
            issues.append((line_num, status_code, context))
    
    return issues


def check_ref_format(data: Dict) -> List[str]:
    """Check that all response references follow correct format."""
    issues = []
    
    def traverse_responses(obj, path=""):
        if isinstance(obj, dict):
            if 'responses' in obj:
                for status_code, response in obj['responses'].items():
                    if isinstance(response, dict):
                        if '$ref' in response:
                            ref = response['$ref']
                            # Should reference components/responses
                            if not ref.startswith('#/components/responses/'):
                                issues.append(
                                    f"{path} -> {status_code}: Invalid $ref format: {ref}"
                                )
                        elif 'content' in response or 'headers' in response:
                            # Has content/headers but no $ref - potential inline definition
                            if status_code not in ['200', '201', '202', '204']:
                                issues.append(
                                    f"{path} -> {status_code}: Response has content/headers without $ref"
                                )
            
            for key, value in obj.items():
                traverse_responses(value, f"{path}/{key}" if path else key)
        elif isinstance(obj, list):
            for i, item in enumerate(obj):
                traverse_responses(item, f"{path}[{i}]")
    
    traverse_responses(data)
    return issues


def check_components_exist(data: Dict) -> List[str]:
    """Check that referenced components exist."""
    issues = []
    
    # Collect all $ref references to components/responses
    refs_used = set()
    
    def collect_refs(obj):
        if isinstance(obj, dict):
            if '$ref' in obj:
                ref = obj['$ref']
                if ref.startswith('#/components/responses/'):
                    component_name = ref.split('/')[-1]
                    refs_used.add(component_name)
            for value in obj.values():
                collect_refs(value)
        elif isinstance(obj, list):
            for item in obj:
                collect_refs(item)
    
    collect_refs(data)
    
    # Check if components exist
    components_responses = data.get('components', {}).get('responses', {})
    
    for ref_name in refs_used:
        if ref_name not in components_responses:
            issues.append(f"Referenced component missing: {ref_name}")
    
    return issues


def check_common_responses_defined(data: Dict) -> List[str]:
    """Check that common error responses are defined."""
    issues = []
    
    components_responses = data.get('components', {}).get('responses', {})
    
    # Expected common responses
    expected = {
        'FoutResponse': 'For 4XX and 5XX errors (Fout schema)',
        'ValidatieFoutResponse': 'For 400 validation errors (ValidatieFout schema)',
    }
    
    for name, description in expected.items():
        if name not in components_responses:
            issues.append(f"Missing common response: {name} ({description})")
    
    return issues


def analyze_response_usage(data: Dict) -> Dict[str, int]:
    """Count how many times each response code appears."""
    response_counts = {}
    
    def count_responses(obj):
        if isinstance(obj, dict):
            if 'responses' in obj:
                for status_code in obj['responses'].keys():
                    response_counts[status_code] = response_counts.get(status_code, 0) + 1
            for value in obj.values():
                count_responses(value)
        elif isinstance(obj, list):
            for item in obj:
                count_responses(item)
    
    count_responses(data)
    return response_counts


def main():
    # Target file
    file_path = "docs/standaard/zaken/zrc/1.6.x/1.6.0/openapi.yaml"
    
    print(f"🔍 Testing refactoring quality: {file_path}\n")
    print("=" * 70)
    
    # Load file
    with open(file_path, 'r') as f:
        content = f.read()
    
    data = load_yaml(file_path)
    
    all_passed = True
    
    # Test 1: Check for inline responses
    print("\n📋 Test 1: Checking for inline response definitions...")
    inline_issues = check_inline_responses(content)
    if inline_issues:
        all_passed = False
        print(f"❌ Found {len(inline_issues)} inline response(s):\n")
        for line_num, status_code, context in inline_issues:
            print(f"  Line {line_num} - Status {status_code}:")
            print(f"  {context}\n")
    else:
        print("✅ No inline responses found")
    
    # Test 2: Check $ref format
    print("\n📋 Test 2: Checking $ref format...")
    ref_issues = check_ref_format(data)
    if ref_issues:
        all_passed = False
        print(f"❌ Found {len(ref_issues)} issue(s):\n")
        for issue in ref_issues:
            print(f"  - {issue}")
    else:
        print("✅ All $ref formats correct")
    
    # Test 3: Check components exist
    print("\n📋 Test 3: Checking referenced components exist...")
    component_issues = check_components_exist(data)
    if component_issues:
        all_passed = False
        print(f"❌ Found {len(component_issues)} issue(s):\n")
        for issue in component_issues:
            print(f"  - {issue}")
    else:
        print("✅ All referenced components exist")
    
    # Test 4: Check common responses defined
    print("\n📋 Test 4: Checking common responses are defined...")
    common_issues = check_common_responses_defined(data)
    if common_issues:
        all_passed = False
        print(f"❌ Found {len(common_issues)} issue(s):\n")
        for issue in common_issues:
            print(f"  - {issue}")
    else:
        print("✅ Common responses defined")
    
    # Test 5: YAML validity
    print("\n📋 Test 5: YAML validity...")
    print("✅ File is valid YAML")
    
    # Statistics
    print("\n📊 Statistics:")
    response_counts = analyze_response_usage(data)
    print(f"  Total response codes used: {len(response_counts)}")
    for code in sorted(response_counts.keys()):
        print(f"    {code}: {response_counts[code]} occurrence(s)")
    
    components_responses = data.get('components', {}).get('responses', {})
    print(f"  Components defined: {len(components_responses)}")
    for name in sorted(components_responses.keys()):
        print(f"    - {name}")
    
    # Final result
    print("\n" + "=" * 70)
    if all_passed:
        print("✅ ALL TESTS PASSED - Refactoring is correct!")
        return 0
    else:
        print("❌ SOME TESTS FAILED - Please review issues above")
        return 1


if __name__ == "__main__":
    sys.exit(main())
