def main():
	randomString = "aksdna skldn alknd"

	for character in randomString:
		if character == "a":
			randomString = str.replace("a", "b")
	print(randomString)

