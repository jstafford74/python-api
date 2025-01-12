import secrets

secret = secrets.SystemRandom().getrandbits(128)

print(secret)
