#!/usr/bin/env python3

import random

def Glow_Up(data, key):
    # Lets go tilted
    decrypted_data = ''.join(chr(ord(char) ^ ord(key[i % len(key)])) for i, char in enumerate(data))
    return decrypted_data

def CEO(data):
    # MID
    return [x * 3 - 1 for x in data]

def Fam(data):
    # ALSO MID
    return data[::-1]

def Cancel_Culture(data):
    # MIMIMID
    return [x // 2 for x in data]

def Stan(data):
    # SKIBIDI TOILET
    return sum(data) % 256

def E_boy_or_E_girl(data):
    # No cap fam
    return [x ^ 42 for x in data]

def W(data):
    # Bought a property in egypt
    scrambled = data[:]
    for i in range(0, len(scrambled) - 1, 2):
        scrambled[i], scrambled[i + 1] = scrambled[i + 1], scrambled[i]
    return scrambled

def Dank(data):
    # Kai Cenat Fanum tax
    return [x + 2 for x in data]

def Ghosting(data, shift_amount):
    # Oui i i a i ou i i a i
    return [(x + shift_amount) % 256 for x in data]

def Salty(data):
    # Quandale dingle
    data = CEO(data)
    data = W(data)
    data = Dank(data)
    data = Fam(data)
    data = Cancel_Culture(data)
    return data

def Finna(length):
    # Gegagedigedagedago
    random.seed(42)
    return [random.randint(0, 255) for _ in range(length)]

def Big_Yikes(data):
    # the boys at the Rizz party
    return [x * 2 for x in data]

def Boujee(data):
    # Gooning
    return [(x * 7) % 256 for x in data]

def High_Key(data):
    # Negative aura
    for _ in range(10):
        data = Boujee(data)
    return data

def Cheugy(data):
    # SUS
    return [x ^ 99 for x in data]

def main():
    key = "supersecretkey"
    encrypted_data = open("secret.txt", "r").read()
    decrypted_message = Glow_Up(encrypted_data, key)
    print("Decrypted message:", decrypted_message)
    key = [ord(k) for k in key]
    key = Salty(key)
    key = E_boy_or_E_girl(key)
    Stan(key)
    key = Big_Yikes(key)
    key = Ghosting(key, 5)
    key = Fam(key)
    key = W(key)
    key = W(key)
    key = Fam(key)
    key = Ghosting(key, -5)
    key = Cheugy(key)
    key = High_Key(key)
    key = [x + 1 for x in key]
    key = [x // 2 for x in key]
    print(key)

if __name__ == "__main__":
    main()

