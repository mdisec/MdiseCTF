from itertools import cycle, izip
from base64 import b64decode

CIPHER_TEXT = """DTcYanoKP1o=
a11hZwRQ
EAdlAgQQFlg=
a11hZwRQRQtjXw==
IgQRMEM8B3odKg==
a11hZwRQRQtj
CAQCBAJTRgUAXw==
Kg4hIEYJAFc=
a11hZw==
Il0lOQYgAWc=
Kxg3IUUf
a11hZwRQ
bx1qNEItFFUQHg==
Kxg3IUUf
Kg4hIEYJAFc=
a15jYgBX
a11hZw==
a1ZnZwBfRwc=
a11hZwRQ
MwM9JVQfHUY=
KRo8IFkPHFY=
bFlkZQdQ
a11hZwRQ
YgEGFFs/HUA1Cw==
PAMzNEoyF1EoBjk/VBRcExIOIDpaBy1RMx0NOkI5EVoxDiAnRQ8cWiBBHzdYFRdwDikNY0lWQGwxDigyXwccWic="""

def encrypt(message, key):
    return ''.join(chr(ord(c)^ord(k)) for c,k in izip(message, cycle(key)))

for each in CIPHER_TEXT.split("\n"):
    print encrypt(b64decode(each), "ZoRS1fr3")