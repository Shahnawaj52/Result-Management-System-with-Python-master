from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3

class student_class:
    def __init__(self, r):
        self.root = r
        self.root.geometry("1380x600")
        self.root.title("Student")
        self.root.config(bg="#d3d9e2")
        self.root.focus_force()  # to make focus forcefully from dashboard

        title = Label(self.root, text="Manage Student Info", font="arial 15 bold", bg="#7e57c2", fg="white")
        title.place(x=10, y=10, relwidth=0.985, height=45)

        # =========ROLL============
        roll = Label(self.root, text="Roll :", font="arial 13 ", bg="#fffcf2", bd="1", relief=RIDGE)
        roll.place(x=10, y=80, width=150, height=55)

        self.roll_var = IntVar()
        self.roll_entry = Entry(self.root, textvariable=self.roll_var, font="arial 13 ", bg="#eee9dc")  # Entry() is used for making input box
        self.roll_entry.place(x=160, y=80, width=170, height=55)

        # =========NAME============
        name = Label(self.root, text="Name :", font="arial 13 ", bg="#fffcf2", bd="1", relief=RIDGE)
        name.place(x=10, y=145, width=150, height=55)

        self.name_var = StringVar()
        self.name_entry = Entry(self.root, textvariable=self.name_var, font="arial 13 ", bg="#eee9dc")  # Entry() is used for making input box
        self.name_entry.place(x=160, y=145, width=170, height=55)

        # =========EMAIL============
        email = Label(self.root, text="Email :", font="arial 13 ", bg="#fffcf2", bd="1", relief=RIDGE)
        email.place(x=10, y=210, width=150, height=55)

        self.email_var = StringVar()
        self.email_entry = Entry(self.root, textvariable=self.email_var, font="arial 13 ", bg="#eee9dc")  # Entry() is used for making input box
        self.email_entry.place(x=160, y=210, width=170, height=55)

        # =========GENDER============
        gender = Label(self.root, text="Gender :", font="arial 13 ", bg="#fffcf2", bd="1", relief=RIDGE)
        gender.place(x=10, y=275, width=150, height=55)

        self.gender_var = StringVar()
        self.gender_entry = ttk.Combobox(self.root, textvariable=self.gender_var, font="arial 13 ", state='readonly',
                                         values=("Male", "Female"))  # Entry() is used for making input box
        self.gender_entry.place(x=160, y=275, width=170, height=55)

        # =========BIRTHDAY============
        birthday = Label(self.root, text="Birthday :", font="arial 13 ", bg="#fffcf2", bd="1", relief=RIDGE)
        birthday.place(x=350, y=80, width=150, height=55)

        self.birthday_var = StringVar()
        self.birthday_entry = Entry(self.root, textvariable=self.birthday_var, font="arial 13 ",
                                    bg="#eee9dc")  # Entry() is used for making input box
        self.birthday_entry.place(x=500, y=80, width=170, height=55)

        # =========CONTACT============
        contact = Label(self.root, text="Contact :", font="arial 13 ", bg="#fffcf2", bd="1", relief=RIDGE)
        contact.place(x=350, y=145, width=150, height=55)

        self.contact_var = IntVar()
        self.contact_entry = Entry(self.root, textvariable=self.contact_var, font="arial 13 ",
                                   bg="#eee9dc")  # Entry() is used for making input box
        self.contact_entry.place(x=500, y=145, width=170, height=55)

        # =========COURSE NAME============
        self.course_list = ["Empty"]

        course_name = Label(self.root, text="Course Name :", font="arial 13 ", bg="#fffcf2", bd="1", relief=RIDGE)
        course_name.place(x=350, y=210, width=150, height=55)

        self.course_name_var = StringVar()
        self.course_name_entry = ttk.Combobox(self.root, textvariable=self.course_name_var, font="arial 13 ", state='readonly',
                                              values=self.course_list)  # Entry() is used for making input box
        self.course_name_entry.place(x=500, y=210, width=170, height=55)

        # =========CITY============
        city = Label(self.root, text="City :", font="arial 13 ", bg="#fffcf2", bd="1", relief=RIDGE)
        city.place(x=350, y=275, width=150, height=55)

        self.city_var = StringVar()
        self.city_entry = Entry(self.root, textvariable=self.city_var, font="arial 13 ",
                                bg="#eee9dc")  # Entry() is used for making input box
        self.city_entry.place(x=500, y=275, width=170, height=55)

        # =========ADDRESS============
        address = Label(self.root, text="Address :", font="arial 13 ", bg="#fffcf2", bd="1", relief=RIDGE)
        address.place(x=10, y=340, width=150, height=100)

        self.address_entry = Text(self.root, font="arial 13 ", bg="#eee9dc")  # Entry() is used for making input box
        self.address_entry.place(x=160, y=340, width=510, height=100)

        # All buttons
        ButtonFrame = Frame(self.root, bg="white")
        ButtonFrame.place(x=10, y=445, width=660, height=70)

        self.add = Button(ButtonFrame, text="Save", font="arial 13 bold", bg="dodgerblue", fg="white", cursor="hand2", command=self.add)
        self.add.place(x=15, y=10, width=200, height=50)

        self.update = Button(ButtonFrame, text="Update", font="arial 13 bold", bg="slateblue", fg="white", cursor="hand2", command=self.update)
        self.update.place(x=230, y=10, width=200, height=50)

        self.delete = Button(ButtonFrame, text="Delete", font="arial 13 bold", bg="tomato", fg="white", cursor="hand2", command=self.delete)
        self.delete.place(x=445, y=10, width=200, height=50)

        # Search Panel
        self.search_var = StringVar()
        search_label = Label(self.root, text="Roll No.: ", font="arial 13", bg="white", bd="1", relief=RIDGE).place(x=700, y=80, height=55, width=160)
        search_entry = Entry(self.root, textvariable=self.search_var, font="arial 13", bg="white").place(x=870, y=80, width=360, height=55)
        btn_search = Button(self.root, text="Search", font="arial 13 bold", bg="dodgerblue", fg="white", cursor="hand2", command=self.search).place(x=1220, y=80, width=150, height=55)

        # Course frame
        self.courseFrame = Frame(self.root, bd=2, relief=RIDGE)
        self.courseFrame.place(x=700, y=140, width=670, height=310)

        # Headings and Columns for the tables
        self.CourseTable = ttk.Treeview(self.courseFrame, columns=("roll", "name", "email", "gender", "birthday", "contact", "course", "address"))
        self.CourseTable.pack(fill=BOTH, expand=1)

        self.CourseTable.heading("roll", text="Roll")
        self.CourseTable.heading("name", text="Name")
        self.CourseTable.heading("email", text="Email")
        self.CourseTable.heading("gender", text="Gender")
        self.CourseTable.heading("birthday", text="Birthday")
        self.CourseTable.heading("contact", text="Contact")
        self.CourseTable.heading("course", text="Course")
        self.CourseTable.heading("address", text="Address")

        self.CourseTable["show"] = "headings"
        self.CourseTable.column("roll", width=70)
        self.CourseTable.column("name", width=70)
        self.CourseTable.column("email", width=70)
        self.CourseTable.column("gender", width=70)
        self.CourseTable.column("birthday", width=70)
        self.CourseTable.column("contact", width=70)
        self.CourseTable.column("course", width=70)
        self.CourseTable.column("address", width=70)
        self.show_students()  # all previous stored data will show

    ##################
    # add course
    def add(self):
        connect = sqlite3.connect(database="rms.db")
        cursor = connect.cursor()

        try:
            # Message box for no course entry
            if self.roll_var.get() == "":
                messagebox.showerror("Error", "Roll must be required", parent=self.root)
            else:
                cursor.execute("SELECT * FROM student WHERE roll=?", (self.roll_var.get(),))
                row = cursor.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "Roll no. already present", parent=self.root)
                else:
                    cursor.execute(
                        "INSERT INTO student(roll, name, email, gender, birthday, contact, course, address) VALUES(?,?,?,?,?,?,?,?)",
                        (self.roll_var.get(),
                         self.name_var.get(),
                         self.email_var.get(),
                         self.gender_var.get(),
                         self.birthday_var.get(),
                         self.contact_var.get(),
                         self.course_name_var.get(),
                         self.address_entry.get("1.0", END)))
                    connect.commit()
                    messagebox.showinfo("Success", "Student added successfully", parent=self.root)
                    self.show_students()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    #################
    # show course data
    def show_students(self):
        connect = sqlite3.connect(database="rms.db")
        cursor = connect.cursor()
        try:
            cursor.execute("SELECT * FROM student")
            rows = cursor.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    #######################
    # get data for show data in fields
    def get_data(self, ev):
        read = self.CourseTable.focus()
        content = self.CourseTable.item(read)
        row = content['values']
        # print(row)
        self.roll_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.birthday_var.set(row[4])
        self.contact_var.set(row[5])
        self.course_name_var.set(row[6])
        self.address_entry.delete("1.0", END)
        self.address_entry.insert(END, row[7])

    #####################
    # update course data
    def update(self):
        connect = sqlite3.connect(database="rms.db")
        cursor = connect.cursor()
        try:
            cursor.execute("SELECT * FROM student WHERE roll=?", (self.roll_var.get(),))
            row = cursor.fetchone()
            if row is None:
                messagebox.showerror("Error", "Select student from list", parent=self.root)
            else:
                cursor.execute("UPDATE student SET name=?, email=?, gender=?, birthday=?, contact=?, course=?, address=? WHERE roll=?",
                               (self.name_var.get(),
                                self.email_var.get(),
                                self.gender_var.get(),
                                self.birthday_var.get(),
                                self.contact_var.get(),
                                self.course_name_var.get(),
                                self.address_entry.get("1.0", END),
                                self.roll_var.get()))

                connect.commit()
                messagebox.showinfo("Success", "Student updated successfully", parent=self.root)
                self.show_students()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    #####################
    # delete course data
    def delete(self):
        connect = sqlite3.connect(database="rms.db")
        cursor = connect.cursor()
        try:
            cursor.execute("SELECT * FROM student WHERE roll=?", (self.roll_var.get(),))
            row = cursor.fetchone()
            if row is None:
                messagebox.showerror("Error", "Select student from list", parent=self.root)
            else:
                cursor.execute("DELETE FROM student WHERE roll=?", (self.roll_var.get(),))
                connect.commit()
                messagebox.showinfo("Success", "Student deleted successfully", parent=self.root)
                self.show_students()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    #####################
    # search course data
    def search(self):
        connect = sqlite3.connect(database="rms.db")
        cursor = connect.cursor()
        try:
            cursor.execute("SELECT * FROM student WHERE roll LIKE ?", ('%' + self.search_var.get() + '%',))
            rows = cursor.fetchall()
            if rows:
                self.CourseTable.delete(*self.CourseTable.get_children())
                for row in rows:
                    self.CourseTable.insert('', END, values=row)
            else:
                messagebox.showerror("Error", "No record found", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")


if __name__ == "__main__":
    root = Tk()
    student_class(root)
    root.mainloop()
