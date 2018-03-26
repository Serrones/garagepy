import timeit

def reverse_01(x):
    return x[::-1]

def reverse_02(x):
    return ''.join(reversed(x))

def reverse_03(x):
    lista = list(x)
    for i in range(len(lista) // 2):
        temp = lista[i]
        lista[i] = lista[len(x) - i - 1]
        lista[len(x) - i - 1] = temp
    return ''.join(lista)

s = 'abcdefghijklmnopqrstuvwxyz' * 3

print('reverse_01 processing: ')
print(timeit.repeat(lambda: reverse_01(s)))
print('reverse_01 done')
print('reverse_02 processing: ')
print(timeit.repeat(lambda: reverse_02(s)))
print('reverse_02 done')
print('reverse_03 processing: ')
print(timeit.repeat(lambda: reverse_03(s)))
print('reverse_03 done')
