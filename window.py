import tkinter as tk
from tkinter import filedialog
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
        self.remove_group_checkbox_dict = {}
        self.remove_group_name_list = []
        self.remove_group_url_list = []

        self.default_group_name_list = ["Group 1", "Group 2", "Group 3"]
        self.default_group_urls_list = ["http://www.google.com", "http://www.google.com", "http://www.google.com"]


        self.title("Automatic Facebook Group Poster")

        self.make_groups()
        self.menubar()

    def menubar(self):

        menubarroot = tk.Menu(self)

        file = tk.Menu(menubarroot, tearoff=0)
        menubarroot.add_cascade(label="File", menu=file)
        file.add_command(label="Add New Group", command=self.add_new_group_window)
        file.add_command(label="Remove Group", command=self.remove_group_window)
        file.add_separator()
        file.add_command(label="Exit", command=self.quit())

        self.config(menu=menubarroot)


    def add_new_group_window(self):
        self.add_group_window = tk.Toplevel(self)
        self.add_group_window.geometry("220x100")
        tk.Label(self.add_group_window, text="Enter New Group").grid(column=1, row=0, columnspan=2)
        tk.Label(self.add_group_window, text="Group Name:").grid(column=0, row=1)
        self.add_group_name = tk.Entry(self.add_group_window, textvariable=self.group_name).grid(column=1, row=1, columnspan=2)
        tk.Label(self.add_group_window, text="Group URL:").grid(column=0, row=2)
        self.add_group_url = tk.Entry(self.add_group_window, textvariable=self.group_url).grid(column=1, row=2, columnspan=2)
        tk.Button(self.add_group_window, text="Confirm", command=self.add_new_groups).grid(column=1, row=3)
        tk.Button(self.add_group_window, text="Cancel", command=self.add_group_window.destroy).grid(column=2, row=3)

    def add_new_groups(self):
        group_name_list.append(self.group_name.get())
        group_urls_list.append(self.group_url.get())

        with open("data/group/group_names.txt", "w") as filehandle:
            filehandle.writelines("%s\n" % names for names in group_name_list)
        with open("data/group/group_url.txt", "w") as filehandle:
            filehandle.writelines("%s\n" % urls for urls in group_urls_list)
        self.add_group_window.destroy()
        self.change(SecondFrame)

    def remove_group_window(self):
        self.add_removegroup_window = tk.Toplevel(self)
        self.add_removegroup_window.geometry("200x150")

        top_frame = tk.Frame(self.add_removegroup_window)
        top_frame.grid(column=0, row=0)
        bottom_frame = tk.Frame(self.add_removegroup_window)
        bottom_frame.grid(column=0, row=1)

        tk.Label(top_frame, text="Select Which Groups to Remove").grid(column=0, row=0)
        row = 1
        for name in group_name_list:
            variable = tk.IntVar()
            c = tk.Checkbutton(top_frame, variable=variable, text=name)
            c.grid(row=row, column=0, sticky="w")
            self.remove_group_checkbox_dict[name] = variable
            row += 1

        tk.Button(bottom_frame, command=self.remove_groups, text="Confirm").grid(column=0, row=0, padx=10, pady=10)
        tk.Button(bottom_frame, command=self.add_removegroup_window.destroy, text="Cancel").grid(column=1, row=0, padx=10, pady=10)

    def remove_groups(self):
        for group_name in self.remove_group_checkbox_dict:
            if self.remove_group_checkbox_dict[group_name].get() == 1:
                self.remove_group_name_list.append(group_name)
                self.remove_group_url_list.append(group_urls_list[group_name_list.index(group_name)])

        for name in self.remove_group_name_list:
            group_name_list.remove(name)
        for url in self.remove_group_url_list:
            group_urls_list.remove(url)

        with open("data/group/group_names.txt", "w") as filehandle:
            filehandle.writelines("%s\n" % names for names in group_name_list)
            filehandle.close()
        with open("data/group/group_url.txt", "w") as filehandle:
            filehandle.writelines("%s\n" % urls for urls in group_urls_list)
            filehandle.close()
        self.add_removegroup_window.destroy()
        self.change(SecondFrame)

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
                    current_place = line
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

        confirmbutton = tk.Button(self, text="Confirm", command=lambda: [self.login(), self.master.change(SecondFrame)])
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
        self.grid()
        self.master.geometry("480x470")

        self.timing_entry = []
        self.textbody = tk.StringVar()
        self.is_secondframe = True
        self.image_file = ""

        self.leftframe = tk.Frame(self.master)
        self.leftframe.grid(column=0, row=0, columnspan=4)
        self.rightframe = tk.Frame(self.master)
        self.rightframe.grid(column=4, row=0, sticky="n", columnspan=2)
        self.left_frame_items()
        self.right_frame_items()

        tk.Button(self.master, command=self.load_saved_text, text="Load Post").grid(column=0, row=1, pady=2)
        tk.Button(self.master, command=self.save_text, text="Save Text").grid(column=1, row=1, pady=2)
        #tk.Label(self.master).grid(column=2, row=1)
        tk.Button(self.master, command=self.load_image, text="Load Image").grid(column=2, row=1, padx=2, pady=2)
        #tk.Label(self.master, width=10).grid(column=5, row=1, columnspan=2)
        tk.Button(self.master, command=self.inputdata, text="Confirm Details").grid(column=5, row=1, padx=2, pady=2)
        tk.Button(self.master, command=self.quit_app, text="Close").grid(column=6, row=1, padx=2, pady=2)


    def left_frame_items(self):
        tk.Label(self.leftframe, text="Text for Post Submission", pady=10).grid(column=0, row=0)

        self.text_for_post = tk.Text(self.leftframe, width=40)
        self.text_for_post.grid(column=0, row=1, rowspan=9, padx=5, pady=5)

    def right_frame_items(self):
        self.group_checkbox_dict = {}

        label1 = tk.Label(self.rightframe, text="Groups to Post to", anchor="center", pady=10)
        label1.grid(column=0, row=0, columnspan=2)
        row = 1
        for name in group_name_list:
            variable = tk.IntVar()
            c = tk.Checkbutton(self.rightframe, variable=variable, text=name)
            c.grid(row=row, column=0, sticky="w")
            self.group_checkbox_dict[name] = variable
            row += 1

    def rightbttm_frame_items(self):
        label = tk.Label(self.rightbttmframe, text="Select Image")
        label.grid(column=0, row=0)
        button = tk.Button(self.rightbttmframe, text="Select Image", command=self.load_image)
        button.grid(column=0, row=1)
        canvas = tk.Canvas(self.rightbttmframe, width=300, height=300)
        canvas.grid(column=0, row=0)
        img = tk.PhotoImage(file=self.image_file)
        # canvas.create_image(0, 0, img=self.image_file)

    def load_image(self):
        self.image_file = filedialog.askopenfilename(initialdir="./data/post", title="Select an Image",
                                              filetypes=(("JPEG files", "*.jpg*"), ("All Files", "*.*")))

    def inputdata(self):
        post_text = self.text_for_post.get("1.0", "end-1c")
        self.email_file = open("email.txt", "r")
        email = self.email_file.read()
        self.email_file.close()
        self.password_file = open("password.txt", "r")
        password = self.password_file.read()
        self.password_file.close()
        image = self.image_file

        for group_name in self.group_checkbox_dict:
            if self.group_checkbox_dict[group_name].get() == 1:
                url = group_urls_list[group_name_list.index(group_name)]
                Log_in(email, password, url, post_text, image)

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

    def quit_app(self):
        os.remove("email.txt")
        os.remove("password.txt")
        self.quit()



