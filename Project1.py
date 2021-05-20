# coding=utf-8

# import libs
# import Project1_cmd
# import Project1_sty
import datetime

# import Fun
import Page1
import Page2
import tkinter as tk
from tkinter import filedialog
from tkinter import *
import tkinter.ttk
import tkinter.font
from PIL import Image, ImageTk

ElementBGArray = {}
ElementBGArray_Resize = {}
ElementBGArray_IM = {}


# Add your Varial Here: (Keep This Line of comments)
# Define UI Class
class Project1:
    def __init__(self, root, isTKroot=True):
        stu_answer = [] #全局变量：学生答案

        # 将上传文件按换行符切割，返回答案数组
        def read_file(file):
            answer = file.split('\n')
            return answer

        def upload_file():
            global stu_answer
            print(ComboBox_6.get())
            if ComboBox_6.get() == "文本":
                selectFile = filedialog.askopenfilename()  # askopenfilename 1次上传1个；askopenfilenames1次上传多个
                if selectFile is not None:
                    with open(file=selectFile, mode='r+', encoding='utf-8') as file:
                        stu_answer = read_file(file.read())
                        print(stu_answer)
                        i = datetime.datetime.now()
                        Text_4.insert("end", "%s/%s/%s %s:%s" % (i.year, i.month, i.day, i.hour, i.minute) + "   上传" +
                                      "%s" % (ComboBox_6.get()) + "成功\n")

            if ComboBox_6.get() == "批量图像":
                selectFiles = filedialog.askopenfilenames()  # askopenfilename 1次上传1个；askopenfilenames1次上传多个
                for File in selectFiles:
                    if File is not None:
                        with open(file=File, mode='r+', encoding='utf-8') as file:
                            file_text = file.read()
                            print(file_text)
                            i = datetime.datetime.now()
                            Text_4.insert("end",
                                          "%s/%s/%s %s:%s" % (i.year, i.month, i.day, i.hour, i.minute) + "   上传" +
                                          "%s" % (ComboBox_6.get()) + "成功\n")

        className = self.__class__.__name__
        # Fun.G_UIElementArray[className] = {}
        # Fun.G_ElementBindingDataArray[className] = {}
        global ElementBGArray
        global ElementBGArray_Resize
        global ElementBGArray_IM
        # Fun.AddElement(className, 'UIClass', self)
        self.root = root
        # style = Project1_sty.SetupStyle()
        if isTKroot == True:
            root.title("Form1")
            root.wm_attributes("-topmost", 1)
            root.geometry("1139x719")
        Form_1 = tkinter.Canvas(root, width=10, height=4)
        Form_1.place(x=0, y=0, width=1139, height=719)
        Form_1.configure(bg="#efefef")
        Form_1.configure(highlightthickness=0)
        ElementBGArray[1] = Image.open("379-1G2121JS4.jpg").convert('RGBA')
        ElementBGArray_Resize[1] = ElementBGArray[1].resize((1139, 719), Image.ANTIALIAS)
        ElementBGArray_IM[1] = ImageTk.PhotoImage(ElementBGArray_Resize[1])
        Form_1.create_image(0, 0, anchor=tkinter.NW, image=ElementBGArray_IM[1], tag="bgimg")
        # Fun.AddElement(className, 'root', root)
        # Fun.AddElement(className, 'Form_1', Form_1)
        # Create the elements of root
        Text_4 = tkinter.Text(root)
        Text_4.place(x=660, y=80, width=452, height=591)
        Text_4.configure(relief="sunken")
        # Fun.AddElement(className, 'Text_4', Text_4)

        Label_5 = tkinter.Label(root, text="上传学生答案", width=10, height=4)
        Label_5.place(x=50, y=50, width=120, height=20)
        Label_5_Ft = tkinter.font.Font(family='System', size=10, weight='bold', slant='roman', underline=0,
                                       overstrike=0)
        Label_5.configure(font=Label_5_Ft)
        # Fun.AddElement(className, 'Label_5', Label_5)
        # ComboBox_6_Variable = Fun.AddElementVariable(className, 'ComboBox_6')
        ComboBox_6 = tkinter.ttk.Combobox(root, state="readonly")
        ComboBox_6.place(x=50, y=90, width=100, height=30)
        ComboBox_6.configure(state="readonly")
        ComboBox_6["values"] = ['文本', '图像', '批量图像']
        ComboBox_6.current(0)
        # Fun.AddElement(className, 'ComboBox_6', ComboBox_6)
        Button_7 = tkinter.Button(root, text="选择文件", width=10, height=4, command=upload_file)
        Button_7.place(x=170, y=90, width=100, height=28)
        # Fun.AddElement(className, 'Button_7', Button_7)

        Label_8 = tkinter.Label(root, text="上传标准答案及评分细则", width=10, height=4)
        Label_8.place(x=50, y=150, width=170, height=20)
        Label_8_Ft = tkinter.font.Font(family='System', size=10, weight='bold', slant='roman', underline=0,
                                       overstrike=0)
        Label_8.configure(font=Label_8_Ft)
        # Fun.AddElement(className, 'Label_8', Label_8)
        Button_9 = tkinter.Button(root, text="选择文件", width=10, height=4)
        Button_9.place(x=50, y=190, width=100, height=28)
        # Fun.AddElement(className, 'Button_9', Button_9)
        Button_10 = tkinter.Button(root, text="执行评分", width=10, height=4)
        Button_10.place(x=130, y=250, width=240, height=80)
        Button_10_Ft = tkinter.font.Font(family='System', size=30, weight='bold', slant='roman', underline=0,
                                         overstrike=0)
        Button_10.configure(font=Button_10_Ft)
        # Fun.AddElement(className, 'Button_10', Button_10)
        NoteBook_11 = tkinter.ttk.Notebook(root, cursor="spider")
        NoteBook_11.place(x=50, y=370, width=540, height=330)
        PageFrame_1 = tkinter.ttk.Frame(NoteBook_11)
        PageFrame_1.place(x=55, y=395, width=530, height=300)
        Page1.Page1(PageFrame_1, False)
        NoteBook_11.add(PageFrame_1, text="标准答案")
        PageFrame_2 = tkinter.ttk.Frame(NoteBook_11)
        PageFrame_2.place(x=55, y=395, width=530, height=300)
        Page2.Page2(PageFrame_2, False)
        NoteBook_11.add(PageFrame_2, text="学生答案")
        # Fun.AddElement(className, 'NoteBook_11', NoteBook_11)
        Label_12 = tkinter.Label(root, text="日志", width=10, height=4)
        Label_12.place(x=660, y=50, width=100, height=20)
        Label_12_Ft = tkinter.font.Font(family='System', size=10, weight='bold', slant='roman', underline=0,
                                        overstrike=0)
        Label_12.configure(font=Label_12_Ft)
        # Fun.AddElement(className, 'Label_12', Label_12)
        # Inital all element's Data
        # Fun.InitElementData(className)
        # Add Some Logic Code Here: (Keep This Line of comments)


# Create the root of Kinter
if __name__ == '__main__':
    root = tkinter.Tk()
    MyDlg = Project1(root)
    root.mainloop()
