import math 

def kubus (sisi):
    return 6 * sisi**2

def balok (panjang, lebar, tinggi):
    return 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)

def bola (r):
    return 4 * math.pi * r**2

def tabung (r, t):
    return 2 * math.pi * r * (r + t)

def kerucut (r, s):
    return math.pi * r * (r + s)

