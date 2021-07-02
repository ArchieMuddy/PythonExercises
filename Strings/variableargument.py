def add(a, *b):
    c = a + (ele for ele in *b)
    print(c)

add(2, 3, 4, 5)