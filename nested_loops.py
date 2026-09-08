'''generate pairs divisible by 2'''
# def pairs():
#     i=1
#     while i<=5:
#         j=1
#         while j<=5:
#             if (i+j)%2==0:
#                 print(f'({i},{j})')
#                 j+=1
#             j+=1
#         i+=1
# pairs()        

'''pairs product greater then 30'''
# def pairs():
#     i=1
#     while i<=10:
#         j=1
#         while j<=10:
#             if (i*j)>30:
#                 print(f'({i},{j})')
#                 j+=1
#             j+=1
#         i+=1
# pairs()    

'''Factors of a number and sum'''
# def factors():
#     while True:
#         num=int(input("Enter a number:"))
#         if num==0:
#             break
#         sum=0
#         factors=[]
#         for i in range(1,num+1):
#             if num%i==0:
#                 factors.append(i)
#                 sum+=i
#         print(f'Factors = {factors}')
#         print(f'sum = {sum}')        

# factors()

'''even numbers count'''
# def evencount(list1):
#     for i in list1:
#         ind=1
#         count=0
#         while ind<=i:
#             if ind%2==0:
#                 count+=1
#             ind+=1    
#         print(f'{i} even count = {count}')
        

# evencount([12,7,30,22])                

