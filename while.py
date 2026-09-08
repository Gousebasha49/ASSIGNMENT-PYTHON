total=0
while True:
    num = int(input("Entr a positive value:"))
    if num > 0:
        break
    else:
        print('Please enter positive value')
for i in range(num+1):
    total+=i
print(f'The sum of 1 to {num} numbers is : {total}')           