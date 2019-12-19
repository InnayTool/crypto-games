'''
Eavsdropping indistinguishability (semantische Sicherheit beschriebt, die Sicherheit eines Algorithmus
'''

import random



class Symmetric_Cipher:
    def __init__(self, gen, enc, dec):
        self.gen = gen
        self.enc = enc
        self.dec = dec

class Key:
    def __init__(self, n, gen):
        #self.n = n

        self.key = gen(n)

    def get(self):
        return self.key



def gen(n):
# NOT A SECURE PSEUDO RANDOM GENERATOR! Don't use for actuall encryption
    return random.getrandbits(n)

def enc(message, key):
    return 0

def dec(ciphertext, key):
    return 0


class Oracle:
    def __init__(self, n : int, cipher : Symmetric_Cipher):
        self.n = n

        self.m = []
        self.cipher = cipher


    def gen_key(self):
        self.key = Key(self.n)

    def test(self):
        return 0

    def receive_messages(self, attacker : 'Attacker'):
        self.m[0] = attacker.get_m(0)
        self.m[1] = attacker.get_m(1)

    def choose_message(self):
        self.b = random.getrandbits(1)

    def encrypt_selected_message(self):
        self.ciphertext = self.cipher.enc(self.m[self.b])

    def get_ciphertext(self):
        return self.ciphertext

    def recieve_b1(self, attacker : 'Attacker'):
        self.b1 = attacker.get_b()

    def verify(self):
        return self.b == self.b1

class Attacker:
    def __init__(self, n):
        self.n = n
        self.m = []

    def choose_messages(self, m0, m1):
        self.m[0] = m0
        self.m[1] = m1

    def get_m(self, i):
        return self.m[i]

    def recieve_ciphertext(self, oracle : Oracle):
        self.ciphertext = oracle.get_ciphertext()

    def determine_b(self):
        self.b = random.getrandbits(1)

    def get_b(self):
        return self.b

def run_eav():
    n = 128
    cipher = Symmetric_Cipher(gen, enc, dec)
    oracle = Oracle(n, cipher)
    attacker = Attacker(n)

    oracle.gen_key()
    attacker.choose_messages("halli", "hallo")
    oracle.receive_messages(attacker)
    oracle.choose_message()
    oracle.encrypt_selected_message()
    attacker.recieve_ciphertext(oracle)
    attacker.determine_b()
    oracle.recieve_b1(attacker)
    return oracle.verify()
