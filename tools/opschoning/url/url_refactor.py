import yaml
import re

with open('docs/standaard/zaken/zrc/1.6.x/1.6.0/openapi.yaml', 'r') as f:
    content = f.read()

# Find all url property definitions with their full context
url_patterns = []
lines = content.split('\n')

i = 0
while i < len(lines):
    line = lines[i]
    # Check if this line contains "url:" as a property (indented)
    if re.match(r'^\s{8,}url:\s*$', line):
        # Capture the full definition
        definition = [line]
        indent = len(line) - len(line.lstrip())
        i += 1
        
        # Capture all following lines that belong to this property
        while i < len(lines):
            next_line = lines[i]
            next_indent = len(next_line) - len(next_line.lstrip())
            
            # If empty line or has greater indent, it belongs to url property
            if not next_line.strip() or next_indent > indent:
                definition.append(next_line)
                i += 1
            # If same or less indent and not a continuation, we're done
            elif next_indent <= indent:
                break
            else:
                i += 1
                
        url_text = '\n'.join(definition)
        
        # Create a normalized version for comparison
        normalized = re.sub(r'\s+', ' ', url_text).strip()
        
        # Check if we already have this pattern
        found = False
        for pattern in url_patterns:
            if pattern['normalized'] == normalized:
                pattern['count'] += 1
                found = True
                break
        
        if not found:
            url_patterns.append({
                'text': url_text,
                'normalized': normalized,
                'count': 1
            })
    else:
        i += 1

# Sort by count (most common first)
url_patterns.sort(key=lambda x: x['count'], reverse=True)

print(f"Gevonden {len(url_patterns)} verschillende url property definities:\n")
print("=" * 80)

for idx, pattern in enumerate(url_patterns, 1):
    print(f"\nVariant {idx} (komt {pattern['count']}x voor):")
    print("-" * 80)
    print(pattern['text'])
    print()
