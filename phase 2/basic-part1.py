#การใช้ list
#การเขียนแบบ primitive
number = [1,2,2,5,4,6,5,6]
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