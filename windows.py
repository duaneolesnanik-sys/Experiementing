import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Itty Bitty Window Hater")
window.geometry("2000x2000")  # Width x Height
label = tk.Label(window, text="Duane is Cool.", font=("Arial", 20), fg="black", bg="green")
label.pack(pady=100)  # Add padding on the y-axis
label.pack()

def on_button_click():
    print("Button was clicked!")

# Create a button
button = tk.Button(window, text="Click Me", font=("Arial", 16), bg="green", fg="white", command=on_button_click)
button.pack(pady=20)
button.pack(padx=3)


entry = tk.Entry(window, font=("Arial", 16))
entry.pack(pady=10)

# Create a button to retrieve input
def get_input():
    user_input = entry.get()
    print(f"You entered: {user_input}")

button2 = tk.Button(window, text="Submit", command=get_input)
button2.pack()

check_var = tk.IntVar()

# Create a checkbox
checkbox = tk.Checkbutton(window, text="I agree to the terms", variable=check_var, font=("Arial", 14))
checkbox.pack(pady=20)

# Create a button to check the state
def check_state():
    if check_var.get() == 1:
        print("Checkbox is selected")
    else:
        print("Checkbox is not selected")

button3 = tk.Button(window, text="Check State", command=check_state)
button3.pack()

choice = tk.IntVar(value=0)

# Create radio buttons
tk.Radiobutton(window, text="Option 1", variable=choice, value=1).pack(anchor="w")
tk.Radiobutton(window, text="Option 2", variable=choice, value=2).pack(anchor="w")
tk.Radiobutton(window, text="Option 3", variable=choice, value=3).pack(anchor="w")

# Create a button to show the selected option
def show_choice():
    print(f"Selected option: {choice.get()}")

button4 = tk.Button(window, text="Submit", command=show_choice)
button4.pack()

def get_value():
    value = scale.get()
    print(f"Selected value: {value}")

scale = tk.Scale(window, from_=0, to=100, orient="horizontal", length=300, 
                 label="Select a Value", font=("Arial", 14), tickinterval=10)
scale.pack(pady=20)

# Create a button to retrieve the value
button5 = tk.Button(window, text="Get Value", command=get_value)
button5.pack()

def show_selection():
    selected_item = listbox.get(tk.ACTIVE)
    print(f"Selected item: {selected_item}")

# Function to add an item
def add_item():
    new_item = entry.get()
    if new_item:
        listbox.insert(tk.END, new_item)

# Function to delete the selected item
def delete_item():
    listbox.delete(tk.ACTIVE)

# Create a listbox
listbox = tk.Listbox(window, font=("Arial", 14), width=25, height=8)
listbox.pack(pady=10)

# Add some initial items
listbox.insert(1, "Apple")
listbox.insert(2, "Banana")
listbox.insert(3, "Cherry")

# Entry field to add new items
entry = tk.Entry(window, font=("Arial", 14))
entry.pack()

# Buttons for listbox operations
add_button = tk.Button(window, text="Add Item", command=add_item)
add_button.pack(pady=5)

delete_button = tk.Button(window, text="Delete Item", command=delete_item)
delete_button.pack(pady=5)

show_button = tk.Button(window, text="Show Selection", command=show_selection)
show_button.pack(pady=5)

# Run the application
window.mainloop()