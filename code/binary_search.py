def bin_search(arr,x): 
    #arr is an ordered list 
    #x is the number we are searching for
    min=0
    max=len(arr)-1
    mid=(min+max)//2
    while min<max:
        if x>arr[mid]:
            min=mid+1
            mid=(min+max)//2
        if x<arr[mid]:
            max=mid-1
            mid=(min+max)//2
        if x==arr[mid]:
            x==arr[mid]
            return(mid)
    return(-1)
    #function will return -1 if x is not present

        
