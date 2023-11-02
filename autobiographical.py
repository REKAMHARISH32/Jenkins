
def Find_Count(n):
	n_sum=sum(map(int,n))
	if n_sum == len(n):
		unique_digits=set(n)
		return len(unique_digits)
	return 0
def main():
	n=input()
	print(Find_Count(n))
if __name__ == "__main__":
	main()