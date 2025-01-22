
import tkinter as tk
from tkinter import ttk
import main


root = tk.Tk()
root.title("Edit requirements")
root.geometry("560x300")
edit_slider_value=tk.DoubleVar()
present=tk.IntVar()

"""
Some methods from main are reused and user 
interest should be 10 for all topics instead 
of 5 so topics are not hidden from supervisor 
"""
for key in main.database_manager.get_all_keywords():
    main.user_interests[key] = 10

global current_topic_name
current_topic_name = ""
updating_key='' # variable for storing keyword that is being edited


def close_edit():
    """Closes the edit window when OK or X is pressed"""
    global edit_window
    edit_window.destroy()

def edit_changed(event=None):
    
    new_value=0
 
    if present.get()!=0:
        new_value=edit_slider_value.get()+present.get()
    main.database_manager.change_requirment(current_topic_name,updating_key,new_value)

    name_vector_array=main.database_manager.get_name_vector()
    vector={}

    for nmv in name_vector_array:
        if nmv['name']==current_topic_name:
            vector=nmv['vector']
    draw_history_table(history_window,vector)



def edit(record):
    """
    Generates an edit window, gets the record that is going to be edited
    """
    global edit_window
    edit_window=tk.Toplevel(root)
    edit_window.geometry('350x200')
    edit_window.title("Choose new value :)")
    l=tk.Label(edit_window,text=record[0]).pack()
    checkbox = tk.Checkbutton(edit_window,
                              text="Present in the topic",
                              onvalue=10,
                              offvalue=0,
                              variable=present,
                              command=edit_changed)
    checkbox.flash()
    checkbox.pack()
    
    edit_slider = ttk.Scale(
        edit_window,
        from_=0,
        to= 10,
        length=300,
        orient='horizontal', 
        command=edit_changed,
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

def show_history(vector):
    """
    Generates a gistory window
    """
    global history_window
    
    
    history_window=tk.Toplevel(root)
    history_window.geometry('400x400')
    
    history_window.title("Keywords")
    draw_history_table(history_window,vector)




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
        global current_topic_name
        for selected_item in tree.selection():
            item = tree.item(selected_item)
            record = item['values'][-1]
            
            name_vector_array=main.database_manager.get_name_vector()
            
            for nmv in name_vector_array:
                if nmv['name']==record:
                    current_topic_name=record
                    vector=nmv['vector']
                    show_history(vector)
            # topic selection action
            # for example opening a pdf
    tree.bind('<<TreeviewSelect>>', item_selected)

    tree.place(x=15,y=20)
    

draw_topics_table(main.generate_new_topic_list())
root.mainloop()