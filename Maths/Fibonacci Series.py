# Fibonacci Series

# title
print("------------------------------------------------".center(100))
print("\tFibonacci Series")
print()

# main func
def main_fib(ask):

	# initial values
	a = 0
	b = 1
	print(f"The Fibonacci Series upto {ask}th term is:", end = " ")
	print(a, b, end = " ")
	
	# for loop
	for i in range(ask-2):
		c = a + b
		print(c, end = " ")
		a, b = b, c
	
# run_main
if __name__ == '__main__':
	# input from client
	ask_series = int(input("Enter the length of the series: "))
	main_fib(ask_series)

