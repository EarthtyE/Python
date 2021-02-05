choice = 0 
def menu(): 
    global choice 
    print('Menu\n1. เพิ่มคำศัพท์ \n2. ลบคำศัทพ์\n3. แสดงคำศัพท์ทั้งหมด\n4. ออกจากโปรแกรม ')
    choice = input('กรุณาเลือกทำรายการ :')  
    
def openเพิ่ม(): 
    def Introduce(arg1, arg2 = 'com', arg3 = 'ed', arg4 = 'kku'):
        print("Hello, I am "+arg1+","+arg2+","+arg3+","+arg4)
        
    Introduce("Python")
    Introduce(arg1= "python")

def openแสดง():
    print("o")
    
def openลบ():
    print("o")

def openออก():
    print("o")
    
while True: 
    menu()
    if choice == '1': 
        openเพิ่ม() 
    elif choice == '2': 
        openแสดง()
    elif choice == '3': 
        openลบ()
    elif choice == '4': 
        openออก()
    else: 
        break