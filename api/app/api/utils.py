import binascii
import os


def generate_random_hex(nos=6):
    return binascii.b2a_hex(os.urandom(nos)).decode('utf-8')
