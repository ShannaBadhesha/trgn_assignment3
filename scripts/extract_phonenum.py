import re
file = open("mytextfile.txt" ,'r')
file
text = file.read()
text
pattern = r"\+?[0-9]\d{0,2}[-]\d{3}[-]\d{3}[-]\d{4}"
phonum = re.findall(pattern,text)
phonum
for match in re.findall(pattern,text):
    print(match)
