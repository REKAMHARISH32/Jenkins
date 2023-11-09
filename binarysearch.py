#Note: For Binary search the input array must be in sorted and space complexity is O(log n)
def binary_search(arr,tar,low,high):
	if low<=high:
		mid=(low+high)//2
		if arr[mid]==tar:
			return mid
		elif arr[mid]<tar:
			return binary_search(arr,tar,mid+1,high)
		else:
			return binary_search(arr,tar,low,mid-1)
	else:
		return -1

arr=input("Enter your array:").split(",")

tar=int(input("Enter your target:"))

arr=[int(x.strip()) for x in arr]

result=binary_search(arr,tar,0,len(arr)-1)

if result!=-1:
	print(f"{tar} is found at index:{result}")
else:
	print(f"{tar} is not found in array.")
		