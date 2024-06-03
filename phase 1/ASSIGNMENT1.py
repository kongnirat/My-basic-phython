#โปรแกรมคำนวณดัชนีมวลกาย
#BMI = กิโลกรัม (kg) / ส่วนสูง * ส่วนสูง (m)

#input
weight = int (input("พิมพ์น้ำหนักของคุณ (kg) : "))
hight = int (input("พิมพ์ส่วนสูงของคุณ (cm) : "))

#process
#cm to m
hight = hight/100

#calculate bmi
bmi = weight/(hight**2)

#output
print("BMI = " ,bmi)

if bmi <= 18.50 :
    print("น้ำหนักน้อย/ผอม")
    print("ภาวะเสี่ยงต่อโรคมากกว่าคนปกติ")

elif bmi >= 18.50 and bmi <=22.90 :
    print("ปกติ(สุขภาพดี)")
    print("ภาวะเสี่ยงต่อโรคเท่าคนปกติ")
    
elif bmi >= 23.00 and bmi <=24.90 :
    print("ท้วม/โรคอ้วนระดับ1")
    print("ภาวะเสี่ยงต่อโรคอันตรายระดับ1")
    
elif bmi >= 25.00 and bmi <=29.90 :
    print("อ้วน/โรคอ้วนระดับ2")
    print("ภาวะเสี่ยงต่อโรคอันตรายระดับ2")

elif bmi >= 30.00 :
    print("อ้วนมาก/โรคอ้วนระดับ3")
    print("ภาวะเสี่ยงต่อโรคอันตรายระดับ3")

