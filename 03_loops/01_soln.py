number = [1 , -2 , 3 , -4 , 5 , 6 , -7 , -8 , 9 , 10]
count = 0
for num in number:
    if(num > 0):
        count += 1
        print("Pos: ", num, end="\n")
        
print(count)