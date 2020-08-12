import tkinter as tk
from tkinter import filedialog, font
from logging_in import Log_in
import os


class MainWindow(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.frame = None
        self.change(LoginFrame)
        self.group_name = tk.StringVar()
        self.group_url = tk.StringVar()
        global group_name_list
        group_name_list = []
        global group_urls_list
        group_urls_list = []
        self.is_secondframe = False

        self.default_group_name_list = ["Group 1", "Group 2", "Group 3"]
        self.default_group_urls_list = ["http://www.google.com", "http://www.google.com", "http://www.google.com"]


        self.title("Automatic Facebook Group Poster")

        self.make_groups()

        menubarroot = tk.Menu(self.master)

        file = tk.Menu(menubarroot, tearoff=0)
        menubarroot.add_cascade(label="File", menu=file)
        file.add_command(label="Add New Group", command=self.add_new_group_name)
        file.add_command(label="Remove Group", command=self.remove_group)
        file.add_separator()
        file.add_command(label="Exit", command=self.quit())

        self.config(menu=menubarroot)

    def make_groups(self):
        try:
            with open("data/group/group_names.txt", "r") as filehandle:
                filecontents = filehandle.readlines()
                for line in filecontents:
                    current_place = line[:-1]
                    group_name_list.append(current_place)
        except FileNotFoundError:
            os.mkdir("data")
            os.mkdir("data/group")
            os.mkdir("data/post")
            with open("data/group/group_names.txt", "w") as filehandle:
                filehandle.writelines("%s\n" % names for names in self.default_group_name_list)
            filehandle.close()
            with open("data/group/group_names.txt", "r") as filehandle:
                filecontents = filehandle.readlines()
                for line in filecontents:
                    current_place = line[:-1]
                    group_name_list.append(current_place)

        try:
            with open("data/group/group_url.txt", "r") as filehandle:
                filecontents = filehandle.readlines()
                for line in filecontents:
                    current_place = line[:-1]
                    group_urls_list.append(current_place)
        except FileNotFoundError:
            with open("data/group/group_url.txt", "w") as filehandle:
                filehandle.writelines("%s\n" % urls for urls in self.default_group_urls_list)
            filehandle.close()
            with open("data/group/group_url.txt", "r") as filehandle:
                filecontents = filehandle.readlines()
                for line in filecontents:
                    current_place = line[:-1]
                    group_urls_list.append(current_place)

    def change(self, frame_class):
        new_frame = frame_class(self)
        if self.frame is not None:
            self.frame.destroy()
        self.frame = new_frame
        self.frame.grid()

    def add_new_group_name(self):
        self.add_group_window = tk.Toplevel(self)
        self.add_group_window.geometry("220x100")
        tk.Label(self.add_group_window, text="Enter New Group").grid(column=1, row=0, columnspan=2)
        tk.Label(self.add_group_window, text="Group Name:").grid(column=0, row=1)
        self.add_group_name = tk.Entry(self.add_group_window, textvariable=self.group_name).grid(column=1, row=1, columnspan=2)
        tk.Label(self.add_group_window, text="Group URL:").grid(column=0, row=2)
        self.add_group_url = tk.Entry(self.add_group_window, textvariable=self.group_url).grid(column=1, row=2, columnspan=2)
        tk.Button(self.add_group_window, text="Confirm", command=self.save_groups).grid(column=1, row=3)
        tk.Button(self.add_group_window, text="Cancel", command=self.add_group_window.quit).grid(column=2, row=3)

    def save_groups(self):
        group_name_list.append(self.group_name.get())
        group_urls_list.append(self.group_url.get())

        with open("data/group/group_names.txt", "w") as filehandle:
            filehandle.writelines("%s\n" % names for names in group_name_list)
        with open("data/group/group_url.txt", "w") as filehandle:
            filehandle.writelines("%s\n" % urls for urls in group_urls_list)

        if self.is_secondframe:
            self.make_group_checks()

        self.add_group_window.destroy()


    def remove_group(self):
        self.add_removegroup_window = tk.Toplevel(self)
        argw = tk.LabelFrame(self.add_removegroup_window, text="Select Which Groups to Remove").pack()
        tk.Label(argw, text="")


class LoginFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master.geometry("250x130")

        self.t_email = tk.StringVar()
        self.t_password = tk.StringVar()

        tk.Label(self, text="Please Login to Facebook").grid(column=0, row=0, padx=10, pady=10, columnspan=4)
        email_label = tk.Label(self, text="Email:").grid(column=0, row=1, sticky=tk.W, padx=25)
        password_label = tk.Label(self, text="Password:").grid(column=0, row=2, sticky=tk.W, padx=25)

        email_details = tk.Entry(self, textvariable=self.t_email).grid(column=2, row=1, columnspan=2)
        password_details = tk.Entry(self, textvariable=self.t_password, show="*").grid(column=2, row=2, columnspan=2)

        confirmbutton = tk.Button(self, text="Confirm", command=lambda: [self.login(), master.change(SecondFrame)])
        confirmbutton.grid(column=2, row=4)

    def login(self):
        email = self.t_email.get()
        password = self.t_password.get()

        email_file = open("email.txt", "w")
        email_file.write(email)
        email_file.close()

        password_file = open("password.txt", "w")
        password_file.write(password)
        password_file.close()
class SecondFrame(tk.Frame, MainWindow):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master.geometry("550x470")

        self.group_checkbox_dict = {}

        self.timing_entry = []

        self.textbody = tk.StringVar()
        self.is_secondframe = True

        self.frame = tk.Frame(self).grid(column=0, row=0)

        tk.Label(self.frame, text="Text for Post Submission", anchor="e", pady=10).grid(column=0, row=0, columnspan=4)

        self.text_for_post = tk.Text(self.frame, width=40)
        self.text_for_post.grid(column=0, row=1, columnspan=4, rowspan=9, padx=5, pady=5)
        tk.Button(self.frame, command=self.load_saved_text, text="Load Post").grid(column=0, row=10, padx=2, pady=2)
        tk.Button(self.frame, command=self.save_text, text="Save Text").grid(column=1, row=10, padx=2, pady=2)
        tk.Button(self.frame, command=self.inputdata, text="Confirm Details").grid(column=2, row=10, padx=2, pady=2)

        # ne_frame = tk.Frame(self).grid(column=3)

        label1 = tk.Label(self.frame, text="Groups to Post to", anchor="w").grid(column=6, row=0, columnspan=2)
        self.make_group_checks()

        # se_frame = tk.LabelFrame(self, text="Posting Frequency").grid(column=1, row=1)

        # label2 = tk.Label(right_frame, text="Posting Frequency").grid(column=0, row=4)
        # f2 = font.Font(label2, label2.cget("font")).configure(underline=True)
        # label2.configure(font=f2)

        ####tk.Checkbutton(right_frame, variable=self.checkbuttondec4, text="Every 4 hours").grid(column=0, row=5)
        ####tk.Checkbutton(right_frame, variable=self.checkbuttondec5, text="Every 8 hours").grid(column=0, row=6)
        ####tk.Checkbutton(right_frame, variable=self.checkbuttondec6, text="Every 12 hours").grid(column=0, row=7)

        # self.confirm_button = tk.Button(self, text="Confirm", command=self.inputdata).grid(column=1, row=9)
        # self.quit_button = tk.Button(self, text="Quit", command=self.quit).grid(column=0, row=9)

    def make_group_checks(self):
        row = 1
        for name in group_name_list:
            variable = tk.IntVar()
            c = tk.Checkbutton(self.frame, variable=variable, text=name)
            c.grid(row=row, column=5, sticky="w")
            self.group_checkbox_dict[name] = variable
            row += 1

    def inputdata(self):
        post_text1 = self.text_for_post.get("1.0", "end-1c")
        print(post_text1)
        print(type(post_text1))
        email_file = open("email.txt", "r")
        email = email_file.read()
        email_file.close()
        os.remove("email.txt")
        password_file = open("password.txt", "r")
        password = password_file.read()
        password_file.close()
        os.remove("password.txt")

        for group_name in self.group_checkbox_dict:
            if self.group_checkbox_dict[group_name].get() == 1:
                url1 = group_urls_list[group_name_list.index(group_name)]
                Log_in(email, password)
                Log_in.access_group(url1, post_text1)

    def load_saved_text(self):
        filename = filedialog.askopenfilename(initialdir="./data/post", title="Select a File",
                                              filetypes=(("Text files", "*.txt*"), ("all files", "*.*")))
        with open(filename, "r") as f:
            self.text_for_post.insert(tk.INSERT, f.read())
        f.close()

    def save_text(self):
        post_text = open("data/post/post_test.txt", "w")
        post_text.write(self.text_for_post.get("1.0", "end-1c"))
        post_text.close()
