import re
pattern = r"[aeiou]"
pattern = r"[A-z][a-z][0-9]"
if re.match(pattern, "a asdksakjd"):
    print("Matched")