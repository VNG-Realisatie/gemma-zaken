import re

file_path = "docs/standaard/zaken/zrc/1.6.x/1.6.0/openapi.yaml"

with open(file_path, 'r') as f:
    content = f.read()

# Pattern voor inline 401, 403, 406, 409, 410, 412, 415, 429 responses (Fout)
pattern_4xx = r"""        '(400|401|402|403|404|405|406|407|408|409|410|411|412|413|414|415|416|417|418|421|422|423|424|425|426|428|429|431|451|500)':
          headers:
            API-version:
              schema:
                type: string
              description:
                'Geeft een specifieke API-versie aan in de context van
                een specifieke aanroep\. Voorbeeld: 1\.2\.1\.'
          content:
            application/problem\+json:
              schema:
                \$ref: ['"]?[^'"]+['"]?
          description: .*"""

# # Vervang alle 400 responses
# content = re.sub(pattern_400, replacement_400, content)

# Vervang alle andere 4XX responses
def replace_4xx(match):
    code = match.group(1)
    return f"        '{code}':\n          $ref: '#/components/responses/{code}'"

content = re.sub(pattern_4xx, replace_4xx, content)


# Schrijf terug
with open(file_path, 'w') as f:
    f.write(content)

print("Refactoring completed!")