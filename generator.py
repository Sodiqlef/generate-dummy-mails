import string
import random
from names import names


x = [''.join(random.choices(names,  k=2)) for _ in range(100)]
for y in x:
    z = str(y ) + ''.join(random.choices(string.digits,  k=2)) + '@' + ''.join(random.choice(['yahoo.com', 'gmail.com', 'hotmail.com', 'icloud.com', 'outlook.com']))
    print(z)
