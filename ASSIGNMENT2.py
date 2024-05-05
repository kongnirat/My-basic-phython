#โปรแกรมเปรียบเทียบค่าตัวเลข

A = int(input("พิมพ์ตัวเลข: "))
B = int(input("พิมพ์ตัวเลข: "))

if A>B :
    print(A , "มากกว่า" , B)
    if A<B : 
        print(A , "น้อยกว่า" ,B)

else :
    print(A, "เท่ากับ" ,B)
    
print("จบการทำงาน")