def search(array,x,no):
    for i in range(0,n):
        if arr[i]==x:
            return i
    return -1


arr=[1,2,3,4,5,6]
x=5
n=len(arr)

searching=search(arr,x,n)
if searching==-1:
    print("element not present")
else:
    print("element found and it is at index:"  +str(searching))