from itertools import cycle, izip
from base64 import b64encode, b64decode
from binascii import hexlify

PASS_LIST = """WXJ9KlMi
123456
Jh7Q5vdk
1234567890
xkCcrZuIGE
123456789
RkPW3546Z0
password
1234
x2wj7FsT
qwerty
123456
5r8gsKffJq
qwerty
password
111111
1234
19541954
123456
iloveyou
sunshine
666666
123456
8nTGjYosod
flag{Tebrikler. Harika_bir_is_cikarttiniz.MdiseCTF_0x02_kazanani}"""

def encrypt(message):
    key = "ZoRS1fr3"
    return ''.join(chr(ord(c)^ord(k)) for c,k in izip(message, cycle(key)))


for password in PASS_LIST.split("\n"):
    ctext = b64encode(encrypt(password))
    print ctext

#f.close()

