from tkinter import *
from tkinter import ttk
import math


class GUI:

    def __init__(self, window):
        self.window = window

        self.notebook = ttk.Notebook(window)

        # frames for the tabs
        self.tab1 = Frame(self.notebook)
        self.tab2 = Frame(self.notebook)
        self.tab3 = Frame(self.notebook)
        self.tab4 = Frame(self.notebook)

        # creating the tabs within the notebook
        self.notebook.add(self.tab1, text="Circle")
        self.notebook.add(self.tab2, text="Rectangle")
        self.notebook.add(self.tab3, text="Square")
        self.notebook.add(self.tab4, text="Triangle")
        self.notebook.pack()

        # Main title's for the tabs
        Label(self.tab1, text="Calculate the area of a circle:", font=('Arial', 36, 'bold'), width=0, height=0,
              pady=20).pack()
        Label(self.tab2, text="Calculate the area of a rectangle:", font=('Arial', 36, 'bold'), width=0, height=0,
              pady=20).pack()
        Label(self.tab3, text="Calculate the area of a square:", font=('Arial', 36, 'bold'), width=0, height=0,
              pady=20).pack()
        Label(self.tab4, text="Calculate the area of a triangle:", font=('Arial', 36, 'bold'), width=0, height=0,
              pady=20).pack()

        # Creating labels for the entry boxes
        Label(self.tab1, text="Enter Radius:", font=('Arial', 18), width=0, height=0, pady=20).pack()
        Label(self.tab2, text="Enter Length:", font=('Arial', 18), width=0, height=0, pady=20).pack()
        Label(self.tab3, text="Enter Length:", font=('Arial', 18), width=0, height=0, pady=20).pack()
        Label(self.tab4, text="Enter Height:", font=('Arial', 18), width=0, height=0, pady=20).pack()

        # Entry boxes for the radius, rectangle length, square length and height
        self.enter_radius = Entry(self.tab1, font=('Arial', 16))
        self.enter_length = Entry(self.tab2, font=('Arial', 16))
        self.enter_SqLength = Entry(self.tab3, font=('Arial', 16))
        self.enter_height = Entry(self.tab4, font=('Arial', 16))

        self.enter_radius.pack()
        self.enter_length.pack()
        self.enter_SqLength.pack()
        self.enter_height.pack()

        # Labels for the Entry boxes
        Label(self.tab2, text="Enter Width:", font=('Arial', 18), width=0, height=0, pady=20).pack()
        Label(self.tab4, text="Enter Width:", font=('Arial', 18), width=0, height=0, pady=20).pack()

        # Entry boxes for the rectangle width and triangle length
        self.enter_RectWidth = Entry(self.tab2, font=('Arial', 16))
        self.enter_TriLength = Entry(self.tab4, font=('Arial', 16))

        self.enter_RectWidth.pack()
        self.enter_TriLength.pack()

        # creating the buttons on the GUI
        self.circ_button = Button(self.tab1, text="Calculate", command=self.submit_circle)
        self.rect_button = Button(self.tab2, text="Calculate", command=self.submit_rectangle)
        self.sq_button = Button(self.tab3, text="Calculate", command=self.submit_square)
        self.tri_button = Button(self.tab4, text="Calculate", command=self.submit_triangle)

        # displaying the buttons on the GUI
        self.sq_button.pack()
        self.circ_button.pack()
        self.rect_button.pack()
        self.tri_button.pack()

        # Creating the labels for the answer box
        self.circ_answer = Label(self.tab1, text='', font=('Arial', 18), pady=20)
        self.circ_answer.pack()
        self.sq_answer = Label(self.tab3, text='', font=('Arial', 18), pady=20)
        self.sq_answer.pack()
        self.rect_answer = Label(self.tab2, text='', font=('Arial', 18), pady=20)
        self.rect_answer.pack()
        self.tri_answer = Label(self.tab4, text='', font=('Arial', 18), pady=20)
        self.tri_answer.pack()

    def submit_circle(self):
        """
        Calculates the area of a circle from the inputs of the user (radius). configures the label to display
        the correct answer with proper formatting.
        """
        try:
            radius = float(self.enter_radius.get())
        except:
            self.circ_answer.config(text='Not a numeric input')
        else:
            if radius <= 0:
                self.circ_answer.config(text='Not a positive number')
            else:
                circ_area = math.pi * radius * radius
                self.circ_answer.config(text=f'Area = {circ_area:.2f}')

    def submit_rectangle(self):
        """
        Calculates the area of a rectangle from the inputs of the user (length, width). configures the label to display
        the correct answer with proper formatting.
        """
        try:
            length = float(self.enter_length.get())
            width = float(self.enter_RectWidth.get())
        except:
            self.rect_answer.config(text='Not a numeric input')
        else:
            if length <= 0 or width <= 0:
                self.rect_answer.config(text='Not a positive number')
            else:
                rect_area = length * width
                self.rect_answer.config(text=f'Area = {rect_area:.2f}')

    def submit_square(self):
        """
        Calculates the area of a square from the inputs of the user (length). configures the label to display
        the correct answer with proper formatting.
        """
        try:
            sqlength = float(self.enter_SqLength.get())
        except:
            self.sq_answer.config(text='Not a numeric input')
        else:
            if sqlength <= 0:
                self.sq_answer.config(text='Not a positive number')
            else:
                sq_area = sqlength * sqlength
                self.sq_answer.config(text=f'Area = {sq_area:.2f}')

    def submit_triangle(self):
        """
        Calculates the area of a triangle from the inputs of the user (length, height). configures the label to display
        the correct answer with proper formatting.
        """
        try:
            height = float(self.enter_height.get())
            length = float(self.enter_TriLength.get())
        except:
            self.tri_answer.config(text='Not a numeric input')
        else:
            if length <= 0 or height <= 0:
                self.tri_answer.config(text='Not a positive number')
            else:
                tri_area = height * length * .5
                self.tri_answer.config(text=f'Area = {tri_area:.2f}')