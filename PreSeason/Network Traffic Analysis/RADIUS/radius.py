from pyshark import FileCapture

access_points = set()

cap = FileCapture('Radius.pcap', display_filter='radius.User_Name == "sally.berro"')

print('user mac: ' + cap[0]['radius'].get('radius.Calling_Station_Id'))

cap = FileCapture('Radius.pcap', display_filter='radius')
for c in cap:
    access_points.add(c['radius'].get('radius.Called_Station_Id'))
access_points.remove(None)

print(len(access_points), ' access points received requests')
