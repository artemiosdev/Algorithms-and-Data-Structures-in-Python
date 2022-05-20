def invert_array(a: list, n: int):
    """Обращение массива (поворот задом-наперёд)
        в рамках индексов от 0 до N-1
    """
    for k in range(n // 2):
        a[k], a[n - 1 - k] = a[n - 1 - k], a[k]


def test_invert_array():
    a1 = [1, 2, 3, 4, 5]
    print(a1)
    invert_array(a1, 5)
    print(a1)
    if a1 == [5, 4, 3, 2, 1]:
        print("#test1 - ok")
    else:
        print("#test1 - fail")

    a2 = [0, 0, 0, 0, 0, 0, 0, 10]
    print(a2)
    invert_array(a2, 8)
    print(a2)
    if a2 == [10, 0, 0, 0, 0, 0, 0, 0]:
        print("#test2 - ok")
    else:
        print("#test2 - fail")


test_invert_array()
