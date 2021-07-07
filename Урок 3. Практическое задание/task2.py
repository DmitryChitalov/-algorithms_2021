from uuid import uuid4
import hashlib

salt = uuid4().hex
password = input("Input password ")

res = hashlib.sha256(salt.encode() + password.encode()).hexdigest()
print(f'In DB save: {res}')

try_pass = input("Repeat password ")
if hashlib.sha256(salt.encode() + try_pass.encode()).hexdigest() == res:
    print("Successful")
else:
    print("Wrong password ")
