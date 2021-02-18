#thanyakorn 633050337-4
import os
choice = 0 
listbar = [0,0,0,0,0]
pick = 0
def menu(): 
    global choice 
    print('Menu\n 1.แสดงรายการสินค้า \n 2.หยิบสินค้าใส่ตะกร้า\n 3.แสดงจำนวนแลราคาสินค้าที่เลือก\n 4.หยิบสินค้าออกจากตะกร้า\n 5.ปิดโปรแกรม ')
    choice = input('กรุณาเลือกทำรายการ :')
    screen_clear() 
    
def order(): 
    print("-------รายการสินค้า-------\n1. มิดไนท์(แบน) 139 บาท\n2. แสงโสม(แบน) 159 บาท\n3. ยูงทอง(แบน) 119 บาท\n4. หงส์ทอง(แบน) 149 บาท\n5. ลีโอ(ขวด) 69 บาท")


def pickmenu ():
    global pick
    print('\t\nรายการสินค้า\n1. มิดไนท์\n2. แสงโสม\n3. ยูงทอง\n4. หงส์ทอง\n5. ลีโอ')
    pick = int(input('เลือกหยิบสินค้าหมายเลข: '))
    if pick == 1:
        listbar[0] += 1
    elif pick == 2:
        listbar[1] += 1
    elif pick == 3:
        listbar[2] += 1
    elif pick == 4:
        listbar[3] += 1
    elif pick == 5:
        listbar[4] += 1
    screen_clear() 

def userpick():
    list_score = ['มิดไนท์','แสงโสม','ยูงทอง','หงส์ทอง','ลีโอ']
    list_price = [5,1,15,22,3]
    print("{0:-<13}{1:-<13}{2:-<13}{3}".format('สินค้า','ราคา','จำนวน','ราคารวม'))
    for i in range(0,5):
        print("{0:-<13}{1:-<13}{2:-<13}{3}".format(list_score[i],list_price[i],listbar[i],listbar[i]*list_price[i]))

def deleteuserpick():
    print('\t\nรายการสินค้า\n1. มิดไนท์\n2. แสงโสม\n3. ยูงทอง\n4. หงส์ทอง\n5. ลีโอ')
    depick = int(input("เลือกลำดับสินค้าที่จะหยิบออก หรือพิมพ์ -1 เพื่อออก"))
    if depick == 1:
        listbar[0] -= 1
    elif depick == 2:
        listbar[1] -= 1
    elif depick == 3:
        listbar[2] -= 1
    elif depick == 4:
        listbar[3] -= 1
    elif depick == 5:
        listbar[4] -= 1

def screen_clear():
    clearscreen = os.system('cls')

while True:
    menu()
    if choice == '1':
        screen_clear()
        order()
    elif choice == '2':
        screen_clear
        pick
    elif choice == '3':
        screen_clear
        userpick
    elif choice == '4':
        screen_clear
        deleteuserpick
    elif choice == '5':
        c = input("ต้องการใช้งานโปรแกรมต่อหรือไม่ y/n: ")
        if c.lower() == 'y':
            screen_clear
        elif c.lower() == 'n':
            screen_clear
            break


""" 
def chouse():
    food = []
    for i in range(1,6):
        number_food = input("หยิบสินค้าชิ้นที่ %d : "%i)
        food.append(number_food)
    print("สินค้าที่หยิบใส่ตะกร้ามีดังนี้\n1.",food[0])
    print("2.",food[1])
    print("3.",food[2])
    print("4.",food[3])
    print("5.",food[4])

  
while True: 
    menu()
    if choice == '1': 
        openorder() 
    elif choice == '2': 
        openหยิบใส่ตะกร้า()
    elif choice == '3': 
        print("-----จบการทำรายการ------")
        break
"""
        
