import secrets

# Generate secure tokens:
print(secrets.token_bytes(16))
print(secrets.token_hex(16))
print(secrets.token_urlsafe(16))

# Picking a random element from a sequence:
print(secrets.choice('abcdefghij'))

# Securely compare two strings for equality
# (Reduces the risk of timing attacks)):
print(secrets.compare_digest('abcdefghij', '123456789'))
print(secrets.compare_digest('123456789', '123456789'))
print(secrets.compare_digest('alpha', 'ALPHA'))
print(secrets.compare_digest('alpha', 'alpha'))

print(secrets.SystemRandom())



"""
b'C\xd2\x0f\xc5*\xd6q@{V fS\xaa\x96\x97'
a060f5ff43c65ffd267c872ddd6ecf2c
ygyppotXEV-KFz01YcHb7A
g
False
True
"""