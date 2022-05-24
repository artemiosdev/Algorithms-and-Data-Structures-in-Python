N = int(input())
A = [0] * N  # созданим массив элементов числа введенного с клавиатуры, и заполним нулями
B = [0] * N

for k in range(N):
    A[k] = int(input())  # заполним массив числами
print(A)

for k in range(N):
    B[k] = A[k]  # скопируем в другой массив каждый элемент
print(B)

# если мы к примеру сделаем `C = A`, то новый объект не создается, и С является всего лишь ссылкой на массив А

C = A
A[0] = 100
print(C[0])  # 100, ссылается на значение A[0]

# есть в языке возможность сделать дубликат массива с помошью list()
C = list(A)
print("Дубликат списка А -", C)