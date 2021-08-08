import sys


good_list = sys.stdin.readlines()
good_list = sorted(good_list, key=lambda name: name.lower())
print(good_list[-1].rstrip())
