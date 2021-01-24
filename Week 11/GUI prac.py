import tkinter as tk #To use "generic" Widgets
from tkinter import ttk #To use stylized, "look-and-feel" widgets
"""
#create application window
window = tk.Tk()

#create user interface
my_label = ttk.Label(window, text = "Hello World!")
my_label.grid(row=1, column=1)

#Start GUI event loop
window.mainloop()

############# Messages ##########################
from tkinter import messagebox
messagebox.showinfo("Information","Informative message")
messagebox.showerror("Error", "Error message")
messagebox.showwarning("Warning","Warning message")

############## Yes/No questions ###################
from tkinter import messagebox

answer = messagebox.askokcancel("Question","Do you want to open this file?")
answer = messagebox.askretrycancel("Question", "Do you want to try that again?")
answer = messagebox.askyesno("Question","Do you like Python?")
answer = messagebox.askyesnocancel("Question", "Continue playing?")

################ Single Value Data Entry #############
from tkinter import simpledialog

application_window = tk.Tk()

answer = simpledialog.askstring("Input", "What is your first name?",
                                parent=application_window)
if answer is not None:
    print("Your first name is ", answer)
else:
    print("You don't have a first name?")

answer = simpledialog.askinteger("Input", "What is your age?",
                                 parent=application_window,
                                 minvalue=0, maxvalue=100)
if answer is not None:
    print("Your age is ", answer)
else:
    print("You don't have an age?")

answer = simpledialog.askfloat("Input", "What is your salary?",
                               parent=application_window,
                               minvalue=0.0, maxvalue=100000.0)
if answer is not None:
    print("Your salary is ", answer)
else:
    print("You don't have a salary?")

###################### File Chooser ##########################
from tkinter import filedialog
import os

application_window = tk.Tk()

# Build a list of tuples for each file type the file dialog should display
my_filetypes = [('all files', '.*'), ('text files', '.txt')]

# Ask the user to select a folder.
answer = filedialog.askdirectory(parent=application_window,
                                 initialdir=os.getcwd(),
                                 title="Please select a folder:")

# Ask the user to select a single file name.
answer = filedialog.askopenfilename(parent=application_window,
                                    initialdir=os.getcwd(),
                                    title="Please select a file:",
                                    filetypes=my_filetypes)

# Ask the user to select a one or more file names.
answer = filedialog.askopenfilenames(parent=application_window,
                                     initialdir=os.getcwd(),
                                     title="Please select one or more files:",
                                     filetypes=my_filetypes)

# Ask the user to select a single file name for saving.
answer = filedialog.asksaveasfilename(parent=application_window,
                                      initialdir=os.getcwd(),
                                      title="Please select a file name for saving:",
                                      filetypes=my_filetypes)
                                     
###################### Color Chooser ##########################
from tkinter import colorchooser
import tkinter as tk

application_window=tk.Tk()
rgb_color, web_color = colorchooser.askcolor(parent=application_window,
                                             initialcolor=(255, 0, 0))

############### Layout manager #################################
application_window = tk.Tk()
my_button = tk.Button(application_window, text="Example")
my_button.grid(row=3, column=1, sticky=tk.E + tk.W, pady=10)

my_button = tk.Button(application_window, text="Example")
my_button.pack(side=tk.TOP, fill=tk.Y, expand=True, pady=10)

##############@@@@@@#### Command events ###############################
def my_function():
  print("my_function was called.")
application_window = tk.Tk()
#my_button = tk.Button(application_window, text="Example", command=my_function)
#my_button.grid(row=3, column=1, sticky=tk.E + tk.W, pady=10)

# or

my_button = tk.Button(application_window, text="Example")
my_button.grid(row=3, column=1, sticky=tk.E + tk.W, pady=10)
my_button['command'] = my_function

#################### Enhanced Hello World Program #########################

# Create the application window
window = tk.Tk()

# Create the user interface
my_label = ttk.Label(window, text="Hello World")
my_label.grid(row=1, column=1)

quit_button = ttk.Button(window, text="Quit")
quit_button.grid(row=2, column=1)
quit_button['command'] = window.destroy

# Start the GUI event loop
window.mainloop()

############################# Event Binding ##########################
def process_event(event):
  print("The process_event function was called.")
application_window = tk.Tk()
my_button = tk.Button(application_window, text="Example")
my_button.grid(row=3, column=1, sticky=tk.E + tk.W, pady=10)
my_button.bind("<Enter>", process_event)

############# Program without class definition (Bad) #############
import tkinter as tk
from tkinter import ttk

global my_counter


def create_user_interface(application_window):
    global my_counter

    my_counter = ttk.Label(application_window, text="0")
    my_counter.grid(row=0, column=0)

    increment_button = ttk.Button(application_window, text="Add 1 to counter")
    increment_button.grid(row=1, column=0)
    increment_button['command'] = increment_counter

    quit_button = ttk.Button(application_window, text="Quit")
    quit_button.grid(row=2, column=0)
    quit_button['command'] = window.destroy


def increment_counter():
    global my_counter
    my_counter['text'] = str(int(my_counter['text']) + 1)

# Create the application window
window = tk.Tk()

create_user_interface(window)

# Start the GUI event loop
window.mainloop()

############### Program WITH class definition ######################
import tkinter as tk
from tkinter import ttk

def main():
    # Create the entire GUI program
    program = CounterProgram()

    # Start the GUI event loop
    program.window.mainloop()

class CounterProgram:

    def __init__(self):
        self.window = tk.Tk()
        self.my_counter = None  # All attributes should be initialize in init
        self.create_widgets()

    def create_widgets(self):
        self.my_counter = ttk.Label(self.window, text="0")
        self.my_counter.grid(row=0, column=0)

        increment_button = ttk.Button(self.window, text="Add 1 to counter")
        increment_button.grid(row=1, column=0)
        increment_button['command'] = self.increment_counter

        quit_button = ttk.Button(self.window, text="Quit")
        quit_button.grid(row=2, column=0)
        quit_button['command'] = self.window.destroy

    def increment_counter(self):
        self.my_counter['text'] = str(int(self.my_counter['text']) + 1)

if __name__ == "__main__":
    main()
"""
######################## Timer Events #########################
import tkinter as tk

application_window = tk.Tk()

def a_callback_function():
    print("a_callback_function was called.")

my_button = tk.Button(application_window, text="Example")
my_button.after(1000, a_callback_function)
