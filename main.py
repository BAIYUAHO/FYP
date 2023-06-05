import tkinter as tk
from tkinter import font

def open_window1():
    # Code to open window for feature 1
    window1 = tk.Toplevel(root)
    window1.title("Feature 1: Object Count Detection")
    label1 = tk.Label(window1, text="This is the window for feature 1")
    label1.pack()

def open_window2():
    # Code to open window for feature 2
    window2 = tk.Toplevel(root)
    window2.title("Feature 2: Handwritten Digit Detection")
    label2 = tk.Label(window2, text="This is the window for feature 2")
    label2.pack()

def open_window3():
    # Code to open window for feature 3
    window3 = tk.Toplevel(root)
    window3.title("Feature 3: Arithmetic Symbol Detection")
    label3 = tk.Label(window3, text="This is the window for feature 3")
    label3.pack()

def open_window4():
    # Code to open window for feature 4
    window4 = tk.Toplevel(root)
    window4.title("Feature 4: Equation Recognition and Calculation")
    label4 = tk.Label(window4, text="This is the window for feature 4")
    label4.pack()

def open_window5():
    # Code to open window for feature 5
    window5 = tk.Toplevel(root)
    window5.title("Feature 5: Handwritten Calculation Result Detection")
    label5 = tk.Label(window5, text="This is the window for feature 5")
    label5.pack()

# Create main window
root = tk.Tk()
root.title("Preschool Mathematics Education Based on Image Detection")

# Set the size of the window
root.geometry("700x400")

# Create a label as the title
title_font = font.Font(size=30, weight="bold")
title_label = tk.Label(root, text="Preschool Mathematics Education", font=title_font)
title_label.pack(pady=10)

# Create buttons
button_font = font.Font(size=15)
button1 = tk.Button(root, text="Object Count Detection", command=open_window1, font=button_font, bg="lightblue", width=30)
button2 = tk.Button(root, text="Handwritten Digit Detection", command=open_window2, font=button_font, bg="lightgreen", width=30)
button3 = tk.Button(root, text="Arithmetic Symbol Detection", command=open_window3, font=button_font, bg="lightblue", width=30)
button4 = tk.Button(root, text="Equation Recognition and Calculation", command=open_window4, font=button_font, bg="lightgreen", width=30)
button5 = tk.Button(root, text="Handwritten Calculation Result Detection", command=open_window5, font=button_font, bg="lightblue", width=30)

# Add buttons to the main window
button1.pack(pady=10)
button2.pack(pady=10)
button3.pack(pady=10)
button4.pack(pady=10)
button5.pack(pady=10)

# Run the main window
root.mainloop()
