from pyshark import FileCapture

access_points = set()

cap = FileCapture('Radius.pcap', display_filter='radius.User_Name == "sally.berro"')

print('user mac: ' + cap[0]['radius'].get('radius.Calling_Station_Id'))

cap = FileCapture('Radius.pcap')

for c in cap:
	r = c['radius']
	if r:
		rcid = r.get('radius.Called_Station_Id')
		if rcid:
			access_points.add(rcid)
		else:
			print('no access station id')
	else:
		print('no radius layer')

print(len(access_points), ' access points received requests')