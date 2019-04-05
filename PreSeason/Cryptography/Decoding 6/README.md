#  Decoding 6

#### It looks like the hackers have gotten more creative and invented a custom protocol for encrypting messages. Good thing they are terrible at physical security. We've obtained a sticky note with the ruleset they are using. We have filtered the relevant parts. It is up to you to decrypt the message and find out what they are up to.

```
================RULESET================
| A = H | H = A  | E = 2E  | M = M+3  |
| 6 = S | G = K  | 16 = U  | 2J = D/2 |
| I = T | C = Y  | 3D = 15 |          |
| B = 3 | 22 = Q | 19 = 4C |          |
| N = D | U = 23 | Z-1 = 6 |          |
|===============MESSAGE===============|
|  QWOD AQHY LFLBJP TL UWCOTY SHYTDK  |
|---------------DECRYPT---------------|
|       H A                    A      |
=======================================
```

1. What is the plaintext of the encrypted message?

The ruleset can be decoded by hand. Python can be used to help in the decoding process.
```
>>> chr(ord('@') + 6) # translate 6
'F'
>>> chr(ord('@') + (ord('E') - ord('@'))*2) # translate 2E
'J'
>>> chr(ord('@') + (ord('D') - ord('@'))//2) # translate D/2
'B'
```
<details>
<summary>The final ruleset</summary>

```
A = H
F = S
I = T
B = C
N = D
H = A
G = K
C = Y
V = Q
U = W
E = J
P = U
L = O
S = L
Y = F
M = P
T = B
```
</details>

Using python the message can be easily decoded.
```
alph = { 'H': 'A', 'S': 'F', 'T': 'I', 'C': 'B', 'D': 'N', 'A': 'H',
'K': 'G', 'Y': 'C', 'Q': 'V', 'W': 'U', 'J': 'E', 'U': 'P',
'O': 'L', 'L': 'S', 'F': 'Y', 'P': 'M', 'B': 'T', ' ': ' ' }

msg = 'QWOD AQHY LFLBJP TL UWCOTY SHYTDK'

print(''.join([alph[m] for m in msg]))
```

<details>
<summary>Flag</summary>

`VULN HVAC SYSTEM IS PUBLIC FACING`
</details>
