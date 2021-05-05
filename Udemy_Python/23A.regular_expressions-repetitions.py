import re
#repetition pattern
#   ab*,        a with zero or more b
#   ab+,        a with one or more b
#   ab?,        a with zero or one b
#   ab{3},      a with three b's
#   ab{3,4}     a with three to four b's
text = "Do you know how to be a script kiddie? It's simple, just copy me."
out = re.findall('ow?',text)
print(out)
text = "a......ab......abb.........abbb...........aabbb"
out = re.findall('ab{2,3}',text)
print(out)