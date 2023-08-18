import random

karakterler = "abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890é!'£^#%½&/=?*-_@<>|"

q = int(input("Kac karakterlik bir sifre istiyorsunuz?"))

for i in range(q):
    x random.choice(karakterler)
    print(x, end = "")
