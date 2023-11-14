import re

pattern = r"colour"
string = "colour, I love red colour"
if re.search(pattern, string):
    print("Matched")
else:
    print("Not matched")

print(re.findall(pattern, string))




"""
https://youtu.be/sTb-lhScglI?list=PLgH5QX0i9K3rz5XqMsTk41_j15_6682BN

"""