#to add an element into a list without using any inbuilt functions

a = [1,2,3,4,5]
a[len(a):] = [6]
print("The new list after adding", a)


#to remove an element from an list without using any inbuilt functions
b = [1,2,3,4,5,6]
i = 5
c = b[:i] + b[i+1:]
print("The New List after deletion", c)
