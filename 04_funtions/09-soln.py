def even_no(limit):
    for i in range(2, limit+1, 2):
        yield i


for num in even_no(10):
    print(num)