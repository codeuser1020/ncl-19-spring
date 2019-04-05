alph = { 'H': 'A', 'S': 'F', 'T': 'I', 'C': 'B', 'D': 'N', 'A': 'H', 
		 'K': 'G', 'Y': 'C', 'Q': 'V', 'W': 'U', 'J': 'E', 'U': 'P', 
		 'O': 'L', 'L': 'S', 'F': 'Y', 'P': 'M', 'B': 'T', ' ': ' ' }

msg = 'QWOD AQHY LFLBJP TL UWCOTY SHYTDK'

print(''.join([alph[m] for m in msg]))