array = [0, 1, 2, 3, 4]
tmp = array[0]
for k in range(len(array)-1):
    array[k] = array[k + 1]
array[len(array)-1] = tmp
print(array)
