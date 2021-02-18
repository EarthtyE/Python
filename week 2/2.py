#Thanyakorn Sutthiprapa 633050337-4
"""
Booleans
"""
"""
2.1
x = input('Input First Number :')
y = input('Input Second Number :')
print('%s = '%x,'%s'%y, ':' ,x==y)
print('%s > '%x,'%s'%y, ':' ,x>y)
print('%s < '%x,'%s'%y, ':' ,x<y)
"""
"""
a = 60
b = 13
c = 0

c =a & b
print(c)

c =a | b
print(c)

c =a ^ b
print(c)

c =~a
print(c)

c =a << 2
print(c)

c =a >> 2
print(c)
"""

"""
#Thanyakorn Sutthiprapa 633050337-4
#Day Converter Program
x=int (input("Number of Days-->"))
print("Days--> Hour :",24*x,"Hour")
print("Days--> Minutes :",24*60*x,"Minutes")
print("Days--> Seconds :",24*60*60*x,"Seconds")
"""

"""
friend=['jan','cream','phu','bam','orm','pee','bas','kong','da','james']
friend[9]="may"
friend[3]="boat"
print(friend[3:8])
"""

"""
friend=['jan','cream','phu','bam','aom','pee','bas','kong','da','james']
friend.append("dome")
friend.append("poondang")
friend.insert(1,"cse")
friend.insert(8,"ped")
friend.remove("aom")
friend.pop(3)
del friend[7]
friend.clear()
del friend
print(friend)
"""

"""
#Thanyakorn Sutthiprapa 633050337-4
#รายการอาหารที่หยิบ
food = []
for i in range(1,6):
    number_food = input("หยิบสินค้าชิ้นที่ %d : "%i)
    food.append(number_food)
print("สินค้าที่หยิบใส่ตะกร้ามีดังนี้\n 1.",food[0])
print("2.",food[1])
print("3.",food[2])
print("4.",food[3])
print("5.",food[4])
"""

four = {
    'ลาดกระบัง-บางบ่อ' : '30 บาท',
    'ลาดกระบัง-บางปะกง' : '45 บาท',
    'ลาดกระบัง-พนัสนิคม' : '55 บาท',
    'ลาดกระบัง-บ้านบึง' : '60 บาท',
    'ลาดกระบัง-บางพระ' : '80 บาท'
}

six = {
    'ลาดกระบัง-บางบ่อ' : '45 บาท',
    'ลาดกระบัง-บางปะกง' : '45 บาท',
    'ลาดกระบัง-พนัสนิคม' : '75 บาท',
    'ลาดกระบัง-บ้านบึง' : '90 บาท',
    'ลาดกระบัง-บางพระ' : '100 บาท'
}

moresix = {
    'ลาดกระบัง-บางบ่อ' : '60 บาท',
    'ลาดกระบัง-บางปะกง' : '70 บาท',
    'ลาดกระบัง-พนัสนิคม' : '110 บาท',
    'ลาดกระบัง-บ้านบึง' : '130 บาท',
    'ลาดกระบัง-บางพระ' : '140 บาท'
}
print('โปรแกรมคำนวณค่าผ่านทางมอเตอร์เวย์')
print('รถยนต์ 4 ล้อ กด 1\nรถยนต์ 6 ล้อ กด 2\nรถยนต์มากกว่า 6 ล้อ กด 3\n')

a=int(input('เลือกประเภทพาหนะ :'))
if a==1:
    print('ค่าบริการรถยนต์ 4 ล้อ')
    print(*four.items(), sep='\n')
if a==2:
    print('ค่าบริการรถยนต์ 6 ล้อ')
    print(*six.items(), sep='\n')
if a==3:
    print('ค่าบริการรถยนต์มากกว่า 6 ล้อ')
    print(*moresix.items(), sep='\n')