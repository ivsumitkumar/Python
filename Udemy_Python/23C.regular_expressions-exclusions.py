import re
#exclusions
#   ^           not including certain patters
text = "This is a sample exclamation! Don't overreact mate?."
out = re.findall('[^as ]+',text)
print(out)
