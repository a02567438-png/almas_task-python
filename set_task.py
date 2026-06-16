#to remove item(s) from a given set
#remove()method delete the item from the set
s={10,20,30,40}
s.remove(20)
print(s)

#remove an item from a set if it is present in the set.
#discard()remove the item is not present,no error occurs
s={1,2,3,4}
s.discard(3)
print(s)

#create set difference
a={1,2,3,4}
b={3,4}
c=a-b
print(c)

#remove all elements from a given set
#clear() method removes all ele from the set,making it empty
s={1,2,3,4}
s.clear()
print(s)

#the maximum and minimum values in a set
#max() returns the largest value in the set
#min() returns the smallest value in the set
s={10,20,30,40,50}
print("maximum:",max(s))
print("minimum:",min(s))
