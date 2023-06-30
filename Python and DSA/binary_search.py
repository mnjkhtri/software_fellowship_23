# recursive 
def binary_search(arr,low, high, el):

    if low > high:
        return "No element in the array."
    else:
        mid = (low + high) //2
        if arr[mid] == el:
            return f"Element at {mid}"
        elif el < arr[mid]:
            return binary_search(arr,low, mid-1, el)
        else:
            return binary_search(arr,mid+1, high, el)


def binary_searchi(arr, el):
    low = 0
    high = len(arr) -1
    while low <= high:
        mid = (low+high)//2
        if (arr[mid] == el):
            return f"{el} at {mid}"
        elif el < arr[mid]:
            high = mid-1 
        else:
            low = mid+1
        
    return "No element in the array."

x = [1,4,7,9,12,22, 32,45,56, 64, 78]
for i in x:
    print(binary_search(x,0,len(x)-1, i))
    print(binary_searchi(x, i))






