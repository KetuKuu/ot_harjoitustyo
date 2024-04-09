from tkinter import Tk
from ui.login_view_copy import LoginView


def main():
    window = Tk()
    window.title("Noki")

    ui_view = LoginView(window)
    ui_view.create_widgets()

    window.mainloop()


if __name__ == "__main__":
    main()