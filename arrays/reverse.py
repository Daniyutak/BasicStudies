
def reverse_array(a):
    c = a[:] #copia o array e nao o ponteiro em si
    c.reverse()
    return c

def reverse_array2(a):
    return a[::-1]

if __name__ == '__main__':
    a = [1, 2, 3, 4, 5]
    print(reverse_array(a))
    print(a)