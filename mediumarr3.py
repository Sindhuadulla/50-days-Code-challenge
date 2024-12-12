# Python3 program to find
# minimum number of swaps
# required to sort an array

# Return the minimum number
# of swaps required to sort
# the array


def minimum_rotations_sort_array(arr):
    N=len(arr)
    rotations=0
    temp=arr.copy()

    temp.sort() 
    hash_set={}
  
    for i in range(N):
        hash_set[arr[i]]=i 
    
    res=0

    for i in range(N):
        if (arr[i] != temp[i]):
            rotations+=1
            res=arr[i]

            arr[i],arr[hash_set[temp[i]]]=arr[hash_set[temp[i]]],arr[i] 
            hash_set[res]=hash_set[temp[i]]
            hash_set[temp[i]]=i 
    return rotations
print(minimum_rotations_sort_array([101,758,315,730,472,619,460,479]))

    


    