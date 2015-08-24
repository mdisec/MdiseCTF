#!/usr/bin/env python
# -*- coding : utf-8 -*-
#
# WARNING : These codes compatible with python3..!
#
# plain:  abcdefghijklmnopqrstuvwxyz
# cipher: dsjmbhotvcwkxyefzialrqgnpu
#
#


class CustomMonoAlpSubsCipher(object):
    def __init__(self):
        """
        Lookup table. We could use maketrans function of
        string module but I just want to provide visual form of our table.
        :return:
        """
        self.lookupTable = {ord('a'): 'd', ord('b'): 's', ord('c'): 'j', ord('d'): 'm',
                            ord('e'): 'b', ord('f'): 'h', ord('g'): 'o', ord('h'): 't',
                            ord('i'): 'v', ord('j'): 'c', ord('k'): 'w', ord('l'): 'k',
                            ord('m'): 'x', ord('n'): 'y', ord('o'): 'e', ord('p'): 'f',
                            ord('q'): 'z', ord('r'): 'i', ord('s'): 'a', ord('t'): 'l',
                            ord('u'): 'r', ord('v'): 'q', ord('w'): 'g', ord('x'): 'n',
                            ord('y'): 'p', ord('z'): 'u', ord(' '): '-'}

    def encrypt(self, plain):
        plain = plain.lower().replace(" ", "-")
        print("Plain text = %s" % plain)
        print("Cipher text = %s" % plain.translate(self.lookupTable).upper())

crypto_factory = CustomMonoAlpSubsCipher()
plain = """
Put another password in
Bomb it out and try again
Try to get past logging in
Your target address starts with eight zero
Try his first wifes maiden name
This is more than just a game
It is real fun but just the same
Your target address continue with two four zero
Put qwerty in there
Run those passwords out and then
Dial back up we are logging in
Your target address continue with one four two
Do not even try to find me
Please do not send zero day exploit to fuck me
Who knows maybe I am right behind you
And of course your target address ends with one two two
"""
crypto_factory.encrypt(plain)