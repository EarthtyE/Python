"""
# 5.1 Thanyakorn 633050337-4
class nisit :
    def __init__(self,name,surname,year,branch,sex) :
        self.name = name
        self.surname = surname
        self.year = year
        self.branch = branch
        self.sex = sex
    
    def shownisit(self) :
        print("----Nisit Properties----")
        print("Name :",self.name)
        print("Surame :",self.surname)
        print("Year :",self.year)
        print("Branch :",self.branch)
        print("Sex :",self.sex)
    
x = nisit("Thanyakorn","Sutthiprapa","1","COM","Mule")
x.shownisit()
"""

class nisit :
    def __init__(self,name,surname,year,branch,sex) :
        self.name =name
        self.surname = surname
        self.year = year
        self.branch = branch
        self.sex = sex
        
    def shownisit(self) :
        print("----Nisit Properties----")
        a =input("Name :")
        print("Name :",a)
        b =input("Surame :")
        print("Surame :",b)
        c =input("Year :")
        print("Year :",c)
        d =input("Branch :")
        print("Branch :",d)
        f =input("Sex :")
        print("Sex :",f)
    
x = nisit(a,b,c,d,f) :
x.shownisit()

def inputinfo():
    global hello, info, name, lastname, sex, year, department, hometown 
     print("-"*20+"แนะนำตัว"+"-"*20)
     info = input("ชื่อ:สกุล:เพศ:ชั้นปีที่ศึกษา:สาขาวิชา:จังหวัดภูมิลำเนา")
     allinfo = info.split(":") 
     name = allinfo[0] 
     lastname = allinfo[1] 
     sex = allinfo[2] 
     year = allinfo[3] 
     department = allinfo[4] 
     hometown = allinfo[5] 
      if (sex == "ชาย"):
        hello = 'สวัสดีครับ' 
      elif (sex == 'หญิง'):
        hello = 'สวัสดีค่ะ'

class nisit : 
    def __init__(self, name, lastname, sex, year, department, hometown):
    self.name = name 
    self.lastname = lastname 
    self.sex = sex 
    self.year = year 
    self.department = department
    self.hometown = hometown 
def showinfo(self):
    print(hello, self.name, self.lastname, self.sex, self.year,self.department, self.hometown)
inputinfo()
X = nisit(name, lastname, sex, year, department, hometown) 
X.show()

