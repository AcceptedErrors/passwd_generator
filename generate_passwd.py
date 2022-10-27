import string
import random

def generate_pw(pwLen=25, chars=string.ascii_letters + string.digits + string.punctuation):
  return ''.join([random.choice(chars) for x in range(pwLen)])

if __name__ == "__main__":
	print("Generated password:")
	for i in range(1, 4):
		print(f" #{i} {generate_pw(65)}")