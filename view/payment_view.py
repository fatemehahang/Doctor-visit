from view import *
from model.entity.payment import Payment
from controller.payment_controller import PaymentController

class PaymentView:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("1100x450")
        self.window.title("Payment View")

        self.payment_id = LabelWithEntry(self.window, "Id", 20, 20, data_type=IntVar, state="readonly")
        self.transaction_type = LabelWithEntry(self.window, "TransactType", 20, 60)
        self.payment_type = LabelWithEntry(self.window, "PaymentType", 20, 100)
        self.date_time = LabelWithEntry(self.window, "DateTime", 20, 140)
        self.payment_id = LabelWithEntry(self.window, "Customer", 20, 180, data_type=IntVar, state="readonly")
        self.total_amount = LabelWithEntry(self.window, "TotalAmount", 20, 220, data_type=IntVar)
        self.description = LabelWithEntry(self.window, "Description", 20, 260)
        self.table = Table(
            self.window,
            ["Id", "TransactType", "PaymentType", "DateTime", "CustomerId", "TotalAmount", "EmployeeId", "Description"],
            [40, 80, 60, 100, 130, 80, 130, 180],
            270, 20,
            18,
            self.select_from_table
        )
        Button(self.window, text="Select Payment", width=19, command=self.select_payment).place(x=20, y=340)
        Button(self.window, text="Refresh", width=7, command=self.refresh).place(x=180, y=340)
        Button(self.window, text="Save", width=7, command=self.save_click).place(x=20, y=380)
        Button(self.window, text="Edit", width=7, command=self.edit_click).place(x=100, y=380)
        Button(self.window, text="Delete", width=7, command=self.delete_click).place(x=180, y=380)
        self.reset_form()
        self.window.mainloop()

    def save_click(self):
        status, message = PaymentController.save(self.transaction_type.get(), self.payment_type.get(),
                                                 self.date_time.get(), self.payment_id.get(),
                                                 self.total_amount.get(),self.description.get())
        if status:
            messagebox.showinfo("Payment Info Save", message)
            self.reset_form()
        else:
            messagebox.showerror("Payment Info Save Error", message)

    def edit_click(self):
        status, message = PaymentController.update(self.payment_id.get(), self.transaction_type.get(),
                                                   self.payment_type.get(),
                                                   self.date_time.get(), self.payment_id.get(),
                                                   self.total_amount.get(),self.description.get())
        if status:
            messagebox.showinfo("Payment Info Update", message)
            self.reset_form()
        else:
            messagebox.showerror("Payment Info Update Error", message)

    def delete_click(self):
        status, message = PaymentController.delete(self.payment_id.get())
        if status:
            messagebox.showinfo("Payment Info Delete", message)
            self.reset_form()
        else:
            messagebox.showerror("Payment Info Delete Error", message)

    def reset_form(self):
        self.payment_id.clear()
        self.transaction_type.clear()
        self.payment_type.clear()
        self.date_time.clear()
        self.payment_id.clear()
        self.total_amount.clear()
        self.description.clear()
        status, payment_list = PaymentController.find_all()
        self.table.refresh_table(payment_list)

    def select_from_table(self, selected_payment):

        if selected_payment:
            status, payment = PaymentController.find_by_id(selected_payment[0])
            if status:
                payment = Payment(*selected_payment)
                self.payment_id.set(payment.payment_id)
                self.transaction_type.set(payment.transaction_type)
                self.payment_type.set(payment.payment_type)
                self.date_time.set(payment.date_time)
                self.payment_id.set(payment.patient_id)
                self.total_amount.set(payment.total_amount)
                self.description.set(payment.description)

    def select_payment(self):
        if self.payment_id.get():
            status, payment = PaymentController.find_by_id(self.payment_id.get())
        else:
            messagebox.showerror("Select", "Select Payment")

    def refresh(self):
        pass