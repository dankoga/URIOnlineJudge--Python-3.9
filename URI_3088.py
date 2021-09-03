import sys
import re

comma = re.compile((r" ,"))
period = re.compile((r" \."))

for text in sys.stdin.readlines():
    print(re.sub(comma, ",", re.sub(period, ".", text.rstrip())))
