import tkinter as tk
from tkinter import filedialog, font

class MainWindow(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.frame = LoginFrame(self)
        self.frame.grid()

    def change(self, frame):
        self.frame.grid_forget()
        self.frame = frame(self)
        self.frame.grid()

class LoginFrame(tk.Frame):
    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        self.master.title("Facebook Login")
        self.master.geometry("260x125")

        self.email_entry = ""
        self.password_entry = ""
        self.t_email = tk.StringVar()
        self.t_password = tk.StringVar()

        tk.Label(self, text="Please Login to Facebook").grid(column=0, row=0, padx=10, pady=10, columnspan=4)
        email_label = tk.Label(self, text="Email:").grid(column=0, row=1, sticky=tk.W, padx=25)
        password_label = tk.Label(self, text="Password:").grid(column=0, row=2, sticky=tk.W, padx=25)

        email_details = tk.Entry(self, textvariable=self.t_email).grid(column=2, row=1, columnspan=2)
        password_details = tk.Entry(self, textvariable=self.t_password, show="*").grid(column=2, row=2, columnspan=2)

        confirmbutton = tk.Button(self, text="Confirm", command=self.login).grid(column=2, row=4)

    def login(self):
        self.email_entry = self.t_email.get()
        self.password_entry = self.t_password.get()
        self.master.change(SecondFrame)


class SecondFrame(tk.Frame):
    def __init__(self, master, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        self.master.title("Facebook Automatic Group Poster")
        self.master.geometry("410x250")

        self.timing_entry = []
        self.grouplinks_entry = []
        self.filename1 = ""

        self.posttitle = tk.StringVar()
        self.checkbuttondec1 = tk.IntVar()
        self.checkbuttondec2 = tk.IntVar()
        self.checkbuttondec3 = tk.IntVar()
        self.checkbuttondec4 = tk.IntVar()
        self.checkbuttondec5 = tk.IntVar()
        self.checkbuttondec6 = tk.IntVar()

        tk.Label(self, text="Post Title:").grid(column=0, row=0)
        tk.Label(self, text="Body of Text:").grid(column=0, row=1, pady=10)
        tk.Label(self).grid(column=0, row=2, columnspan=3)
        options = tk.Label(self, text="         Options         ")
        options.grid(column=0, row=3)
        f = font.Font(options, options.cget("font"))
        f.configure(underline=True)
        options.configure(font=f)

        tk.Label(self, text="Groups to Post to").grid(column=0, row=4)
        tk.Label(self, text="Posting Frequency").grid(column=1, row=4)

        tk.Entry(self, textvariable=self.posttitle, width=50).grid(column=1, row=0, columnspan=3)
        tk.Button(self, text="Browse Files", command=self.browsefiles1).grid(column=1, row=1, sticky="W")

        tk.Checkbutton(self, variable=self.checkbuttondec1, text="Group 1").grid(column=0, row=5)
        tk.Checkbutton(self, variable=self.checkbuttondec2, text="Group 2").grid(column=0, row=6)
        tk.Checkbutton(self, variable=self.checkbuttondec3, text="Group 3").grid(column=0, row=7)

        tk.Checkbutton(self, variable=self.checkbuttondec4, text="Every 4 hours").grid(column=1, row=5)
        tk.Checkbutton(self, variable=self.checkbuttondec5, text="Every 8 hours").grid(column=1, row=6)
        tk.Checkbutton(self, variable=self.checkbuttondec6, text="Every 12 hours").grid(column=1, row=7)

        self.confirm_button = tk.Button(self, text="Confirm", command=self.inputdata).grid(column=1, row=9)
        self.quit_button = tk.Button(self, text="Quit", command=self.quit).grid(column=0, row=9)

    def inputdata(self):
        self.from_date_entry = self.t_from_date.get()
        self.to_date_entry = self.t_to_date.get()
        if self.checkbuttondec1 == 1:
            self.grouplinks_entry += ["link one", ]
        if self.checkbuttondec2 == 1:
            self.grouplinks_entry += ["link two", ]
        if self.checkbuttondec3 == 1:
          self.grouplinks_entry += ["link three", ]

        self.quit()

    def browsefiles1(self):
        self.filename1 = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("Text File", "*.txt*"), ("All Files", "*.*")))



