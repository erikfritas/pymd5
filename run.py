'''
PYMD5
by @erikfritas
'''
from imports import *

msg = {
    True: '^^^ That is your md5 hash',
    False: 'We don\'t have a md5 hash in this wordlist ;(\nTry again with other wordlist!'
}

wordlists = {
    'A': 'default.txt'
}

wl = wordlists[str(input('Choose your wordlist: \n(A) default.txt\n\n$ ')).upper()]

with open(f'./{wl}') as wordlist:
    wordlist = wordlist.readlines()

m1 = str(input("Digit your md5 hash: "))
print(f'Your hash: {m1}\n')
md5_ = md5()

for i in wordlist:
    md5_.update(i.encode('utf-8'))
    m2 = md5_.hexdigest()

    print(f'{m2} == {i}, m1 == m2 => {m1 == m2}')

    if m1 == m2: break

print(msg[m1 == m2])
