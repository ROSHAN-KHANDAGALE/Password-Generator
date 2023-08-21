import random
import string
import tkinter as tk

def password_generate(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_password():
    try:
        passlength = int(input1.get())
        if passlength <= 0:
            input2.delete(0, tk.END)
            input2.insert(0, 'INVALID GENERATION')
            return
        generated = password_generate(passlength)
        input2.delete(0, tk.END)
        input2.insert(0, generated)
    except ValueError:
        input2.delete(0, tk.END)
        input2.insert(0, 'Invalid input!!')

frame = tk.Tk()
frame.geometry('450x250')
frame.title('PASSWORD GENERATOR')
frame.configure(bg='grey')

fontProp = ('Cascadia Mono SemiBold', 12)

text0 = tk.Label(frame, font=fontProp, bg='red', text='PASSWORD GENERATOR!!')
text0.pack(pady=10)

txt1 = tk.Label(frame, font=fontProp, bg='white', text='ENTER LENGTH OF PASSWORD : ')
txt1.configure(bg='orange')
txt1.pack(pady=5)

input1 = tk.Entry(frame, font=fontProp, justify='center')
input1.pack()

btn_generate = tk.Button(frame, font=fontProp, text='GENERATE PASSWORD', command=generate_password, bg='teal')
btn_generate.pack(pady=10)

input2 = tk.Entry(frame, font=fontProp, width=20, justify='center')
input2.pack()

frame.mainloop()
