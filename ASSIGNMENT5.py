#การแปลง พศ. ให้ไปเป็น รศ./ค.ศ./
number = int(input("ปี พศ. ที่ต้องการหา: "))
#หารศ.
รศ = number-2324
print("ปี รศ.: " ,รศ)
#หาคศ.
คศ = number-543
print("ปี คศ.: " ,คศ)

print("จบการทำงาน")

#การแปลง รศ. ให้เป็นพศ.
r = int(input("ปี รศ. ที่ต้องการหา: "))
p = r+2324
print("ปี พศ.: " ,p)#แปลงจากรศ.มาเป็นพศ.
print("จบการทำงาน")

#การแปลง คศ. ห้เป็นพศ.
c = int(input("ปี คศ. ที่ต้องการหา: "))
pa = c+543
print("ปี พศ.: " ,pa)#แปลงจากคศ.มาเป็นคศ.
print("จบการทำงาน")