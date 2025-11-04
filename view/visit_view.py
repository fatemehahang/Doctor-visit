from tkinter import *
from tkinter import messagebox
from controller.visit_controller import VisitController
from view.component.label_with_entry import LabelWithEntry
from view.component.table import Table

class Visit:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("1010x400")
        self.window.title("Doctor Visit")

        self.patient_id = LabelWithEntry(self.window, "id", 20, 20, data_type=IntVar, state="readonly")
        self.first_name = LabelWithEntry(self.window, "FirstName", 20, 60)
        self.last_name = LabelWithEntry(self.window, "LastName", 20, 100)
        self.phone_number = LabelWithEntry(self.window, "PhoneNumber", 20, 140)
        self.doctor_name = LabelWithEntry(self.window, "DoctorName", 20, 180)
        self.date_time = LabelWithEntry(self.window, "DateTime", 20, 220)
        self.description = LabelWithEntry(self.window, "Description", 20, 260)

        self.table = Table(
            self.window,
            ["Id", "first_name", "last_name", "phone_number", "doctor_name", "date_time", "description"],
            [40,100,100,100,100,100,160],
            275, 20,
            12,
            self.select_from_table
        )

        Button(self.window, text="Select patient", width=19, command=self.select_visit).place(x=100, y=300)
        Button(self.window, text="Refresh", width=7, command=self.refresh).place(x=20, y=300)
        Button(self.window, text="Save", width=7, command=self.save_click).place(x=20, y=340)
        Button(self.window, text="Edit", width=7, command=self.edit_click).place(x=100, y=340)
        Button(self.window, text="Delete", width=7, command=self.delete_click).place(x=180, y=340)
        self.reset_form()
        self.window.mainloop()

    def save_click(self):
        status = message = VisitController.save(self.first_name.get(), self.last_name.get(), self.phone_number.get(),
                                                self.doctor_name.get(), self.date_time.get(), self.description.get())
        if status:
            messagebox.showinfo("Success Save", message)
            self.reset_form()
        else:
            messagebox.showerror("Save Error", message)

    def edit_click(self):
        status = message = VisitController.update(self.patient_id.get(), self.first_name.get(), self.last_name.get(),
                                                  self.phone_number.get(), self.doctor_name.get(), self.date_time.get(),
                                                  self.description.get())
        if status:
            messagebox.showinfo("Success Edit", message)
            self.reset_form()
        else:
            messagebox.showerror("Edit Error", message)

    def delete_click(self):
        status = message = VisitController.delete(self.patient_id.get())
        if status:
            messagebox.showinfo("Success Delete", message)
            self.reset_form()
        else:
            messagebox.showerror("Delete Error", message)

    def reset_form(self):
        self.patient_id.clear()
        self.first_name.clear()
        self.last_name.clear()
        self.phone_number.clear()
        self.doctor_name.clear()
        self.date_time.clear()
        self.description.clear()
        status, visit_list = VisitController.find_all()
        self.table.refresh_table(visit_list)

    def select_from_table(self, selected_visit):
        if selected_visit:
            status, visit = VisitController.find_by_id(selected_visit[0])
            if status:
                visit = Visit(*selected_visit)
                self.patient_id.set(visit.patient_id)
                self.first_name.set(visit.first_name)
                self.last_name.set(visit.last_name)
                self.phone_number.set(visit.phone_number)
                self.doctor_name.set(visit.doctor_name)
                self.date_time.set(visit.date_time)
                self.description.set(visit.description)


    def select_visit(self):
        if self.patient_id.get():
            status, visit = VisitController.find_by_id(self.patient_id.get())
        else:
            messagebox.showerror("Select", "Select visit")

    def refresh(self):
        pass