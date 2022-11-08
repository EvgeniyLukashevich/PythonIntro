import os
import random as r

symbs = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f',
16: 'g', 17: 'h', 18: 'i', 19: 'j', 20: 'k', 21: 'l', 22: 'm', 
23: 'n', 24: 'o', 25: 'p', 26: 'q', 27: 'r', 28: 's', 29: 't',
30: 'u', 31: 'v', 32: 'w', 33: 'x', 34: 'y', 35: 'z'}



def songChoose():
    d = 'data\songs'
    x = r.choice([x for x in os.listdir(d)])
    return x

def picChoose():
    d = 'data\pics'
    x = r.choice([x for x in os.listdir(d)])
    return x

def voiceChoose():
    d = 'data/voices'
    x = r.choice([x for x in os.listdir(d)])
    return x

def artChoose():
    d = 'data/arts'
    x = r.choice([x for x in os.listdir(d)])
    return x