

arr_in_file = ['S', 'K', 'Y', '-', 'P', 'Q', 'N', 'O', '-', '1', '0', '0', '1']

flag = [None]*13

for idx, a in enumerate(arr_in_file):
	if idx < 4 or idx == 8: flag[idx] = a; continue
	#print(idx, ord(a), a, chr(ord(a)^4))
	flag[idx] = chr(ord(a)^4)

print(''.join(flag))