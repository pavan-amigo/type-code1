def convertToBasethree(N):
	if (N == 0):
		return;
	x = N % 3;
	N //= 3;
	if (x < 0):
		N += 1;
	convertToBasethree(N);
	if (x < 0):
		print(x + (3 * -1), end = "");
	else:
		print(x, end = "");
def convert(Decimal):
	
	print("Ternary number of ", Decimal,
		" is: ", end = "");
	if (Decimal != 0):
		convertToBasethree(Decimal);
	else:
		print("0", end = "");
if __name__ == '__main__':
	Decimal = int(input())
	convert(Decimal);
