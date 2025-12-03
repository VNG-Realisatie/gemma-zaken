import re

file_path = "docs/standaard/zaken/zrc/1.6.x/1.6.0/openapi.yaml"

with open(file_path, 'r') as f:
    content = f.read()

# Pattern voor de inline 400 response (ValidatieFout)
# pattern_400 = r"""        '400':
#           headers:
#             API-version:
#               schema:
#                 type: string
#               description:
#                 'Geeft een specifieke API-versie aan in de context van
#                 een specifieke aanroep\. Voorbeeld: 1\.2\.1\.'
#           content:
#             application/problem\+json:
#               schema:
#                 \$ref: '#/components/schemas/ValidatieFout'
#           description: Bad request"""

# replacement_400 = "        '400':\n          $ref: '#/components/responses/ValidatieFoutResponse'"

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

# Pattern voor 500 responses
pattern_500 = r"""        '500':
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
                \$ref: '#/components/schemas/Fout'
          description: Internal server error"""

replacement_500 = "        '500':\n          $ref: '#/components/responses/FoutResponse'"

content = re.sub(pattern_500, replacement_500, content)

# Schrijf terug
with open(file_path, 'w') as f:
    f.write(content)

print("Refactoring completed!")