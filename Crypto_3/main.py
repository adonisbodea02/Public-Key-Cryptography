from random import randrange

import math
from math import sqrt, gcd

plain_text = {
    ' ': 0,
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26,
}

cypher_text = [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def is_prime(n):
    """
    Function to compute if a number is prime
    :param n: Integer
    :return: True, if n is prime
             False, otherwise
    """
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def modulo_inverse(n, m):
    """
    Function which determines the modulo inverse for a given number and a given base
    :param n: Integer - the number
    :param m: Integer - the base
    :return: Integer: the modulo inverse, if it exists
                      -1, otherwise
    """
    for i in range(1, m):
        if (n * i) % m == 1:
            return i
    return -1


def successive_squaring(base, exp, mod):
    """
    Function which computes a^exp mod m
    :param base: Integer: the base
    :param exp: Integer: the exponent
    :param mod: Integer: the modulo
    :return: Integer: a^exp mod m
    """
    return pow(base, exp, mod)


def encryption_word_to_code(text):
    """
    Function which generates the code of a block of text of 2 letters
    :param text: String of length 2
    :return: Integer: the codification of the text
    """
    return 27 * plain_text[text[0]] + plain_text[text[1]]


def encryption_word_to_text(code):
    """
    Function which generates string of length 3 from a code
    :param code: Integer
    :return: String of length 3
    """
    return cypher_text[int(code / (27 ** 2))] + cypher_text[int((code % (27 ** 2)) / 27)] + \
           cypher_text[int((code % (27 ** 2)) % 27)]


def decryption_word_to_code(text):
    """
    Function 
    :param text:
    :return:
    """
    return (27 ** 2) * plain_text[text[0].lower()] + 27 * plain_text[text[1].lower()] + plain_text[text[2].lower()]


def decryption_word_to_text(code):
    return cypher_text[int(code / 27)].lower() + cypher_text[int(code % 27)].lower()


def validate_plain_text(text):
    for i in text:
        if i not in plain_text.keys():
            return False
    return True


def validate_cypher_text(text):
    for i in text:
        if i not in cypher_text:
            return False
    return True


def separate_in_blocks_of_2(text):
    if len(text) % 2 == 1:
        text += ' '
    return [(text[i:i + 2]) for i in range(0, len(text), 2)]


def separate_in_blocks_of_3(text):
    return [(text[i:i + 3]) for i in range(0, len(text), 3)]


def generate_random_primes():
    p = randrange(2, 100)
    while not is_prime(p):
        p = randrange(2, 100)
    q = randrange(2, 100)
    while not is_prime(q):
        q = randrange(2, 100)
    return p, q


def generate_random_coprime(n):
    cp = randrange(2, n - 1)
    while gcd(n, cp) != 1:
        cp = randrange(2, n - 1)
    return cp


def generate_keys():
    p, q = generate_random_primes()
    n = p * q
    fi_n = (p - 1) * (q - 1)
    e = generate_random_coprime(fi_n)
    d = modulo_inverse(e, fi_n)
    print("Public key: ", n, e)
    print("Private key: ", d)
    return n, e, d


def encrypt(n, e):
    text = input("Give a plain text: ")
    while not validate_plain_text(text):
        text = input("Give a plain text: ")
    text = separate_in_blocks_of_2(text)
    encryption = ''
    for block in text:
        code = encryption_word_to_code(block)
        code = successive_squaring(code, e, n)
        encryption += encryption_word_to_text(code)
    print(encryption)


def decrypt(n, d):
    text = input("Give a cypher text: ")
    while not validate_cypher_text(text):
        text = input("Give a cypher text: ")
    text = separate_in_blocks_of_3(text)
    decryption = ''
    for block in text:
        code = decryption_word_to_code(block)
        code = successive_squaring(code, d, n)
        decryption += decryption_word_to_text(code)
    print(decryption)


def print_menu():
    print('0. Exit')
    print('1. Generate public and private keys')
    print('2. Encrypt text')
    print('3. Decrypt text')


def menu():
    print_menu()
    i = input('Give option: ')
    n = 0
    d = 0
    e = 0
    while i != '0':
        if i == '1':
            n, e, d = generate_keys()
        elif i == '2':
            if n != 0 and e != 0 and d != 0:
                encrypt(n, e)
        elif i == '3':
            if n != 0 and e != 0 and d != 0:
                decrypt(n, d)
        print_menu()
        i = input('Give option: ')


menu()
