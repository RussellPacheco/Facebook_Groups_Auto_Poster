import tkinter as tk
from tkinter import filedialog, font
from .logging_in import Log_in
import ast
import os

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

        #self.email_entry = "" probably dont need this
        #self.password_entry = "" probably dont need this
        self.t_email = tk.StringVar()
        self.t_password = tk.StringVar()

        tk.Label(self, text="Please Login to Facebook").grid(column=0, row=0, padx=10, pady=10, columnspan=4)
        email_label = tk.Label(self, text="Email:").grid(column=0, row=1, sticky=tk.W, padx=25)
        password_label = tk.Label(self, text="Password:").grid(column=0, row=2, sticky=tk.W, padx=25)

        email_details = tk.Entry(self, textvariable=self.t_email).grid(column=2, row=1, columnspan=2)
        password_details = tk.Entry(self, textvariable=self.t_password, show="*").grid(column=2, row=2, columnspan=2)

        confirmbutton = tk.Button(self, text="Confirm", command=self.login).grid(column=2, row=4)

    def login(self):
        self.t_email.get()
        self.password_entry = self.t_password.get()
        self.master.change(SecondFrame)


class SecondFrame(tk.Frame):
    def __init__(self, master, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        self.master.title("Facebook Automatic Group Poster")
        self.master.geometry("410x250")

        try:
            self.group_link_file = open("data/group_links.txt", "r")
        except FileNotFoundError:
            os.mkdir("data")
            self.group_link_file = open("data/group_links.txt", "w")
            file.write("""("Group Links 1", "http://www.google.com")""")
            self.group_link_file.close()
            self.group_link_file = open("data/group_links.txt", "r")


        self.timing_entry = []
        self.grouplinks_entry = []
        self.filename1 = ""

        self.textbody = tk.StringVar()
        self.group_name = tk.StringVar()
        self.group_url = tk.StringVar()
        self.checkbuttondec1 = tk.IntVar()
        self.checkbuttondec2 = tk.IntVar()
        self.checkbuttondec3 = tk.IntVar()
        self.checkbuttondec4 = tk.IntVar()
        self.checkbuttondec5 = tk.IntVar()
        self.checkbuttondec6 = tk.IntVar()

        menubar = tk.Menu(self)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Add New Group", command=self.add_new_group_name)
        filemenu.add_command(label="Remove Group", command=self.remove_group)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.quit())

        left_frame = tk.LabelFrame(self, text="Type Post Here").grid(column=0)

        #tk.Label(left_frame, text="Body of Text:").grid(column=0, row=0, pady=10) probably dont need this
        #tk.Label(left_frame).grid(column=0, row=1, columnspan=3) probably dont need this

        text_for_post = tk.Text(left_frame).grid(column=0, row=0)
        tk.Button(left_frame, command=self.load_saved_text, text="Load Post").grid(column=0, row=1, columnspan=3)
        tk.Button(left_frame, command=self.save_text, text="Save Text").grid(column=1, row=1)
        tk.Button(left_frame, command=self.send_text, text="Confirm Details").grid(column=2, row=1)

        right_frame= tk.LabelFrame(self, text="Options").grid(column=1)

        label1 = tk.Label(right_frame, text="Groups to Post to").grid(column=0, row=0)
        f1 = font.Font(label1, label1.cget("font")).configure(underline=True)
        label1.configure(font=f1)

        for i in len(self.group_link_file)


            tk.Checkbutton(right_frame, variable=self.checkbuttondec[i] text=f"{[i]}").grid(column=0, row=1)
        tk.Checkbutton(right_frame, variable=self.checkbuttondec2, text="Group 2").grid(column=0, row=2)
        tk.Checkbutton(right_frame, variable=self.checkbuttondec3, text="Group 3").grid(column=0, row=3)

        label2 = tk.Label(right_frame, text="Posting Frequency").grid(column=0, row=4)
        f2 = font.Font(label2, label2.cget("font")).configure(underline=True)
        label2.configure(font=f2)

        tk.Checkbutton(right_frame, variable=self.checkbuttondec4, text="Every 4 hours").grid(column=0, row=5)
        tk.Checkbutton(right_frame, variable=self.checkbuttondec5, text="Every 8 hours").grid(column=0, row=6)
        tk.Checkbutton(right_frame, variable=self.checkbuttondec6, text="Every 12 hours").grid(column=0, row=7)

        #self.confirm_button = tk.Button(self, text="Confirm", command=self.inputdata).grid(column=1, row=9)
        #self.quit_button = tk.Button(self, text="Quit", command=self.quit).grid(column=0, row=9)

    def add_new_group_name(self):
        self.add_group_window = tk.Toplevel(self)
        agw = tk.LabelFrame(add_group_window, text="Enter New Group").grid(column=0)
        tk.Label(agw, text="Group Name:").grid(column=0, row=0)
        self.group_name = tk.Entry(agw, textvariable=self.group_name).grid(column=1, row=0)
        tk.Label(agw, text="Group URL:").grid(column=0, row=2)
        self.group_url = tk.Entry(agw, textvariable=self.group_url).grid(column=1, row=0)
        tk.Button(agw, text="Confirm", command=self.save_groups.grid(column=0, row=3)
        tk.Button(agw, text="Cancel", command=self.add_group_window.quit)

    def save_groups(self):
        self.grouplinks_entry.append((self.group_name.get(), self.group_url.get()))
        self.group_links_file.write(str(self.grouplinks_entry))


    def inputdata(self):
        if self.checkbuttondec1 == 1:
            self.grouplinks_entry += ["link one", ]
        if self.checkbuttondec2 == 1:
            self.grouplinks_entry += ["link two", ]
        if self.checkbuttondec3 == 1:
          self.grouplinks_entry += ["link three", ]

        self.quit()


