import hashlib

print(hashlib.algorithms_guaranteed)


mystring = b"Hello Abinash"

sha 		= hashlib.sha256()
sha.update(mystring)
hash_string	=	sha.hexdigest()

print(f"{mystring}--{hash_string}")