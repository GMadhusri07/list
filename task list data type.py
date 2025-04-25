# 1.implement the count method on a list by taking input from the user without using the actual method.

num=[1,2,2,3,4,5,6,6,6,6,7,7,7,8,8,8,8,9]
ele=int(input("enter a num from list to count : "))
count=0
for ind in range(0,len(num)):
    if num[ind]==ele:
        count+=1
print(count)


# 2.implement the copy method on a list just as the above condition.
user_input=input("enter a elements in list seperated by spaces : ")
actual_list=[int(x) for x in user_input.split()]
copied_list=[]
for ind in range(0,len(actual_list)):
    copied_list.append(actual_list[ind])
print(copied_list)