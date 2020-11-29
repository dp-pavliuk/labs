print("First constant", False)
print("Second constant", True)
print("Third constant", None)

print(abs(-0.5), f"equal {abs(0.5)}")
print(bin(322))
print(float('+3.22'))

C = True
print("So C=True" if C else " So C=False")

C = False
print("So C=True" if C else " So C=False")

B = 0
try:
	print("What if", 10/B, "?")
except Exception as e:
	print(e)
finally:
	print("There is !")

with open("README.md", "r") as f:
	for line in f :
		print(line)

full_name = lambda first, last: f'Full name{first} {last}'
full_name('Danylo','Pavliuk')
print("Simple function", full_name)
print("Call function", full_name ('Danylo', 'Pavliuk'))