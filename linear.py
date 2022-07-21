def search(list1,key):
     list1=[]
     flag = False
     for i in range(len(list1)):
          if key==list1[i]:
              flag=True
              list1.append(i)
              
     if flag==True:
         print("key element is found at index:")
         for i in list1:
             print(i)
              
     else:
        print("key element is not found")
              
          
list1=[34,23,5,6,7,1,23,8]
print(list1)
key=int(input("Enter the key element:"))
search(list1,key)