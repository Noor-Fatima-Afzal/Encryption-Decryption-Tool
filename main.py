from tkinter import *
import base64
from tkinter import messagebox

root=Tk()
root.title("Encryption and decryption tool")
root.iconbitmap("favicon.ico")
root.configure(background="#ADF6A5")

def encrypt():
    #1 represents the first line and 0 represents the first character of that line
    secret=my_text.get(1.0, END)
    my_text.delete(1.0, END)

    if my_entry.get()=="noor":
        secret=secret.encode('ascii')
        secret=base64.b64encode(secret)
        #encrypted message is in bytes, so we need to decode it to string
        secret=secret.decode('ascii')
        my_text.insert(END, secret)
    else:
        messagebox.showwarning("Warning", "Please enter the corerct passward")

def decrypt():  
    secret=my_text.get(1.0, END)
    my_text.delete(1.0, END)
    if my_entry.get()=="noor":
        secret=secret.encode('ascii')
        secret=base64.b64decode(secret)
        secret=secret.decode('ascii')
        my_text.insert(END, secret)
    else:
        messagebox.showwarning("Warning", "Please enter the corerct passward")

def clear():
    my_text.delete(1.0, END)
    my_entry.delete(0, END)        

my_frame=Frame(root, background="#ADF6A5")
my_frame.pack(pady=20)

enc_button=Button(
        my_frame, 
    text="Encrypt", 
    command=encrypt, 
    font=("Helvetica", 20),
    background="green",
    foreground="white"
    )
enc_button.grid(row=0, column=0, padx=20)

dec_button=Button(
        my_frame, 
    text="Decrypt", 
    command=decrypt, 
    font=("Helvetica", 20),
    background="blue",
    foreground="white"
    )
dec_button.grid(row=0, column=1, padx=20)

clear_button=Button(
        my_frame, 
    text="Clear", 
    command=clear, 
    font=("Helvetica", 20),
    background="red",
    foreground="white"
    )
clear_button.grid(row=0, column=2, padx=20)

my_text= Text(
        root, 
    height=10, 
    width=40, 
    font=("Helvetica", 16),
    background="white",
    foreground="black"
    )
my_text.pack(pady=20)

passward_label=Label(
        root, 
    text="Enter the text to encrypt", 
    font=("Helvetica", 20),
    background="white",
    foreground="black"
    )
passward_label.pack(pady=20)

passward_label=Label(
        root, 
    text="Enter the passward", 
    font=("Helvetica", 20),
    background="white",
    foreground="black"
    )
passward_label.pack(pady=20)

my_entry=Entry(
        root, 
    font=("Helvetica", 24), 
    width=35 , 
    show="*",
    background="white",
    foreground="black"
    )
my_entry.pack(pady=20)

mainloop()