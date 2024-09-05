#การใช้ list
#การเขียนแบบ primitive
number = [1,2,2,5,4,6,5,6]
animal = ["cat","dog","fish","bird"]

#การเรียกใช้ข้อมูลจากซ้ายไปขวา
print(number[1])
print(number[1:3])

#การเรียกใช้ข้อมูลจากขวาไปซ้าย
print(number[-3])
print(number[-3:-1])

#การแก้ไขข้อมูลใน list
print('ก่อนแก้ไขข้อมูล => ',number)
number[2]=9
number[-2]=4
print("หลังแก้ไข =>" ,number)

#การแสดงผลด้วย loop
sum=0
for x in number:
    print(x)
print(sum)      

#การเช็คข้อมูลในตัวแปร
if 6 in number:
    print("T")
else:
    print("F")
    
#แสดงจำนวนสมาชิก
print(len(number))

#len() ทำงานร่วมกับ loop
for i in range(len(number)):
    print(number[i])
    
#การเพิ่มข้อมูล
animal.append("duck")#ต่อท้าย
animal.insert(1, "wolf")#แทรกข้อมูล

print(animal)

#การลดข้อมูล
animal.remove("cat")#ลบข้อมูล
animal.pop()#ลบข้อมูลตัวหลังสุด
del animal[1]#ลบindex
animal.clear()#ล้างข้อมูลสมาชิกของ list

print(animal)

#หารคัดลอกข้อมูลจาก list 1 = list 2
z = []
print(z)
z = animal.copy()
print(z)                 

#การรวมข้อมูล
allGroup = number + animal
print(allGroup)

#การแสดงจำนวนสมาชิก
a = number.count(6)
print(a)

#การรวมข้อมูล2
number.extend(animal)

print(animal)

#การใช้ turple เป็นข้อมูลที่ไม่สามารถเปลี่ยนแปลงได้
tup = (1,2,3,4)#this is turple
tupC = tuple((1,2,3,4))#this is turple but constructor

print(tup)

#การเข้าถึงข้อมูล
#การเรียกใช้ข้อมูลจากซ้ายไปขวา
print(tup[1])#การเข้าถึงข้อมูลผ่านindexเหมือนlist
print(tup[0:3])

#การเรียกใช้ข้อมูลจากขวาไปซ้าย
print(tup[-3])#การเข้าถึงข้อมูลผ่านindexเหมือนlist
print(tup[-3:-1])

#การแก้ไขข้อมูล
#แปลงจาก tuple to list
lis = list(tup)
lis[0] = "bg"
print(lis)

#แปลงจาก list to tuple
tup = tuple(lis)
print(tup)

#แสดงผลโดยใช้loop
for item in tup:
    print(item)
    
#การตรวจสอบข้อมูล
if "bg" in tup :
    print("T")
else :
    print("F")
    
#การนับสมาชิก
print(len(tup))

#len ทำงานร่วมกับ loop for
for item in range(len(tup)):
    print(tup[item])
    
#การสร้างและเพิ่มจำนวนข้อมูล(join)
y = (1,)
v = (2 ,)
y = y+v #ถ้าจะเพิ่มสมาชิกให้นะturpleมาต่อกัน
print(y)

#การลบข้อมูลด้วยDel
del tup#ลบตัวแปรทิ้งทั้งหมด

#การลบข้อมูลสมาชิกให้เปลี่ยนไปเป็น list แล้วค่อยเปลี่ยน tuple

#การนับข้อมูลสมาชิก
b = tupC.count(4)
print(b)

#การค้นหาสมาชิกด้วย index
m = tupC.index(4)
print(m)

#การ sort ข้อมูล
#เป็นการเรียงตัวเลยซึ่งต้องทำให้ tuple เปลี่ยนเป็น list ก่อนจึงจะสามารถทำได้









