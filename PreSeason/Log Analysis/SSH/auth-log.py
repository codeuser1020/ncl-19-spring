from collections import Counter
import re

users = set()
users_list = []
invalid_users = set()
unauthorized_ips = set()
unauthorized_ips_list = []
fail_count = 0
attempts = set()

with open('auth.log') as f:
	for line in f:
		m = re.search('[^r]user=(.+)', line)
		if m: users.add(m.group(1)) ; users_list.append(m.group(1))
		""" find number of invalid user attempts """
		m = re.search('invalid user (.+?) ', line)
		if m: invalid_users.add(m.group(1)) ; 
		m = re.search('invalid user (.+?) from', line)
		if m: users_list.append(m.group(1))
		""""""

		""" find unathorized access attempts """
		m = re.search('Failed password .* (.+) port', line)
		if m: unauthorized_ips.add(m.group(1)) ; unauthorized_ips_list.append(m.group(1))
		m = re.search('Invalid user .* from (.+)', line)
		if m: unauthorized_ips.add(m.group(1)) 
		""""""
		m = re.search(r'pam_unix\(sshd:auth\): authentication failure;', line)
		if m: fail_count += 1

		m = re.search(r'sshd\[([0-9]+)\]', line)
		if m: attempts.add(m.group(1))

print(len(unauthorized_ips), 'unauthorized ip') # correct
print(len(invalid_users|users), 'total users') # correct
print(len(invalid_users), 'invalid users')
print(len(users), 'valid users') # correct
print('10th most common IP', Counter(unauthorized_ips_list).most_common(10)[-1][0])
print('5th most common username', Counter(users_list).most_common(5)[-1][0])
print('number of failed attempts', len(attempts))


""" wrong fail count values
	3687
	3474
	2579
	4817
"""
