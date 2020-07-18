import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkFont
from db import Database

db = Database('store.db')

# fetching the data

def populate_list():
    parts_list.delete(0, tk.END)
    print('list deleted')
    for row in db.fetch():
        print(row)
        parts_list.insert(tk.END, row)

def add_item():
    if part_text.get() == '' or customer_text.get() == '' or retailer_text.get() == '' or price_text.get() == '':
        messagebox.showerror("Required Fields", "Please include all fields")
    db.insert(part_text.get(), customer_text.get(), retailer_text.get(), price_text.get())
    parts_list.delete(0, tk.END)
    parts_list.insert(tk.END, (part_text.get(), customer_text.get(), retailer_text.get(), price_text.get()))
    populate_list()

def remove_item():
    print("remove")

def update_item():
    print("update")

def clear_item():
    print("clear")



# create window object
app = tk.Tk()

# the GUI
# adding the widget
# ------------------Input boxes-------------------
# part
part_text = tk.StringVar()
part_label = tk.Label(app, text='Part Name', pady=20, padx=20)
part_label.grid(row=0, column=0, )
part_entry = tk.Entry(app, textvariable=part_text)
part_entry.grid(row=0, column=1)

# customer
customer_text = tk.StringVar()
customer_label = tk.Label(app, text="Customer Name")
customer_label.grid(row=0, column=2)
customer_entry = tk.Entry(app, textvariable=customer_text)
customer_entry.grid(row=0, column=3)

# Retailer
retailer_text = tk.StringVar()
retailer_label = tk.Label(app, text='Retailer ', pady=20, padx=20)
retailer_label.grid(row=1, column=0, )
retailer_entry = tk.Entry(app, textvariable=retailer_text)
retailer_entry.grid(row=1, column=1)

# Pricing
price_text = tk.StringVar()
price_label = tk.Label(app, text="Price")
price_label.grid(row=1, column=2)
price_entry = tk.Entry(app, textvariable=price_text)
price_entry.grid(row=1, column=3)

# parts list
parts_list = tk.Listbox(app, height=8, width=50, border=0)
parts_list.grid(row=3, column=0, columnspan=3, rowspan=6, pady=20, padx=20)

# scrollbar

scrollbar = tk.Scrollbar(app)
# since the list expands from 0 - 2, placing the scrollbar at 3
scrollbar.grid(row=3, column=3)
# set scroll to listbox
parts_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=parts_list.yview)


# buttons
# 4 different button add, remove, update, clear
# addbutton


add_btn = tk.Button(app, text="Add Part", width=12, command=add_item)
add_btn.grid(row = 2, column = 0, pady= 20)

# remove
remove_btn = tk.Button(app, text="Remove Part", width=12, command=remove_item)
remove_btn.grid(row = 2, column = 1, pady= 20)

# update button
update_btn = tk.Button(app, text="Update Part", width=12, command=update_item)
update_btn.grid(row = 2, column = 2, pady= 20)

# clear button
clear_btn = tk.Button(app, text="Clear Part", width=12, command=clear_item)
clear_btn.grid(row = 2, column = 3, pady= 20)

# window details
font = tkFont.Font(family='gothic142', size=16)
tk.Text(app, height=10).configure(font=font)
app.title("Part Manager")
app.geometry('700x350')

# populate data
populate_list()

# start program
app.mainloop()
