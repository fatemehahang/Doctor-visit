from tkinter import *
from PIL import ImageTk, Image
from view.visit_view import Visit

class DashboardView:
    def visit_view(self):
        ui = Visit()

    def __init__(self):
        font = ("Arial", 18, "bold")
        width = 24
        background_color = "violet red"
        foreground_color = "white"

        y_dist = 60

        self.window = Tk()
        self.window.geometry("730x690")
        self.window.title("Dashboard")
        self.window.config(bg="white")

        image = Image.open("./view/images/img.jpeg")
        image = ImageTk.PhotoImage(image)

        Label(self.window, image=image).place(x=100, y=15)

        Button(self.window, font=font, width=width, bg=background_color, fg=foreground_color, text="Visit",
               command=self.visit_view).place(x=190, y=590)

        self.window.mainloop()
