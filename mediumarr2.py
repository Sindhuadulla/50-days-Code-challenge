def sort_array(arr):
    n=len(arr)
    i=0 
    while i<n:
        correct=arr[i]-1

        if arr[correct]!=arr[i]:
            swap(arr,i,correct) 
        else:
            i=i+1
    return arr

    
def swap(arr,first,second):
    temp=0
    temp=arr[first]
    arr[first]=arr[second] 
    arr[second]=temp
    return arr
print(sort_array([3,2,5,6,1]))


