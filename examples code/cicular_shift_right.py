array = [0, 1, 2, 3, 4]
tmp = array[len(array)-1]
for k in range(len(array)-2, -1, -1):
    array[k + 1] = array[k]
array[0] = tmp
print(array)