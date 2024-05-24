class Calculation:
    def __init__(self) -> None:
        self.num1 = None
        self.num2 = None
    def sume (self):
        return (self.num1 + self.num2)
    def tafrigh (self):
        return (self.num1 - self.num2)
    def zarb (self):
        return (self.num1 * self.num2)
    def taghsim (self):
        return (self.num1 / self.num2)
  
choise = None
while(choise != "payan"):
    choise = int(input("please choise your number : 1_sume , 2_tafrigh , 3_zarb , 4_taghsim , 5_payan :"))
    if(choise == 1):
         x = int(input("please enter a number1 : "))
         y = int(input("please enter a number1 : "))
         result_sume = Calculation(  )
         result_sume.num1 = x
         result_sume.num2 = y
         print("Sume : ", result_sume.sume())
    elif(choise == 2):
        x = int(input("please enter a number1 : "))
        y = int(input("please enter a number1 : "))
        result_tafrigh = Calculation(  )
        result_tafrigh.num1 = x
        result_tafrigh.num2 = y
        print("Tafrigh : ", result_tafrigh.tafrigh())
    elif(choise == 3):
        x = int(input("please enter a number1 : "))
        y = int(input("please enter a number1 : "))
        result_zarb = Calculation(  )
        result_zarb.num1 = x
        result_zarb.num2 = y
        print("Zarb : " , result_zarb.zarb())
    elif(choise == 4):
        x = int(input("please enter a number1 : "))
        y = int(input("please enter a number1 : "))
        result_taghsim = Calculation( )
        result_taghsim.num1 = x
        result_taghsim.num2 = y
        print("Taghsim : " , result_taghsim.taghsim())
    elif(choise == 5):
        break


        