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
        self.window.geometry("540x900")
        self.window.title("Dashboard")
        self.window.config(bg="white")

        image = Image.open("./view/images/img.png")
        image = ImageTk.PhotoImage(image)

        Label(self.window, image=image).place(x=195, y=15)

        Button(self.window, font=font, width=width, bg=background_color, fg=foreground_color, text="Visit",
               command=self.visit_view).place(x=80, y=180)

        self.window.mainloop()
