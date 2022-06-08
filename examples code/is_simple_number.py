def is_simple_number(x):
  """ Определяет, является ли число простым.
      х - целое положительное число.
      Если простое, то возвращает True,
      а иначе - False
  """
  divisor = 2
  while divisor < x:
    if x % divisor == 0:
      return print("False")
    divisor += 1
  return print("True")
print(is_simple_number(8))
help(is_simple_number) # вызов документа-строки