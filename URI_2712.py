RESTRICTION = ['FRIDAY',
               'MONDAY',
               'MONDAY',
               'TUESDAY',
               'TUESDAY',
               'WEDNESDAY',
               'WEDNESDAY',
               'THURSDAY',
               'THURSDAY',
               'FRIDAY']


def check_tag(tag):
    if len(tag) != 8:
        return False
    if tag[3] != '-':
        return False
    return tag[:3].isupper() and tag[4:].isnumeric()


tags_qty = int(input())
for test in range(tags_qty):
    tag = input()
    if check_tag(tag):
        print(RESTRICTION[int(tag[-1])])
    else:
        print('FAILURE')
