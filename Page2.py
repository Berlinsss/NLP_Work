#coding=utf-8

#import libs 
# import Page2_cmd
# import Page2_sty
# import Fun
import os
import tkinter
from   tkinter import *
import tkinter.ttk
import tkinter.font
ElementBGArray={}  
ElementBGArray_Resize={} 
ElementBGArray_IM={} 

#Add your Varial Here: (Keep This Line of comments)
#Define UI Class
class  Page2:
    def __init__(self,root,isTKroot = True):
        className = self.__class__.__name__
        # Fun.G_UIElementArray[className]={}
        # Fun.G_ElementBindingDataArray[className]={}
        global ElementBGArray
        global ElementBGArray_Resize
        global ElementBGArray_IM
        # Fun.AddElement(className,'UIClass',self)
        self.root = root
        # style = Page2_sty.SetupStyle()
        if isTKroot == True:
            root.title("Form1")
            root.wm_attributes("-topmost",1)
            root.geometry("540x300")
        Form_1= tkinter.Canvas(root,width = 10,height = 4)
        Form_1.place(x = 0,y = 0,width = 540,height = 300)
        Form_1.configure(bg = "#efefef")
        Form_1.configure(highlightthickness = 0)
        # Fun.AddElement(className,'root',root)
        # Fun.AddElement(className,'Form_1',Form_1)
        #Create the elements of root 
        TreeView_2= tkinter.ttk.Treeview(root,show="tree")
        TreeView_2.place(x = 10,y = 10,width = 520,height = 280)
        TreeView_2.configure(show = "headings")
        TreeView_2.configure(selectmode = "extended")
        TreeView_2.configure(columns = ["答案","得分"])
        TreeView_2.column("答案",anchor="center",width=370)
        TreeView_2.heading("答案",text="答案")
        TreeView_2.column("得分",anchor="center",width=70)
        TreeView_2.heading("得分",text="得分")
        # Fun.AddElement(className,'TreeView_2',TreeView_2)
        #Inital all element's Data 
        # Fun.InitElementData(className)
        #Add Some Logic Code Here: (Keep This Line of comments)
        path = 'result_stu_answer.txt'
        if os.path.exists(path):
            with open(file=path, mode='r+', encoding='utf-8') as file:
                data = file.read()
                data_list = data.split('\n')
                data_lists = [[]]

            for i in range(0, len(data_list)):
                data_lists.append(data_list[i].split('\t'))

            del data_lists[0]

            i = 0
            for v in data_lists:
                TreeView_2.insert('', i, values=(v[0], v[1]))
                i += 1


#Create the root of Kinter 
if  __name__ == '__main__':
    root = tkinter.Tk()
    MyDlg = Page2(root)
    root.mainloop()
