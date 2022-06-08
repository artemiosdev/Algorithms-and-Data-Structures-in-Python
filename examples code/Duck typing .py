def max2(x, y):
  if x > y:
    return x
  return y
	
def max3(x, y, z):
  return max2(x, max2(y,z))

number = max3(5,6,7)
print(number)
print(max3(5.1, 5.2, 5.3))
print(max3("a", "ab", "abc"))
print(max3("cat", "cot", "cit"))