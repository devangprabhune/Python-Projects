import tkinter as tk
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+',
    '[', ']', '{', '}', '|', ';', ':', ',', '<', '.', '>', '/', '?']

def generate_password():
    try:
        letters_cnt = int(entry_letters.get())
        numbers_cnt = int(entry_numbers.get())
        symbols_cnt = int(entry_symbols.get())

        password_list=[]
        #appending random values in the empty password list
        for char in range(letters_cnt):
            password_list.append(random.choice(letters))

        for num in range(numbers_cnt):
            password_list.append(random.choice(numbers))

        for sym in range(symbols_cnt):
            password_list.append(random.choice(symbols))


        #jumbling the order of the letters, numbers and symbols
        random.shuffle(password_list)
        password = ''.join(password_list) #finalizing the password in the variable
    
        label_result.config(text = f"Generated password: {password}")
    except:
        label_result.config(text = f"Please enter valid numbers...")


#creating GUI window
root =  tk.Tk() # Toplevel widget of Tk which represents mostly the main window of an application. It has an associated Tcl interpreter.
root.title("Robust Password Generator")
root.geometry("400x300")

#label for welcome message
label_welcome = tk.Label(root, text = "Welcome to the Robust Password Generator", font = ("Arial", 14))
label_welcome.pack(pady = 10)

#creating input boxes for the letters, numbers and symbols
label_letters = tk.Label(root, text="How many letters? ")
label_letters.pack()
entry_letters = tk.Entry(root)
entry_letters.pack(pady=5)

label_numbers = tk.Label(root, text="How many numbers?")
label_numbers.pack()
entry_numbers = tk.Entry(root)
entry_numbers.pack(pady=5)

label_symbols = tk.Label(root, text="How many symbols?")
label_symbols.pack()
entry_symbols = tk.Entry(root)
entry_symbols.pack(pady=5)

#making a button to generate password
button_generate = tk.Button(root, text = "Generate Password", command= generate_password)
button_generate.pack(pady=10)

#label to display the generated password
label_result = tk.Label(root, text = "", font=("Arial", 12))
label_result.pack(pady=10)

#run the tkinter event loop
root.mainloop()
"""The mainloop() is the Tkinter event loop that runs the application, 
waits for events (like button clicks, key presses, etc.), 
and keeps the GUI window active."""
"""Once the mainloop() is called, the program enters a continuous loop, 
and the Tkinter window will respond to user interactions until the window is closed."""



        