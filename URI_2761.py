from struct import pack, unpack

var_int, var_float, var_char, var_str = input().split(' ', 3)
var_int = int(var_int)
var_float = unpack('f', pack('f', float(var_float)))[0]

print('{}{:.6f}{}{}'.format(var_int, var_float,var_char, var_str))
print('{}\t{:.6f}\t{}\t{}'.format(var_int, var_float,var_char, var_str))
print('{:10d}{:10f}{:>10s}{:>10s}'.format(var_int, var_float,var_char, var_str))
