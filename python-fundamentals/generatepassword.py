#!/usr/bin/python3
# -*- coding: utf-8 -*-

# https://docs.python.org/3/library/secrets.html#module-secrets
# https://docs.python.org/3/library/random.html

import string
import secrets
alphabet = string.ascii_letters + string.digits
while True:
    password = ''.join(secrets.choice(alphabet) for i in range(24))
    if (any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and sum(c.isdigit() for c in password) >= 3):
        break

print(password)