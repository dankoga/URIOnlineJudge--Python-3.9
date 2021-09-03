import sys
import re

re_include = re.compile(r"(#include )(<.+?>)")
re_endline = re.compile(r";")
re_bracket = re.compile(r"([{}])")

source_lines = sys.stdin.readlines()
source_stream = ' '.join([words for lines in source_lines for words in lines.split()])
source_stream = re.sub(re_include, r"\g<1>\g<2>\n", source_stream)
source_stream = re.sub(re_endline, r";\n", source_stream)
source_stream = re.sub(re_bracket, r" \g<1> ", source_stream)
print(source_stream)
