import numpy as np
arr1 = np.array([(8,9),(10,12),(13,14)])

print(arr1[0:2,1])

arr2 = np.array([10,20,30])
print(arr2.min())
print(arr2.max())
print(arr2.sum())



arr3 = np.array([(1,2,3),(4,5,6)])
print(arr3.sum(axis=1))

arr4 =np.array([(4,9,6),(11,13,15)])
print(np.sqrt(arr4))
print(np.std(arr4))
print()
arr5 = np.array([(1,2,3),(3,4,5)])
arr6 = np.array([(1,2,3),(3,4,5)])


print(arr5+arr6)
print(arr5-arr6)
print(arr5*arr6)
print(arr5/arr6)
print(arr5//arr6)

print()
x = np.array([(1,2,3),(4,5,6)])
y = np.array([(1,2,3),(4,5,6)])

print(np.vstack((x,y)))
print()
print(np.hstack((x,y)))


print("-----------------")

z = np.arange(1,21,3)
print(np.sin(z))
print(np.log2(z))