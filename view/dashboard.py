from tkinter import *
from PIL import ImageTk, Image
from model.entity.payment import Payment
from view.visit_view import Visit

class DashboardView:
    def visit_view(self):
        ui = Visit()

    def payment_view(self):
        ui = Payment()

    def __init__(self):
        font = ("Arial", 18, "bold")
        width = 12
        background_color = "violet red"
        foreground_color = "white"

        y_dist = 60

        self.window = Tk()
        self.window.geometry("400x400")
        self.window.title("Dashboard")
        self.window.config(bg="white")

        image = Image.open("./view/images/img.png")
        image = ImageTk.PhotoImage(image)

        Label(self.window, image=image).place(x=100, y=15)

        Button(self.window, font=font, width=width, bg=background_color, fg=foreground_color, text="Visit",
               command=self.visit_view).place(x=108, y=250)
        Button(self.window, font=font, width=width, bg=background_color, fg=foreground_color, text="Payment",
               command=self.payment_view).place(x=108, y=250 + y_dist * 1)

        self.window.mainloop()
