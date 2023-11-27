def   binS(x,max,min): 
    min=min
    max=max
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
    print("This element is not present")
    return(None)

def   binSMAX(x,max,min): 
    min=min
    max=max
    mid=(min+max)//2

    while min<max:
        if x<arr[mid]:
            max=mid-1
            mid=(min+max)//2
        if x==arr[mid]:
            min=mid+1
            mid=(min+max)//2   
    if arr[mid]!=x:
        mid-=1#Just to make sure
    return(mid)

def   binSMIN(x,max,min): 
    min=min
    max=max
    mid=(min+max)//2
    
    while min<max:
        if x>arr[mid]:
            min=mid+1
            mid=(min+max)//2
        if x==arr[mid]:
            max=mid-1
            mid=(min+max)//2
    if arr[mid]!=x:
        mid+=1#Just to make sure
    return(mid)
        
x = 0   #Element we are searching for
arr= []#Sorted Array
max=len(arr)-1
y=binS(x, max, 0)#Looking for some instance (what are we looking for, Maximum, Minimum)

if y!=None:
    minimal_index=binSMIN(x,y,0)#(what are we looking for, Maximum, Minimum)
    maximal_index=binSMAX(x,max,y)#(what are we looking for, Maximum, Minimum)
    print(maximal_index)
    print(minimal_index)





