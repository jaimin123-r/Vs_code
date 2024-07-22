# from tkinter import *


# root=Tk()
# root.title("My GUI")
# root.geometry("500x500")
# # root.wm_iconbitmap("icon.ico")
# root.resizable(False,False)



# root.mainloop()

import tkinter as tk
from tkinter import messagebox

class GatePassForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Gate Pass Form")
        self.root.geometry("400x500")
        self.root.resizable(False, False)

        self.id_var = tk.StringVar()
        self.name_var = tk.StringVar()
        self.mobile_var = tk.StringVar()
        self.allow_assest_var = tk.StringVar()
        self.come_from_var = tk.StringVar()
        self.no_of_person_var = tk.StringVar()
        self.to_meet_var = tk.StringVar()
        self.purpose_var = tk.StringVar()
        self.in_date_var = tk.StringVar()
        self.out_date_var = tk.StringVar()
        self.in_time_var = tk.StringVar()
        self.out_time_var = tk.StringVar()
        self.gatepass_number_var = tk.StringVar()

        self.create_form()

    def create_form(self):
        # Labels
        tk.Label(self.root, text="ID:").grid(row=0, column=0, sticky="w")
        tk.Label(self.root, text="Name:").grid(row=1, column=0, sticky="w")
        tk.Label(self.root, text="Mobile Number:").grid(row=2, column=0, sticky="w")
        tk.Label(self.root, text="Allow Assest:").grid(row=3, column=0, sticky="w")
        tk.Label(self.root, text="Come From:").grid(row=4, column=0, sticky="w")
        tk.Label(self.root, text="No of Person:").grid(row=5, column=0, sticky="w")
        tk.Label(self.root, text="To Meet:").grid(row=6, column=0, sticky="w")
        tk.Label(self.root, text="Purpose:").grid(row=7, column=0, sticky="w")
        tk.Label(self.root, text="In Date:").grid(row=8, column=0, sticky="w")
        tk.Label(self.root, text="Out Date:").grid(row=9, column=0, sticky="w")
        tk.Label(self.root, text="In Time:").grid(row=10, column=0, sticky="w")
        tk.Label(self.root, text="Out Time:").grid(row=11, column=0, sticky="w")
        tk.Label(self.root, text="Gatepass Number:").grid(row=12, column=0, sticky="w")

        # Entry Fields
        tk.Entry(self.root, textvariable=self.id_var, state="disabled").grid(row=0, column=1)
        tk.Entry(self.root, textvariable=self.name_var).grid(row=1, column=1)
        tk.Entry(self.root, textvariable=self.mobile_var).grid(row=2, column=1)
        tk.Entry(self.root, textvariable=self.allow_assest_var).grid(row=3, column=1)
        tk.Entry(self.root, textvariable=self.come_from_var).grid(row=4, column=1)
        tk.Entry(self.root, textvariable=self.no_of_person_var).grid(row=5, column=1)
        tk.Entry(self.root, textvariable=self.to_meet_var).grid(row=6, column=1)
        tk.Entry(self.root, textvariable=self.purpose_var).grid(row=7, column=1)
        tk.Entry(self.root, textvariable=self.in_date_var).grid(row=8, column=1)
        tk.Entry(self.root, textvariable=self.out_date_var).grid(row=9, column=1)
        tk.Entry(self.root, textvariable=self.in_time_var).grid(row=10, column=1)
        tk.Entry(self.root, textvariable=self.out_time_var).grid(row=11, column=1)
        tk.Entry(self.root, textvariable=self.gatepass_number_var).grid(row=12, column=1)

        # Submit Button
        tk.Button(self.root, text="Submit", command=self.submit_form).grid(row=13, column=0, columnspan=2, pady=10)

    def validate_form(self):
        # Add your validation logic here
        if not self.name_var.get():
            messagebox.showerror("Error", "Please enter Name")
            return False
        # Similarly, add validations for other fields
        return True

    def submit_form(self):
        if self.validate_form():
            # Submit logic goes here
            messagebox.showinfo("Success", "Form submitted successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = GatePassForm(root)
    root.mainloop()
