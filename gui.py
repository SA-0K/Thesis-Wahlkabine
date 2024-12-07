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

sample_table ={'GUIDELINES FOR IEC 61499 DEVELOPMENT IN ECLIPSE 4DIAC IDE\n': 73.03423854604085, 'C++FUNCTIONBLOCKVERIFIERLITCyber-Physical SystemsLab\n': 73.03423854604085, 'TEXTUAL DELTA MODEL INFRASTRUCTURE FOR EXPRESSING CONTROL SOFTWARE VARIABILITY\n': 73.03423854604085, 'VISUALISATION OF OPC UA INFORMATION MODEL\n': 73.03423854604085, 'INFORMATION TRACEABILITY BETWEEN VARIABILITY ARTIFACTS AND THEIR RELATED VARIANTS\n': 73.44385610791416, '“THESIS-WAHLKABINE”: DEVELOPING AN ONLINE WEB-BASED PLATFORM FOR MATCHING STUDENTS TO THESIS TOPICS\n': 73.71566997592845, 'BRINGING THE DESIGN OF FEEDBACK CONTROL LAWS RIGHT INTO THE DISTRIBUTED CONTROL SOFTWARE\n': 73.71566997592845, 'DEVELOPING AN EXTRACTOR FOR MINING VARIABILITY FROM PRODUCT VARIANTS\n': 73.85120175054702, 'ENSURING DATA QUALITY IN PRODUCTION SYSTEMS\n': 73.98648525237566}

root = tk.Tk()
root.title("Theses matching")
root.geometry("520x520")

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

def change():
    global n
    label.config(text=question)

    #n=  0 if (n==len(questions)-1) else n+1
    
    
def forward_button():
    global question, value,base
    for v,q in base.items():
        val=(current_slider_value.get())
        assign_values(base,val)
        draw_table(generate_new_dict())
        base=generate_questions(1)
    for v,q in base.items():
        question=q
        value=v
    change()
    
    #label.config(text=curr_q)

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

bf=tk.Button(root, text="Next",width=15,command=forward_button)
bf.pack(side="right",padx=25,pady=10,anchor="n")#.place(x=25,y=130)
bb=tk.Button(root, text="Previous",width=15)
bb.pack(side="left",padx=25,pady=10,anchor="n")#.place(x=325,y=130)

draw_table(sample_table)


root.mainloop()









"""
radio_buttons=[]


for i in range(0,11):

    radio_buttons.append(tk.Radiobutton(root, text=f"{i}",value=i).place(x=i*40+15,y=150))
"""