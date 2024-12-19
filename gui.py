"""
Graphical user interface
@author Oleksandr Kudriavchenko

Copyright 2024 Johannes Kepler University Linz
LIT Cyber-Physical Systems Lab
All rights reserved
"""

import tkinter as tk
from tkinter import ttk
from time import sleep
from main import *


questions =[
"How familiar are you with the concepts of external plugins (0-10)?",
"How experienced are you with Variability Mining (0-10)?",
"How interested are you in formal methods?",
"How proficient are you with Threshold Analysis (0-10)?"
]
updating_key=''

sample_table ={'GUIDELINES FOR IEC 61499 DEVELOPMENT IN ECLIPSE 4DIAC IDE\n': 73.03423854604085, 'C++FUNCTIONBLOCKVERIFIERLITCyber-Physical SystemsLab\n': 73.03423854604085, 'TEXTUAL DELTA MODEL INFRASTRUCTURE FOR EXPRESSING CONTROL SOFTWARE VARIABILITY\n': 73.03423854604085, 'VISUALISATION OF OPC UA INFORMATION MODEL\n': 73.03423854604085, 'INFORMATION TRACEABILITY BETWEEN VARIABILITY ARTIFACTS AND THEIR RELATED VARIANTS\n': 73.44385610791416, '“THESIS-WAHLKABINE”: DEVELOPING AN ONLINE WEB-BASED PLATFORM FOR MATCHING STUDENTS TO THESIS TOPICS\n': 73.71566997592845, 'BRINGING THE DESIGN OF FEEDBACK CONTROL LAWS RIGHT INTO THE DISTRIBUTED CONTROL SOFTWARE\n': 73.71566997592845, 'DEVELOPING AN EXTRACTOR FOR MINING VARIABILITY FROM PRODUCT VARIANTS\n': 73.85120175054702, 'ENSURING DATA QUALITY IN PRODUCTION SYSTEMS\n': 73.98648525237566}

root = tk.Tk()
root.title("Theses matching")
root.geometry("557x520")

n=0

global value,question,base
question=""
value =""
base=generate_questions(1)


for v,q in base.items():
    value = v
    question =q

    label = tk.Label(root, text=question)

label.pack(pady=30)

"""
zero_label = tk.Label(root,text="0").pack(side="left", pady=0,padx=(55,0), anchor="n")
ten_label = tk.Label(root,text="10").pack(side="right",pady=0,padx=(0,55), anchor="n")
"""
def draw_table(table):
    # define columns
    columns = ("№",'topic_name')

    tree = ttk.Treeview(root, columns=columns, show='headings')

    # define headings
    tree.heading('topic_name', text='Topic')
    tree.heading('№', text='№')

    tree.column("№",width=50)
    tree.column("topic_name",width=480)

    n=1
    for name,dist in table.items():
        tree.insert('', tk.END,values=(n,name))
        n+=1


    def item_selected(event):
        for selected_item in tree.selection():
            item = tree.item(selected_item)
            record = item['values']
            # show a message
            print(record)
            #showinfo(title='Information', message=','.join(record))
    tree.bind('<<TreeviewSelect>>', item_selected)

    tree.place(x=15,y=200)#.grid(row=0, column=0, sticky='nsew')
    

current_slider_value=tk.DoubleVar()
current_slider_value2=tk.DoubleVar()

def change():
    global n
    label.config(text=question)

    #n=  0 if (n==len(questions)-1) else n+1
    
def update_values():
    global chose_val
    assign_values(updating_key,current_slider_value2.get())
    chose_val.destroy()

def forward_button():
    global question, value,base
    for v,q in base.items():
        val=(current_slider_value.get())
        assign_values(v,val)
        draw_table(generate_new_dict())
        base=generate_questions(1)
    for v,q in base.items():
        question=q
        value=v
    change()
    
    #label.config(text=curr_q)


def edit():
    
    history=show_history(user_interests,already_been_asked)
    
    edit_window=tk.Toplevel(root)
    edit_window.geometry('400x400')
    
    edit_window.title("Edit choices :)")

    columns = ("keyword","value")

    tree = ttk.Treeview(edit_window, columns=columns, show='headings')

    # define headings
    tree.heading('keyword', text='Keyword')
    tree.heading('value', text='Value')

    tree.column("value",width=50)
    tree.column("keyword",width=350)

    
    for key,value in history.items():
        tree.insert('', tk.END,values=(key,round(value,1)))
        
    def item_selected(event):
        global updating_key,chose_val
        for selected_item in tree.selection():
            item = tree.item(selected_item)
            record = item['values']
            updating_key=record[0]
            # show a message
            
            chose_val=tk.Toplevel(root)
            chose_val.geometry('350x200')
            #edit_window.grab_release()
            #chose_val.grab_set()
            chose_val.title("Choose new value  :)")
            #print(record)
            l=tk.Label(chose_val,text=record[0]).pack()
            bf1=tk.Button(root, text="Ok",width=50)
            slider2 = ttk.Scale(
                chose_val,
                from_=0,
                to= 10,
                length=300,
                orient='horizontal', 
                command=slider_changed,
                variable=current_slider_value2
            )
            slider2.set(record[-1])
            slider2.pack(pady=10)
            chose_val.protocol("WM_DELETE_WINDOW",update_values)
            
            #showinfo(title='Information', message=','.join(record))
    tree.bind('<<TreeviewSelect>>', item_selected)


    tree.place(x=0,y=0)



def slider_changed(event):
    #draw_table(sample_table)
    pass

slider = ttk.Scale(
    root,
    from_=0,
    to= 10,
    length=400,
    orient='horizontal', 
    command=slider_changed,
    variable=current_slider_value
)
slider.set(5)
slider.pack(pady=10)

bf=tk.Button(root, text="Next",width=50,command=forward_button)
bf.pack(side="right",pady=10,padx=(0,25), anchor="n")#.place(x=25,y=130)
bb=tk.Button(root, text="Edit",width=10,command=edit)
bb.pack(side="left",pady=10,padx=(25,0), anchor="n")#.place(x=325,y=130)

draw_table(sample_table)


root.mainloop()









"""
radio_buttons=[]


for i in range(0,11):

    radio_buttons.append(tk.Radiobutton(root, text=f"{i}",value=i).place(x=i*40+15,y=150))
"""