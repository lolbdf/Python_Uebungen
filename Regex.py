import re

x = re.search("0{3}(?P<teil2>-0+1)", "000-01")
print(x.span())

