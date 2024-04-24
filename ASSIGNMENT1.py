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