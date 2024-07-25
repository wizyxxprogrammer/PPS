from colorama import*
from keyboard import*
class Window():
    def __init__(self):
        self.message="Press enter to close window."
        self.foreColor=Fore.WHITE
        self.backColor=Back.BLACK
        self.StyleMode=Style.NORMAL
        self.fore=[Fore.BLACK,Fore.RED,Fore.GREEN,Fore.YELLOW,Fore.BLUE,Fore.MAGENTA,Fore.CYAN,Fore.WHITE]
        self.back=[Back.BLACK,Back.RED,Back.GREEN,Back.YELLOW,Back.BLUE,Back.MAGENTA,Back.CYAN,Back.WHITE]
        self.style=[Style.DIM,Style.NORMAL,Style.BRIGHT]
        self.closeKey="enter"
        self.errors=["Error."]
    def closeWindow(self):
        print(self.message,end="")
        print("")
        wait(self.closeKey)
        exit()
    def error(self,numberError):
        print(self.errors[numberError])
        self.closeWindow()
    def coloredText(self,text):
        if self.foreColor in self.fore and self.backColor in self.back and self.StyleMode in self.style:
           return self.foreColor+self.backColor+self.StyleMode+text
        else:
            self.closeWindow()
    def setForeColor(self,color_num=int):
        if color_num<=7 and color_num>=0:
            self.foreColor=self.fore[color_num]
        else:
            self.closeWindow()
    def setBackColor(self,color_num=int):
        if color_num<=7 and color_num>=0:
            self.backColor=self.back[color_num]
        else:
            self.closeWindow()
    def setStyle(self,mode_num=int):
        if mode_num>=0 and mode_num<=2:
            self.StyleMode=self.style[mode_num]
        else:
            self.closeWindow()
    def createTable(self,head=list,data=list):
        columns=len(head)
        coof=0.5
        lenghtData=[]
        for i in range(len(data)):
            lenghtData.append(len(data[i]))
        maxLenghtData=max(lenghtData)
        if maxLenghtData==1:
            coof=2
        coof=maxLenghtData
        if len(data)%columns==0:
            for i in range(columns):
                print(" "*(maxLenghtData-1)*coof,head[i],end=" "*(maxLenghtData-1)*coof)
            print("")
            print(end="|")
            for i in range(len(data)):
                if i%columns==0 and i!=0:
                    print("")
                    print("|",end="")
                print(" "*(maxLenghtData-1)*coof,data[i]," "*(maxLenghtData-1)*coof,end="|")
    def func_by_key(self,func,key=str):
        wait(key)
        func()