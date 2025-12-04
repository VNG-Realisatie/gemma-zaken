import re

# Basis voorbeeld: vervang alle cijfers door 'X'
text = "Ik heb 3 appels en 5 peren"
result = re.sub(r'\d', 'X', text)
print(result)  # Output: Ik heb X appels en X peren

# Met groepen: wissel voornaam en achternaam om
text = "Henri Korver"
result = re.sub(r'(\w+) (\w+)', r'\2, \1', text)
print(result)  # Output: Korver, Henri

# Met een functie: maak elk woord hoofdletter
def capitalize_match(match):
    return match.group(0).upper()

text = "hallo wereld"
result = re.sub(r'\w+', capitalize_match, text)
print(result)  # Output: HALLO WERELD

# Meerdere regels met DOTALL flag
text = """<div>
  content
</div>"""
result = re.sub(r'<div>.*?</div>', '<span>nieuw</span>', text, flags=re.DOTALL)
print(result)  # Output: <span>nieuw</span>

# Alleen eerste N matches vervangen
text = "a1 b2 c3 d4"
result = re.sub(r'\d', 'X', text, count=2)
print(result)  # Output: a1 bX cX d4