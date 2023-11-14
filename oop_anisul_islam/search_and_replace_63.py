import re
pattern = r"colour"
text = "My favourite colour is Red, I love blue colour as well"

print(re.sub(pattern, "color", text, count=1))
print(text)
