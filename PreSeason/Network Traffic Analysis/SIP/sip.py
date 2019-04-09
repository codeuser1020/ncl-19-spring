from pyshark import FileCapture
import re

# ignore stdout
import os
import sys
f = open(os.devnull, 'w')
sys.stderr = f

try:
	""" software running voip proxy """	
	cap = FileCapture('SIP.pcap', display_filter='ip.src == 10.21.128.1 && sip')
	print('proxy software:', cap[0]['sip'].get('sip.Server').split(' ')[0])
	

	""" number of voice mails for user 542 """
	cap = FileCapture('SIP.pcap', display_filter='sip.Method == NOTIFY && sip.r-uri.user == "542"')
	hdr = cap[0]['sip'].get('sip.msg_hdr')
	match = re.search(r'Voice-Message: (\d)/(\d)', hdr)
	print('number of voice mails', int(match.group(1)) + int(match.group(2)))

	cap = FileCapture('SIP.pcap', display_filter='sip.Method == INVITE')
	""" What is the SIP address of the caller in the only call? """
	print('initializer of only call:', cap[0]['sip'].get('sip.from.addr'))
	""" What is the SIP address of the recipient of the only call? """
	print('recipient of only call:', cap[0]['sip'].get('sip.to.addr'))
	""" What is the IP address of the recipient of the only call? """
	cap = FileCapture('SIP.pcap', display_filter='sip.r-uri.user == "635"')
	print('ip of recipient:', cap[0]['ip'].src)
	""" What brand of physical phone was the recipient of the call using? """
	print('type of device:', cap[0]['sip'].get('sip.User-Agent'))
	""" What is the SIP address of the individual who hangs up the call? """
	cap = FileCapture('SIP.pcap', display_filter='sip.Method == BYE')
	print('sip address of user who closed call:', cap[0]['sip'].get('sip.from.addr'))
	""" How many seconds into the capture is the first word of the call said? """
	cap = FileCapture('SIP.pcap', display_filter='rtp', only_summaries=True)
	print('number of seconds:', round(float(cap[0].time)))
	""" How many different SIP agents registered with the SIP proxy? """
	agents = set()
	cap = FileCapture('SIP.pcap', display_filter='sip.CSeq.method == "REGISTER" && sip.Status-Code == 200')
	for c in cap:
		a = c['sip'].get('sip.from.addr')
		if a: agents.add(a)
	print('number of agents registered:', len(agents))
except:
	pass