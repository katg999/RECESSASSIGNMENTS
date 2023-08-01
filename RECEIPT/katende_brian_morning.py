
from tkinter import *
import random
from tkinter import messagebox

root = Tk()
root.title('Test')
root.geometry('1270x685')
bg_color = "#4D0039"

c_name = StringVar()
c_phone = StringVar()
billno = StringVar()
item = StringVar()
Rate = IntVar()
Quantity = IntVar()
x = random.randint(1000, 9999)
billno.set(str(x))

# Create a BooleanVar to keep track of whether items have been added
has_items = BooleanVar()
has_items.set(False)

global l
l = []

def additm():
    item_value = item.get()
    rate_value = Rate.get()
    quantity_value = Quantity.get()

    if item_value == '' or rate_value == 0 or quantity_value == 0:
        messagebox.showerror('Error', 'Please enter valid item details')
    else:
        total_price = rate_value * quantity_value
        l.append(f"{item_value}\t\t{quantity_value}\t\t{total_price}")
        textarea.insert(END, f"{item_value}\t\t{quantity_value}\t\t{total_price}\n")
        has_items.set(True)

def welcome():
    textarea.delete(1.0, END)
    textarea.insert(END, "\t Welcome Shivan ")
    textarea.insert(END, f"\n\nBill Number  :\t\t{billno.get()}   ")
    textarea.insert(END, f'\n Customer Name:\t\t{c_name.get()} ")"')
    textarea.insert(END, f'\n Phone Number:\t\t{c_phone.get()} ")"')
    textarea.insert(END, f"\n===========================================================")
    textarea.insert(END, '\n Product\t\t  QTY\t\tPrice')
    textarea.insert(END, f"\n===========================================================")
    textarea.configure(font='arial 15 bold')

def gbill():
    if not has_items.get():
        messagebox.showerror('Error', 'No items added')
    else:
        welcome()
        tex = textarea.get(10.0, END)
        textarea.delete(1.0, END)
        textarea.insert(END, tex)
        textarea.insert(END, f"\n===========================================================")
        for i, item_details in enumerate(l, start=1):
            textarea.insert(END, f'{i}. {item_details}\n')
        textarea.insert(END, f"Total Paybill Amount:\t\t\t{sum(l)}")
        textarea.insert(END, f"\n===========================================================")

def savebill():
    op = messagebox.askyesno('Save bill', 'Do you want to save the bill')
    if op > 0:
        bill_details = textarea.get(1.0, END)
        f1 = open(f"bills/{billno.get()}.txt", 'w')
        f1.write(str(bill_details))
        f1.close()
        messagebox.showinfo('Bill no', f'Bill no:{billno.get()} Saved successfully')
    else:
        return

def clear():
    c_name.set('')
    c_phone.set('')
    item.set('')
    Rate.set(0)
    Quantity.set(0)
    welcome()

def exit():
    root.destroy()












title = Label(root, text='Billing Software', bg=bg_color, fg='white', font=('times new roman', 25, 'bold'), relief='groove')
title.pack(fill=X)

# Customer details
F1 = LabelFrame(root, text='Customer Details', font=('times new roman', 18, 'bold'), relief='groove', bd=10, bg=bg_color, fg='gold')
F1.place(x=0, y=80, relwidth=1)

cname_lbl = Label(F1, text='Customer Name', font=('times new roman', 18, 'bold'), bg=bg_color, fg='white')
cname_lbl.grid(row=0, column=0, pady=5)
cname_txt = Entry(F1, width=15, font='arial 15 bold', relief=SUNKEN, textvariable=c_name)
cname_txt.grid(row=0, column=1, padx=10, pady=5)

cphone_lbl = Label(F1, text='Phone Number', font=('times new roman', 18, 'bold'), bg=bg_color, fg='white')
cphone_lbl.grid(row=0, column=2, pady=5)
cphone_txt = Entry(F1, width=15, font='arial 15 bold', relief=SUNKEN, textvariable=c_phone)
cphone_txt.grid(row=0, column=3, padx=10, pady=5)

# Product details
F2 = LabelFrame(root, text='Product details', font=('times new roman', 18, 'bold'), relief='groove', bd=10, bg=bg_color, fg='gold')
F2.place(x=20, y=180, width=630, height=500)

itm = Label(F2, text='Product Name', font=('times new roman', '18', 'bold'), bg=bg_color, fg='lightgreen')
itm.grid(row=0, padx=30, pady=20)
itm_txt = Entry(F2, width=20, font='arial 15 bold', textvariable=item)
itm_txt.grid(row=0, column=1, padx=30, pady=20)

rate = Label(F2, text=' Product Rate', font=('times new roman', '18', 'bold'), bg=bg_color, fg='lightgreen')
rate.grid(row=1, padx=30, pady=20)
rate_txt = Entry(F2, width=20, font='arial 15 bold', textvariable=Rate)
rate_txt.grid(row=1, column=1, padx=30, pady=20)

quantity = Label(F2, text='Product Quantity', font=('times new roman', '18', 'bold'), bg=bg_color, fg='lightgreen')
quantity.grid(row=2, padx=30, pady=20)
quantity_txt = Entry(F2, width=20, font='arial 15 bold', textvariable=Quantity)
quantity_txt.grid(row=2, column=1, padx=30, pady=20)

# Buttons
btn1 = Button(F2, text='Add item', font='arial 15 bold', padx=5, pady=10, bg='lime', width=15, command=additm)
btn1.grid(row=3, column=0, padx=10, pady=30)

btn2 = Button(F2, text='Generate Bill', font='arial 15 bold', padx=5, pady=10, bg='lime', width=15, command=gbill)
btn2.grid(row=3, column=1, padx=10, pady=30)

btn3 = Button(F2, text='Clear', font='arial 15 bold', padx=5, pady=10, bg='lime', width=15, command=clear)
btn3.grid(row=4, column=0, padx=10, pady=30)

btn4 = Button(F2, text='Exit', font='arial 15 bold', padx=5, pady=10, bg='lime', width=15, command=exit)
btn4.grid(row=4, column=1, padx=10, pady=30)

# Bill area
F3 = Frame(root, relief=GROOVE, bd=10)
F3.place(x=700, y=180, width=500, height=500)

bill_title = Label(F3, text='Bill Area', font='arial 15 bold', relief=GROOVE, bd=7).pack(fill=X)
scroll_y = Scrollbar(F3, orient=VERTICAL)
textarea = Text(F3, yscrollcommand=scroll_y)
scroll_y.pack(side=RIGHT, fill=Y)
scroll_y.config(command=textarea.yview)
textarea.pack()
welcome()

root.mainloop()
