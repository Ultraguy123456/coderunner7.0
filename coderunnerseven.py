#imports
from tkinter import *
from tkinter.filedialog import *
from tkinter import simpledialog
from tkinter import messagebox
from tkinter.colorchooser import askcolor
import os
from tkinter.font import *
#window
a = Tk()
a.geometry('666x776')
a.title('Code runner v7.0')
a.configure(bg='black')
c = Frame(a, cursor='dotbox white black')
c.pack(side='top', expand=True, fill='both')
c.config(bg='Black')
l1 = Label(a)
#clear frame function
def clear():
    for i in c.winfo_children():
        i.destroy()
#coding screen fuction
def Codingsc():
    global yes_or_no
    global t1,l1

    clear()
    t1 = Text(c, cursor='dotbox white black',height=450,width=500)
    t1.pack()

#executing function
def execute():
    try:
        exec(t1.get(0.0, END))
        messagebox.showinfo("Action", "Code sucsessfully executed...")
    except:
        messagebox.showerror("Error!","Error found in code")
#2nd page help fuction
def help_sc():
    clear()
    l2 = Label(
        c,
        text=
        "Deleting\nTo delete a file, click the \"File Options\"\n After, click \
the Delete a file option.\nEnter the location like the example, if you do \
not remember then \
scroll along the shell and find the file path.\
\nType the file name without the \".txt\". \nWhen the file has been \
sucsessfully deleted you should find the file name and was \
deleted.\nIDLE Version ©",
        bg='White',fg='Black')
    l2.pack()
    b1 = Button(c, text='◀', command=Helpsc)
    b1.pack()
#1st page help sunction
def Helpsc():
    global l1
    clear()
    l1 = Label(
        c,
        text=
        'Help\n This is The 6th version of the code runner made by \
Superguy123456 and can run python code.\nWhen you click the Coding dropdown \
find the Coding page, after  \
find \
the editor. Simply type in the code.\nOpening\nTo open \
a saved file you must click the "File Options" \
.\nAfter,select the file name\n For it to work you must \
keep the Coding Page open.\nSaving\nTo save a file\
you must click "File Options" and select "save file".\nOnce \
that is is done, name your file.\nIn addition, keep the Coding page \
open while doing so.\nIf you close the Coding Page without saving the \
code will be lost. \nIf saved correctly, then the location and file name \
should appear (this will help with deleting\
).\
\nExecution\nTo execute code that has been written you must click \
the Coding dropdown and then Execute tab above.\nErrors\nIf any error comes \
and shows a line of code you never wrote down then that is not to be worried \
about,\n \
under that however you should see the error you did\
.',
        bg='White',fg='Black')
    b1 = Button(c, text='▶', command=help_sc)
    l1.pack()
    b1.pack()
#file deleting function

def delete():
    file_loc = simpledialog.askstring("File Path","What is the file location\
\n (If you do not know then check the shell \
for the file path and take the file name out...)\n\
Ex:/Users/Name/Desktop")
    location=file_loc
    file_ident = simpledialog.askstring(
        "Delete file",
        "What file would you like to delete?\n Do add tag...",
        parent=c)
    if file_ident is not None:
        try:
            file = file_ident
            path = os.path.join(location, file)
            os.remove(path)
            messager = file + ' is sucsessfully deleted...'
            messagebox.showinfo("Action", messager)
            print(file,' was deleted')
        except:
            messagebox.showerror("Error!","No such file...")
#file opening function
def open_file():
    file = askopenfile(mode='r', filetypes=[('Python Files', '*.py')])
    try:
        if file is not None:
            content = file.read()
            messagebox.showinfo("Action", "File opened...")
        t1.delete(1.0, END)
        t1.insert(1.0, content)
    except:
        messagebox.showerror("Error!","File Opening had a problem...")
#file saving function
def save():
    global yes_or_no

    saver = asksaveasfilename(initialfile='change_to_txt_if_needed.py',
                                  defaultextension=".py",
                                  filetypes=[("All Files", "*.*"),
                                             ("Text Documents", "*.py")])
    
    
    if saver == "":
        saver = None
    else:
        try:
            print(saver)
            file = open(saver, 'w')
            file.write(t1.get(0.0, END))
            a.title(os.path.basename(saver))
            messagebox.showinfo("Action", "File saved...")
        except:
            messagebox.showerror("Error!","File Saving had a problem...")
        finally:
            file.close()
def Shell():
    while(1):
        shellinput=simpledialog.askstring("Shell v1","Please enter you code:")
        if shellinput is not None:
            try:
                exec(shellinput)
            except:
                messagebox.showerror("Error","The line that you have entered is\
 incorrect...")
        else:
            break
def choose():
  colors = askcolor(title="Customize Background Color")
  c.config(bg=colors[1])
def mwindow():
    import mwindow
    mwindow.newsc()
def Opers():
    messagebox.showinfo("Python Info: Operators","Here are most operators that\
 are used in if functions:\n < , > , == , != , <= , >= , && ,is , not , and.\n\
All of these are commonly used.\nDo not use these for 'else' statments, for \
the do not exept operators")
def Escapechar():
    messagebox.showinfo("Python Info: Escape Characters","Escape characters \
look like this: \ . These are used to cut strings so they can be read.\n\
 Another purpose for the characters is for keyboard commands like:\
 \\n. This makes a new line.\nAnother way to use this is \\t which makes a \
 \n'tab' space. \nIn fact, this text is written with escape characters!")
def Mathopers():
    messagebox.showinfo("Python Info: Math operators","Math Operators are used \
for the exact purpose of their name: do math. They can \nbe used in basicly all\
python code. Examples are: + , - , * , / , ** , // , =- , =+ , %.\n + is addition, \
- is subtraction, * is multiplication, / is division, \n\
** is exponential, // is floor division, =- is for variable expressions \n\
like x=x-1 to make is shorter to: x=-1, =+ is the same as =- but for \n\
addition, and % is modulus.")
def tkinterinfo():
    messagebox.showinfo("Python Info: Tkinter","Tkinter is a module that is \
avalible to all people who have Python on their computor. \nThe python IDLE you are\
 using might even be made by tkinter!\n This Coderunner is coded in tkinter!\
It comes with objects called widgets. Some widgets are: Buttons, Textboxes, Labels,\
Menus, Spinboxes, Dropdowns, Radiobuttons,\n Entries. All of these make it an \
exelent GUI toolkit.")
Codingsc()
#menus
menubar = Menu(a)

Coding = Menu(menubar, tearoff=0)
Help = Menu(menubar, tearoff=0)
filer=Menu(menubar,tearoff=0)
Codinginfo=Menu(menubar,tearoff=0)
Window=Menu(menubar,tearoff=0)
Codinginfo.add_command(label='Operators',command=Opers)
Codinginfo.add_command(label='Escape Characters',command=Escapechar)
Codinginfo.add_command(label='Math operators',command=Mathopers)
Codinginfo.add_command(label='Tkinter',command=tkinterinfo)
Coding.add_command(label='Coding Page', command=Codingsc)
Coding.add_command(label='Execute', command=execute)
Coding.add_command(label='Shell',command=Shell)
Window.add_command(label='New Window',command=mwindow)
Window.add_command(label='Change Color',command=choose)

Help.add_command(label='Help Page', command=Helpsc)
filer.add_command(label='Save File',command=save)
filer.add_command(label='Open File',command=open_file)
filer.add_command(label='Delete a File',command=delete)

menubar.add_cascade(label='Help', menu=Help)
menubar.add_cascade(label='Coding', menu=Coding)
menubar.add_cascade(label='Coding Info',menu=Codinginfo)
menubar.add_cascade(label='File Options',menu=filer)
menubar.add_cascade(label='Window',menu=Window)
a.config(menu=menubar)
a.mainloop()
