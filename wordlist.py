from colorama import Fore

try:
	kata = input("Masukkan String\t\t:")
	limit = int(input("Masukkan Limit Angka\t:"))
	file = input("Masukkan Nama Wordlist\t:")

	def gen(digit, file, kata=None):
		for x in range(1, digit + 1):
			output = open(file, "a")
			result = ""
			if(kata != None):
				result = kata
			
			result += str(x)

			output.write(result + "\n")
			output.close()
			print(Fore.GREEN + result)


	if(kata != ""):
		gen(limit, file, kata)
	else:
		gen(limit, file)

except:
	print(Fore.RED + "Limit di isi dengan angka !!!")