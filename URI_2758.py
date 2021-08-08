import struct

number_A, number_B = map(float, input().split())
number_A = struct.unpack('f',(struct.pack('f', number_A)))[0]
number_B = struct.unpack('f',(struct.pack('f', number_B)))[0]
number_C, number_D = map(float, input().split())

print('A = {:.6f}, B = {:.6f}\nC = {:.6f}, D = {:.6f}'.format(number_A, number_B, number_C, number_D))
print('A = {:.1f}, B = {:.1f}\nC = {:.1f}, D = {:.1f}'.format(number_A, number_B, number_C, number_D))
print('A = {:.2f}, B = {:.2f}\nC = {:.2f}, D = {:.2f}'.format(number_A, number_B, number_C, number_D))
print('A = {:.3f}, B = {:.3f}\nC = {:.3f}, D = {:.3f}'.format(number_A, number_B, number_C, number_D))
print('A = {:.3E}, B = {:.3E}\nC = {:.3E}, D = {:.3E}'.format(number_A, number_B, number_C, number_D))
print('A = {:.0f}, B = {:.0f}\nC = {:.0f}, D = {:.0f}'.format(number_A, number_B, number_C, number_D))
