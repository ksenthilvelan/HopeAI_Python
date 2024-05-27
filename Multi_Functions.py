# import decimal 
from decimal import Decimal

class Multiple_Functions():
    
    def Subfields():
        AI_Subfields=["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        print("Sub-fields in AI are : ")
        for Sub_AI in AI_Subfields:
            print(Sub_AI)
            
    def OddEven():
        num=int(input("Enter a Number : "))
        if (num%2 != 0):
            msg=print(num," is Odd Number")
        else:
            msg=print(num," is Even Number")
        return msg
    
    
    def BMI():
        weight=int(input("Enter the BMI Index:"))
        #print("Enter the BMI Index:",weight)
        if(weight<18.5):
            print("Under weight")
        elif(weight<25):
                print("Normal")
        elif(weight<30):
            print("Over weight")
        else:
            print("Very Overweight")
    
    
    def Eligible():
        Gender=input("Your Gender : ")
        Age=int(input("Your Age : "))
        if (Gender=="Male" and Age>21):
            msg=print("ELIGIBLE")
        elif(Gender=="Female" and Age>18):
            msg=print("ELIGIBLE")
        else:
            msg=print("NOT ELIGIBLE")
        return msg
    
    def Percentage():
        # from decimal import Decimal()
        subjects=["Subject1","Subject2","Subject3","Subject4","Subject5"]
        marks=[98,87,95,95,93]
        
        # zip() used to pair each elements between subject and marks
        for subjects,marks in zip(subjects,marks):
            print(subjects,"=",marks)

        # Now marks values changed, duplicating marks as array/list 
        marks1=[98,87,95,95,93]
        total=0
        for ele in range(0,len(marks1)):
            total = total + marks1[ele]
        print("Total : ",total)
        percentage = total/len(marks1)
        # print(percentage)
        
        # from decimal class importing  Decimal function
        percentage_decimal = decimal.Decimal(percentage)
        print("Percentage : ",percentage_decimal.quantize(Decimal("1.0000000000000")))
        
    def AreaTriangle():
        Height=int(input("Height : "))
        Breadth=int(input("Breadth : "))
        Area_of_Triangle=(Height*Breadth)/2
        print("Area of Triangle formula : (Height*Breadth)/2")
        print("Area of Triangle : ", Area_of_Triangle)

    def PerimeterTriangle():
        Height1=int(input("Height1 : "))
        Height2=int(input("Height2 : "))
        Breadth=int(input("Breadth : "))
        Perimeter_of_Triangle = Height1+Height2+Breadth
        print("Perimeter of Triangle : Height1+Height2+Breadth")
        print("Perimeter of Triangle : ",Perimeter_of_Triangle)