seconds = int(input())
hour, remainder = divmod(seconds, 60*60)
minutes, seconds = divmod(remainder, 60)
print("{}:{}:{}".format(hour, minutes, seconds))
