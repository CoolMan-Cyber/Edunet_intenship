# Variables
city_name = "Mumbai"
population = 39
b = "twenty two"
c = "degree"

print("City name :", city_name, "RTO ", "Tempreture is ", b, c)

print(f"City NAme : {city_name} RTO, Tempreture is {b}  {c}")

# Dictionary
this_dic1={
    "key": 1,
    "value":20,
    "key1":[1,2,3],
    "key2":[4,5,6],
    "key3":[9,8,7],
}
print(type(this_dic1))
print(this_dic1)

#List
key_list = ['names', 'rollno','stream']
print("1",type(key_list))
names_list=['gj','mh','rj']
roll_list=[1,11,111]
dictb=dict.fromkeys(key_list)
print("2",dictb)

dictb['names']=names_list
dictb['rollno']=roll_list
dictb['stream']=['ds','cs','ec']
dictb['city']=[1,2,3]
dictb.update({'aqi':[101,200,300]})
print("3",dictb)

print("4",dictb.items())
print("5",dictb.keys())
print("6",dictb.values())

#Tuples
t = (10, 20, 30, 20, 40)
print(t)
print(t.count(20))
print(t.index(30))

a = list(t)
a.append(50)
print(a)
a.reverse()
print(a)
print(len(t))

#Set
s = {10, 20, 30}
print(s)
s.add(40)
print(s)
s.remove(20)
print(s)
s.update([50, 60])
print(s)
s.pop()
print(s)

#if
a = 15
if a > 10:
    print("Number is greater than 10")
if a < 10:
    print("Number is smaller than 10")


#if-else
a = 7

if a % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

#if-elif-else
marks = 72

if marks >= 90:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
else:
    print("Grade C")

#nested if
age = 20

if age >= 18:
    if age >= 21:
        print("Can drive and vote")
    else:
        print("Can vote")
else:
    print("Not eligible")

#Break-continue-pass
for i in range(1, 11):
    if i == 6:
        break
    print(i)

for i in range(1, 11):
    if i == 6:
        continue
    print(i)

for i in range(1, 6):
    if i == 3:
        pass
    print(i)

#inpunt-range
name = input("Enter your name : ")

print("Welcome", name)

for i in range(5):
    print(i)

#len-type
names = ["Ram", "Shyam", "Mohan"]

print(len(names))

a = 10
b = "Hello"
c = 10.5

print(type(a))
print(type(b))
print(type(c))

#for-while loop
fruits = ["Apple", "Banana", "Mango"]

for i in fruits:
    print(i)

i = 1

while i <= 5:
    print(i)
    i = i + 1
