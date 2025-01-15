"""
Graphical user interface
@author Oleksandr Kudriavchenko

Copyright 2024 Johannes Kepler University Linz
LIT Cyber-Physical Systems Lab
All rights reserved
"""

import tkinter as tk
from tkinter import ttk
import main

main.init()

updating_key='' # variable for storing keyword (user choice) that is being edited

# init the main window
root = tk.Tk()
root.title("Theses matching")
root.geometry("557x520")



# first question placement
global value,question,base
question = ""
value = ""
base=main.generate_questions(1)

# tkinter variables for sliders
main_slider_value=tk.DoubleVar()
edit_slider_value=tk.DoubleVar()

for v,q in base.items():
    value = v
    question =q
    label = tk.Label(root, text=question)
label.pack(pady=30)



def draw_topics_table(table):
    """
    Draws the table with topics in main window
    """

    # define columns
    columns = ("№",'topic_name')

    tree = ttk.Treeview(root, columns=columns, show='headings')

    # define headings
    tree.heading('topic_name', text='Topic')
    tree.heading('№', text='№')

    tree.column("№",width=50)
    tree.column("topic_name",width=480)

    n=1
    for name in table:
        tree.insert('', tk.END,values=(n,name))
        n+=1


    def item_selected(event):
        for selected_item in tree.selection():
            item = tree.item(selected_item)
            record = item['values']
            # topic selection action
            # for example opening a pdf
    tree.bind('<<TreeviewSelect>>', item_selected)

    tree.place(x=15,y=200)
    


def close_edit():
    """Closes the edit window when OK or X is pressed"""
    global edit_window
    edit_window.destroy()
    
def update_values():
    """Updates all values and tables"""
    global edit_window, history_window
    main.assign_values(updating_key,edit_slider_value.get())
    draw_topics_table(main.generate_new_topic_list())
    draw_history_table(history_window,main.generate_history())


def forward_button():
    """
    Shows the next question and updates the main table
    """
    global question, value,base
    for v,q in base.items():
        val=(main_slider_value.get())
        main.assign_values(v,val)
        draw_topics_table(main.generate_new_topic_list())
        base=main.generate_questions(1)
    for v,q in base.items():
        question=q
        value=v
    label.config(text=question)

def edit_slider_changed(event):
    """
    Calls update when edit slider changes
    """
    update_values()
    
def edit(record):
    """
    Generates an edit window, gets the record that is going to be edited
    """
    global edit_window
    edit_window=tk.Toplevel(root)
    edit_window.geometry('350x200')
    edit_window.title("Choose new value :)")
    l=tk.Label(edit_window,text=record[0]).pack()
    edit_slider = ttk.Scale(
        edit_window,
        from_=0,
        to= 10,
        length=300,
        orient='horizontal', 
        command=edit_slider_changed,
        variable=edit_slider_value
    )
    edit_slider.set(record[-1])
    edit_slider.pack(pady=10)
    bf1=tk.Button(edit_window, text="Ok",width=50,command=close_edit).pack()
    edit_window.protocol("WM_DELETE_WINDOW",close_edit)
            


def draw_history_table(window, history):
    """
    Draws a table in history window    
    """
    columns = ("keyword","value")
    tree = ttk.Treeview(window, columns=columns, show='headings')

    # define headings
    tree.heading('keyword', text='Keyword')
    tree.heading('value', text='Value')

    tree.column("value",width=50)
    tree.column("keyword",width=350)




    
    for key,value in history.items():
        tree.insert('', tk.END,values=(key,round(value,1)))

    def item_selected(event):
        global updating_key,edit_window
        for selected_item in tree.selection():
            item = tree.item(selected_item)
            record = item['values']
            updating_key=record[0]
            # show a message
            edit(record)
            
            #showinfo(title='Information', message=','.join(record))
    tree.bind('<<TreeviewSelect>>', item_selected)
    tree.place(x=0,y=0)

def show_history():
    """
    Generates a gistory window
    """
    global history_window
    history=main.generate_history()
    
    history_window=tk.Toplevel(root)
    history_window.geometry('400x400')
    
    history_window.title("History")
    draw_history_table(history_window,history)






slider = ttk.Scale(
    root,
    from_=0,
    to= 10,
    length=400,
    orient='horizontal', 
    variable=main_slider_value
)
slider.set(5)
slider.pack(pady=10)

bf=tk.Button(root, text="Next",width=50,command=forward_button)
bf.pack(side="right",pady=10,padx=(0,25), anchor="n")
bb=tk.Button(root, text="History",width=10,command=show_history)
bb.pack(side="left",pady=10,padx=(25,0), anchor="n")

draw_topics_table(main.generate_new_topic_list()) # Draws a table when the app started

def main_window():
    root.mainloop()

if __name__=="__main__":
    main_window()

