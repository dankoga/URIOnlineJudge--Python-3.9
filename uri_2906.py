import sys

addresses_qty = input()
unique_addresses = set()
for address in sys.stdin:
    local_raw, provider = address.rstrip().split('@')
    local = local_raw.replace('.','')
    addon_index = local.find('+')
    if addon_index > 0:
        unique_addresses.add(local[:addon_index] + '@' + provider)
    else:
        unique_addresses.add(local + '@' + provider)
print(len(unique_addresses))
