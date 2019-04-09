
from pyshark import FileCapture
from binascii import unhexlify

# prevent error output
import os
import sys
f = open(os.devnull, 'w')
sys.stderr = f

# What is the IP address of the device that is pinging other devices?
cap = FileCapture('Basics.pcap', display_filter='icmp.type == 8')
print('IP of device pinging other devices:', cap[0]['ip'].addr)

# According to the ping traffic, what is the IP address of the host that is not up?
cap = FileCapture('Basics.pcap', display_filter='icmp.type == 8 && icmp.resp_not_found')
print('IP of device pinging other devices:', cap[0]['ip'].dst)

# What is the IP address of the device at 00:50:56:F9:77:70 given by ARP
cap = FileCapture('Basics.pcap', display_filter='arp.src.hw_mac == 00:50:56:f9:77:70')
print('ip address of device at 00:50:56:F9:77:70:', cap[0]['arp'].get('arp.src.proto_ipv4'))

# What is the first website that 10.0.0.132 visited?
cap = FileCapture('Basics.pcap', display_filter='http && ip.addr==10.0.0.132')
print('first website visited by 10.0.0.132:', cap[0]['http'].get('http.host'))

# How many bytes large is the only .ico file downloaded via HTTP?
cap = FileCapture('Basics.pcap', display_filter='http.request.uri contains ".ico"')
req = cap[0].frame_info.number
cap = FileCapture('Basics.pcap', display_filter='http.response')
for c in cap:
    if '104' == c['http'].get('request_in'):
        print('number of bytes in ico file:', len(unhexlify(c['http'].get('file_data'))))
        break

# What is the IP address of the FTP server the user at 10.0.0.132 connects to?
cap = FileCapture('Basics.pcap', display_filter='ftp && ip.src==10.0.0.132')
print('ip address of ftp server:', cap[0]['ip'].dst)

# What was the password used to log in to the FTP server?
cap = FileCapture('Basics.pcap', display_filter='ftp.request.command == "PASS"')
print('password:', cap[0]['ftp'].get('request.arg'))

# How many folders are directly (not including child folders) in the /ubuntu folder on the FTP server?
cap = FileCapture('Basics.pcap', display_filter='ftp-data && tcp.stream == 30')
# cant figure out how to print out ftp-data payload


