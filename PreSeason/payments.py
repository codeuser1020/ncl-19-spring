from collections import Counter
import re

orders = []
states = []
count = 0

with open('payments.log') as f:
	for line in f:
		m = re.search('OrderTotal currencyID="USD">(.*?)<', line)
		if m: orders.append(float(m.group(1)))
		m = re.search('<ebl:StateOrProvince>(..)</ebl:StateOrProvince>', line)
		if m: states.append(m.group(1))
		m = re.search('PPAPIService: Request', line)
		if m: count += 1

print('number of requests:', count)
print('largest purchase: $%.2f' % max(orders))
print('state with most purchases:', Counter(states).most_common(1)[0][0])