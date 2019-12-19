'''
Bei der Chosen plaintext Attack kann der Angreifer für einen beliebigen Plaintext den zugehörigen Chiffretext erfragen.
Zuerst wählt der Angreifer also Nachrichten aus und lässt sich dafür die Ciphertexts zurückgeben.
Danach wählt der Angreifer zwei weitere Nachrichten und schickt sie dem Orakel, welches eine Nachricht auswählt
und dessen Ciphertext zurückschickt. Der Angreifer muss nun entscheiden, welche der beiden Nachrichten verschlüsselt wurde.
Das Spiel ist gewonnen, wenn der Angreifer die richtige Nachricht ausgewählt hat.
Durch Raten wird in der Hälfte der Fälle die richtige Nachricht ausgewählt.
Die Rate der richtige gewählten Nachrichten muss also signifikant größer sein als 1/2 (1/2 + negl(n))
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
# NOT A SECURE PSEUDO RANDOM GENERATOR! Don't use for actuall encryption.
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
        self.ciphertexts = []


    def gen_key(self):
        self.key = Key(self.n)

    def test(self):
        return 0

    def receive_messages(self, attacker : 'Attacker'):
        self.m = attacker.get_m()


    def choose_message(self):
        self.b = random.getrandbits(1)

    def encrypt_messages(self):
        for mess in self.m:
            self.ciphertexts.append(self.cipher.enc(mess))

    def encrypt_message(self):
        self.ciphertext = self.cipher.enc(self.m[self.b])

    def get_ciphertexts(self):
        return self.ciphertexts

    def get_ciphertext(self):
        return self.ciphertexts[0]

    def recieve_b1(self, attacker : 'Attacker'):
        self.b1 = attacker.get_b()

    def verify(self):
        return self.b == self.b1

class Attacker:
    def __init__(self, n):
        self.n = n
        self.m = []

    def choose_messages(self, m):
        self.m = m

    def get_m(self, i):
        return self.m[i]

    def recieve_ciphertexts(self, oracle : Oracle):
        self.ciphertexts = oracle.get_ciphertexts()

    def recieve_ciphertext(self, oracle : Oracle):
        self.ciphertext = oracle.get_ciphertext()
    def determine_b(self):
        self.b = random.getrandbits(1)

    def get_b(self):
        return self.b

def run_cpa():
    n = 128
    cipher = Symmetric_Cipher(gen, enc, dec)
    oracle = Oracle(n, cipher)
    attacker = Attacker(n)

    oracle.gen_key() # 1
    # beliebig viele Nachrichten senden und ciphertext bekommen
    attacker.choose_messages(["halli", "hallo"]) # 2
    oracle.receive_messages(attacker)
    oracle.encrypt_messages() # 3
    attacker.recieve_ciphertexts(oracle)


    #oracle.choose_message()
    attacker.choose_messages("halli", "hallo") # 4
    oracle.receive_messages(attacker)
    oracle.choose_message() # 5
    oracle.encrypt_messages() # 6
    attacker.recieve_ciphertext(oracle)




    attacker.choose_messages(["halli", "hallo"]) # 7
    oracle.receive_messages(attacker)
    oracle.encrypt_messages() # 8
    attacker.recieve_ciphertexts(oracle)


    attacker.determine_b() # 9
    oracle.recieve_b1(attacker)
    return oracle.verify() # 10
