x=20
y = 12
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
print('ค่า x มากกว่า y หรือไม่ ? : ' ,x>y)
print('ค่า x น้อยกว่า y หรือไม่ ? : ' ,x<y)