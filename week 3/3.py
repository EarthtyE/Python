#Thanyakorn Sutthiprapa 633050337-4
#แบบฝึกหัดที่ 3.1
"""print("\tเลือกเมนูเพื่อทำรายการ")
print("#"*50)
print("\tกด 1 เลือกจ่ายเพิ่ม")
print("\tกด 2 เลือกเหมาจ่าย")
choose = int(input(" ")) #เลือกจ่ายเพิ่มหรือเหมาจ่าย
km = int(input("กรุณากรอกระยะทาง กิโลเมตร\n")) #กรอกระยะทาง
if choose == 1 : #เลือกแบบจ่ายเพิ่ม
    if km <= 25: #ถ้าไม่ถึง 25 km จ่าย 25 บาท
        print("ค่าใช้จ่ายรวมทั้งหมด 25 บาท") 
    elif km > 25: #ถ้าเกิน 25 km จ่าย 25+55 บาท
        print("ค่าใช้จ่ายรวมทั้งหมด 80 บาท")
if choose == 2 : #เลือกแบบเหมาจ่าย
    if km <= 25: #ถ้าไม่เกิน 25 km จ่าย 25 บาท
        print("ค่าใช้จ่ายรวมทั้งหมด 25 บาท")
    elif km > 25: #ถ้าเกิน 25 km จ่าย 55 บาท
        print("ค่าใช้จ่ายรวมทั้งหมด 55 บาท")"""

#แบบฝึกหัดที่ 3.2
'''a1=int(input("กรุณากรอกจำนวนครั้งการรับค่า\n"))
a2 = 0
a3 = 1
while(a3 <= a1) :
    num = int(input("กรอกตัวเลข : "))
    a2 += num
    a3+=1
print("ผลรวมค่าที่รับมาทั้งหมด = %d"%a2)'''

#แบบฝึกหัด 3.3
"""print("ป้อนชื่ออาหารสุดโปรดของคุณ หรือ exitเพื่อออกจากโปรแกรม")
a1 = []
i = 0
while(True) :
    i += 1
    food = input("อาหารโปรดอันดับที่ {} คือ \t".format(i))
    a1.append(food)
    if food == "exit" :
        break
print("อาหารสุดโปรดของคุณมีดังนี้ ",end= "")
for x in range(1,i):
        print(x,".",a1[x-1],end=" ")"""
"""
#แบบฝึกหัด 3.4
a = []
while True :
    b = input('----ร้านคุณหลินบิวตี้----\n เพิ่ม [a]\n แสดง [s]\n ออกจากระบบ [x]\n')
    b = b.lower()
    if b == 'a' : 
        c = input('ป้อนรายชื่อลูกค้า(รหัส : ชื่อ : จังหวัด)')
        a.append(c)
        print('\n*******ข้อมูลได้เข้าสู่ระบบแล้ว*******\n')
    elif b == 's' : 
        print('{0:-<30}'.format(""))
        print('{0:-<8}{1:-<10}{2:10}'.format('รหัส','ชื่อ','จังหวัด'))
        print('{0:-<6}{0:-<10}{0:-<10}'.format(""))
        for d in a : 
            e = d.split(":")
            print('{0[0]:<6} {0[1]:<10}({0[2]:<10})'.format(e))
            continue
    elif b == 'x' : 
        c=input("ต้องการปิดโปรแกรมใช่หรือไม่ : ")
        if c =="ใช่":
            print("จบการทำงาน")
            break
        else : 
            continue
"""
# 3.5
score_l = ['90-100','80-89', '70-79', '60-69','50-59', '0-49']
sum_s = [0,0,0,0,0,0] 
n = int(input("จำนวนนักเรียนที่คุณต้องการ :"))
i = 0
while i < n: 
    score = int(input("คะแนนของนักเรียนคนที่ "+str(i+1)+" :"))
    i +=1 
    if score<=100 and score>=90:
        sum_s[0] +=1 
    elif score<98 and score>=80:
        sum_s[1] +=1 
    elif score<88 and score>=70:
        sum_s[2] +=1 
    elif score<70 and score>=60:
        sum_s[3] +=1 
    elif score<60 and score>=50:
        sum_s[4] +=1 
    else:
        sum_s[5] +=1 
for j in range(0,6): 
    print(score_l[j],":", sum_s[j]*"/") 