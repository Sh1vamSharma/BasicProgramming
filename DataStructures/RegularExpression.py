import re

teststring = r"\t123abc456ABCrtvd145abc"

# finding a pattren 1
pattren = re.compile(r"abc")
matches = pattren.finditer(teststring)
# finding a pattren 2
# matches = re.finditer(r"abc", teststring)
# methods :
# findall() - all the matches in string
# match() - begning
# search() - return first match

# group
# start
# end
# span
for match in matches:
    print(match)


