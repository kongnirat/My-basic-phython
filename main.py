x=20
y = 12
b = 30
a = "45"

#แปลงเป็นstringโดยใช้str
print('ผลลัพธ์ = '+str(x))

#ตัวเช็ตข้อมูล
print(type(x))

#การแปลงจาก str เป็น int,foat
result = y+int(a)#สามารภเปลี่ยนเป็น foatได้โดยนำไปวางไว้แทน int
print(result)

#function input
print('hello bro what your name?')
firstname = input ('your name: ')#รับค่าที่ user พิมพ์ลงตัวแปรfirstname
lastname =input('your last name: ')
print('hello' ,firstname + lastname)

#คณิตศาสตร์
print('บวก' ,y+x)
print('ลบ' ,y-x)
print('คูณ' ,y*x)
print('หาร' ,y/x)
print('หารปัดเศษ' ,y//x)
print('ยกกำลัง' ,y**x)
print('หารเอาเศษ' ,y%x)

#ตัวเปรียบเทียบ
#เป็นการเปรียบเทียบค่าอย่างน้อย 2 ค่า
#คำตอบจะเป็น true/false
print('ค่า x มากกว่า y หรือไม่ ? : ' ,x>y)
print('ค่า x น้อยกว่า y หรือไม่ ? : ' ,x<y)
print('ค่า x เท่ากับ y หรือไม่ ? : ' ,x==y)
print('ค่า x ไม่เท่ากับ y หรือไม่ ? : ' ,x!=y)

print('ค่า x มากกว่า หรือ เท่ากับ y หรือไม่ ? : ' ,x>=y)#ถ้าค่าตัวใดตัวหนึ่งเป็นจริงค่าก็จะเป็น true แต้ถ้าเป็น false ก็จะเท็จทั้งหมด
print('ค่า x น้อยกว่า หรือ เท่ากับ y หรือไม่ ? : ' ,x<=y)

print('ค่า x มากกว่า y และ y มากกว่า b หรือไม่ ? : ' ,x>y>b)#ถ้ามีค่าตัวใดตัวหนึ่งเเป็น false ก็จะตอบออกมาเป็น false ทันที่ถ้าต้องการ true ค่าทั้งสองจะต้องเป็นจริงทั้งคู่
print('ค่า x น้อยกว่า y และ y น้อยกว่า b หรือไม่ ? : ' ,x<y<b)
print('ค่า b มากกว่า y และ y น้อยกว่า x หรือไม่ ? : ' ,b>y<x)

#ตรรกศาสตร์
#คำตอบจะเป็น true/false
#AND = และ (ถ้ามีตัวใดเป็นเท็จจะเป็นเท็จทั้งหมด)
q = (2>4) #type = bool
e = (4==2)#type = bool

z = q and e # z = (2>4) and (4==2)
r = (4>2) and (4==4)

print(z)#False
print(r)#True

#OR = หรือ (ถ้ามีตัวใดเป็นจริงก็จะเป็นจริงทั้งหมด)
k = q or e 
o = (4>2) or (4==4)

print(k)#False
print(o)#True

#NOT = ไม่ (ทำให้เป็นค่าตรงข้าม)
print(not k)#True
print(not o)#False

#Compound Assignment(เป็นตัวดำเนินการเพิ่มหรือลดเพื่อการเปลี่ยนแปลงค่าของตัวแปร)
u = 20
print("ก่อน" ,u)
u = u+5
print("หลัง" ,u)




