def binarysearch(list1,key):
  low=0
  high=len(list1)-1
  Found = False
  while low<=high and not Found:
     mid=low+high//2
     if key==list1[mid]:
       Found = True
     elif key>list1[mid]:
       low=mid+1
     else:
       high=mid-1
  if Found==True:
        print("Key is found")
  else:
        print("Key is not found")
list1=[23,1,4,2,3]
list1.sort()
print(list1)
key = int(input("Enter the key:"))
binarysearch(list1,key)