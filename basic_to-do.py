import tkinter
from tkinter import *
import sys
import random
from tkinter import messagebox


root=Tk()
root.title("To-Do")                 #Title of Root Window
root.geometry("300x250+300+300")
root.resizable(True,True)
root.config(bg="light pink")
#Empty list for some operations like asc_order and desc_order,remove,num_of_tasks etc.As these operatios on Listbox is not applicable.
task_list=[]
s= StringVar()

def update_mylist():
    clear_task()
    for task in task_list:
        mylist.insert("end",task)

def add_task():
    task=entry.get()
    task_list.append(task)
    update_mylist()
    s.set("")

def clear_task():
    mylist.delete(0,END)

def remove():
    task = mylist.get("active")
    try:
        if task in task_list:
            task_list.remove(task)
            update_mylist()
    except:
        random_choose_lable.config(text="There is no task pending")

def asc_order():
    task_list.sort()
    update_mylist()

def desc_sort():
    task_list.sort()
    task_list.reverse()
    update_mylist()

def choose_random():
   random.shuffle(task_list)
   random_task=task_list[0]
   random_choose_lable.config(text=random_task)

def num_of_task():
    j=0                                 #OR--->>To calculate number of tasks just check len(task_list)
    for i in task_list:
        j=j+1
    random_choose_lable.config(text=j)

def exit():
    result=messagebox.askyesno("ALERT","do you want to exit")
    if result==TRUE:
        sys.exit()
    else:
        pass
random_choose_lable=Label(root,text="",bg="lightskyblue")
random_choose_lable.grid(row=3,column=3)

# label=Label(root,text="To-Do List")
# label.grid(row=0,column=0)

add_item_button=Button(root,text="Add to-do item",width=18,command=add_task,bg="light blue")
add_item_button.grid(row=1,column=0)

clr_task_button=Button(root,text="Clear all tasks",width=18,command=clear_task,bg="light blue")
clr_task_button.grid(row=2,column=0)

remove_button=Button(root,text="Remove",width=18,command=remove,bg="light blue")
remove_button.grid(row=3,column=0)

asc_sort_button=Button(root,text="Ascending sort",width=18,command=asc_order,bg="light blue")
asc_sort_button.grid(row=4,column=0)

sort_desc_button=Button(root,text="Sort(DESC)",width=18,command=desc_sort,bg="light blue")
sort_desc_button.grid(row=5,column=0)

choose_random_button=Button(root,text="Choose Random",width=18,command=choose_random,bg="light blue")
choose_random_button.grid(row=6,column=0)

number_of_tasks_button=Button(root,text="Number of Tasks",width=18,command=num_of_task,bg="light blue")
number_of_tasks_button.grid(row=7,column=0)


#Instructions for exit function

exit_button=Button(root,text="Exit",width=10,command=exit,bg="red")  #For Exit above defined exit function is not needed here sys module invokes the exit function with only command=exit or "exit"
exit_button.grid(row=8,column=0)


entry=Entry(root,textvariable=s)
entry.grid(row=1,column=1)

mylist=Listbox(root)
mylist.grid(row=2,column=1,rowspan=7)

root.mainloop()