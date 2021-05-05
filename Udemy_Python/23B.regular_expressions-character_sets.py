import re

#character sets
#   [ab],       a or b
#   s[ab]+      s with one or more a or b
text = "This is a sample paragraph. Do you like paragliding?. No, I like parasailing. paraam"
out = re.findall('para[sga]+',text)
print(out)