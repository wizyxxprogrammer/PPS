from Window import*
win=Window()

class solveProblem():
    def __init__(self,type=str,note=str,result=str):
        self.type=type
        self.note=note
        self.result=result
        self.input_var=input("Введите имя вводимой переменной:")#имя вводимой переменной
        self.dop_var=input("Введите имя дополнительной переменной:")#имя дополнительной переменной
        self.indent="   "
        self.indent_num=0
        self.data=[]#список вводиммых данных    
        self.res_data=[]#список данных получаемого результата
        self.code=[]#список кода, который выводится при результате
        match self.note:#проверка примечания
            case "NumOfNums":#кол-во вводимых чисел
                self.NumOfNums(int(input("Введите кол-во вводимых чисел:")))
            case "while!=0":#пока не 0
                self.while0()
            case _:
                win.error(0)
        match self.type:#проверка типа задачи
            case "crat":#задача на кратность 
                self.problem_crat(int(input("Введите кратное:")))
            case "last_num":#задача на последнее число
                self.problem_last_num(int(input("Введите последнее число:")))
            case _:
                win.error(0)
        match self.result:#проверка типа результата
            case "quantity":#кол-во
                self.res_quantity(self.res_data)
            case "sum":#сумма
                self.res_sum(self.res_data)
            case _:
                win.error(0)
        print("Code:")
        for i in range(len(self.code)):#вывод кода
            print(self.code[i])


    def NumOfNums(self,nums):#кол-во вводимых чисел
        self.code.append(f"n=int(input())")
        self.code.append(f"{self.dop_var}=0")
        self.code.append(f"for i in range(n):")
        self.indent_num+=1
        self.code.append(f"{self.indent*self.indent_num}{self.input_var}=int(input())")
        for i in range(nums):
            self.data.append(int(input(f"{i+1}:")))

    def while0 (self):#пока не 0
        self.code.append(f"{self.input_var}=1")
        self.code.append(f"{self.dop_var}=0")
        self.code.append(f"while {self.input_var}!=0:")
        self.indent_num+=1
        self.code.append(f"{self.indent*self.indent_num}{self.input_var}=int(input())")
        num=1
        input_var=int(input(f"{num}:"))
        while input_var!=0:
            num+=1
            input_var=int(input(f"{num}:"))
            self.data.append(input_var)


    def problem_crat(self,multiple):#задача на кратность 
        self.code.append(f"{self.indent*self.indent_num}if {self.input_var}%{multiple}==0:")
        self.indent_num+=1
        for i in range(len(self.data)):
            if self.data[i] % multiple==0:
                self.res_data.append(self.data[i])

    def problem_last_num(self,num):#задача на последнее число 
        self.code.append(f"{self.indent*self.indent_num}if {self.input_var}%10=={num}:")
        self.indent_num+=1
        for i in range(len(self.data)):
            if self.data[i] % 10==num:
                self.res_data.append(self.data[i])


    def res_quantity(self,data=list):#кол-во
        quan=0
        self.code.append(f"{self.indent*self.indent_num}{self.dop_var}+=1")
        for i in range(len(data)):
            quan+=1
        self.res_data=[quan]
        print(f"Result:{self.res_data[0]}")
        self.code.append(f"print({self.dop_var})")

    def res_sum(self,data=list):#сумма
        sum=0
        self.code.append(f"{self.indent*self.indent_num}{self.dop_var}+={self.input_var}")
        for i in range(len(data)):
            sum+=data[i]
        self.res_data=[sum]
        print(f"Result:{self.res_data[0]}")
        self.code.append(f"print({self.dop_var})")
    
solver=solveProblem(input(f"Введите тип задачи:"),input(f"Введите примечание:"),input(f"Введите тип:"))
        
win.closeWindow()