#for

for i in range(1,11):
    print(i)


for i in range(2,51,2):
    print(i)


for i in range(10,0,-1):
    print(i)


n= int(input("Введите число: "))
count = 0
for i in range(1,n+1):
    count += i 
print(f"Сумма чисел от 1 до {n} = {count}")


n=int(input("Введите число: "))
fact = 1
for i in range(1,n+1):
    fact *= i
print(f"Факториал числа {n} = {fact}")


n=int(input("Введите число: "))
for i in range(1,11):
    print(f"{n} * {i} = n * i")


list1=[1,2,3,4,5,6,-1,-4]
count = 0 
for i in list1:
    if i > 0:
        count += 1
print(count)


str="я люблю питон"
abcd = "аеёиоуыэюя"
count = 0
for i in str:
    if i in abcd:
        count+=1
print(count)


list1=[1,2,3,4,5,6]
max = list1[0]
for i in list1:
    if i > max:
        max = i
print(max)


##########################################

#while

i = 1
while i <= 10:
    print(i)
    i+=1


x = int(input("Введите число "))
count = 0 
while x != 0:
    count += x 
    x = int(input("Введите число "))
print("Сумма ", count)


x = 5676876
count = 0 
while x > 0:
    count += 1
    x //= 10
print(count)


n = 123456
count = 0 
while n > 0:
    count += n % 10
    n //= 10 
print(count)

#5,6 - нет

correct_pass = "123"
pas = input("Введите пароль ") 
while pas != correct_pass:
    print("Неверный парлль")
    pas = input("Введите пароль ") 
print("Доступ разрешенн")




#словари

dict1={"Ivan": 5, "Anna":3, "Anastasia":5}
print(dict1["Ivan"])



dict1={1:"Яблоко", 2:"Помидор"}
dict1.update({3:"Банан"})
dict1[1] = "ГРуша"
del dict1[2]
print(dict1)



dict1={1:"Значение_1", 2:"Значение_2"}
print(dict1.get(1))


dict1={1:"bim", 2:"bam", 3:"bom"}
print(list(dict1.keys()))
print(list(dict1.values()))
print(len(dict1))


dict1={"Apple": 100, "Banana": 150, "Mango": 200}
for item,price in dict1.items():
    print(item,price)


dict1={"Apple": 100, "Banana": 150, "Mango": 200}
sum = sum(dict1.values())
print(sum)



str="bim bam bom"
dict1={}
for i in str:
    if i in dict1:
        dict1[i] += 1
    else:
        dict1[i] = 1
print(dict1)


dict1={"a": 1, "b": 2, "c": 3}
dict2={}
for key,value in dict1.items():
    dict2[value] = key
print(dict2)

