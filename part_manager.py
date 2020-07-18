import  tkinter as tk
import tkinter.font as tkFont
# create window object
app = tk.Tk()

# part
# adding the widget
part_text = tk.StringVar()
part_label = tk.Label(app, text='Part Name', font= ('arial', 14), pady = 20)
part_label.grid(row = 0, column = 0)
part_entry = tk.Entry(app, textvariable = part_text)
part_entry.grid(row = 0, column = 1)

# customer
customer_text = tk.StringVar()
customer_label = tk.Label(app, text='Customer', font= ('arial', 14), pady = 20)
customer_label.grid(row = 0, column = 2)
customer_entry = tk.Entry(app, textvariable = part_text)
customer_entry.grid(row = 0, column = 3)

#retailer
retailer_text = tk.StringVar()
retailer_label = tk.Label(app, text='Retailer', font= ('arial', 14), pady = 20)
retailer_label.grid(row = 1, column = 0, sticky = 'w')
retailer_entry = tk.Entry(app, textvariable = part_text)
retailer_entry.grid(row = 0, column = 1)


part_text = tk.StringVar()
part_label = tk.Label(app, text='Part Name', font= ('arial', 14), pady = 20)
part_label.grid(row = 0, column = 0)
part_entry = tk.Entry(app, textvariable = part_text)
part_entry.grid(row = 0, column = 1)


# window details
font = tkFont.Font(family = 'gothic142', size = 16)
tk.Text(app, height=10).configure(font = font)
app.title("Part Manager")
app.geometry('700x350')

# start program
app.mainloop()

