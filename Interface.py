from tkinter import Tk
from tkinter import Label, Frame, Button, Entry, Canvas
from tkinter import StringVar
from tkinter import BOTTOM, TOP, CENTER, LEFT, RIGHT
from Labirynt import Maze
from stale import *
from HelperFunction import *


class Interface:

    def play_maze(self):
        """
        Obsłyga przycisku New Button
        """

        Maze(self.height_maze, self.width_maze, self.window, self.x_start, self.y_start,
             self.x_finish, self.y_finish)
        self.window.quit()

    def __init__(self):
        self.window = Tk()
        self.window.title("Generator Labiryntu")
        self.window.geometry("{}x{}".format(WIDTH, HEIGHT))
        self.window.resizable(width=False, height=False)

        self.width_maze = 0
        self.height_maze = 0
        self.x_finish = 0
        self.y_finish = 0
        self.x_start = 0
        self.y_start = 0
        self.iter = 1

        self.warning = StringVar("")
        warning_label = Label(self.window, textvariable=self.warning, font=("Times New Roman", 14))
        warning_label.pack(side=TOP)
        label = Label(self.window, font=("Times New Roman", 12),
                      text="Witam w moim projekcie pt. \"Labirynt\"\nPodaj wymiary labiryntu:", justify=CENTER)
        label.pack(side=TOP)
        self.frame = Frame(self.window)

        n_label = Label(self.frame, font=("Times New Roman", 12), text="Podaj szerokość (1-30):")
        n_label.pack(side=LEFT)

        self.width_maze_entry = Entry(self.frame, width=10, font=("Times New Roman", 12))
        self.width_maze_entry.pack(side=LEFT)

        self.height_maze_entry = Entry(self.frame, width=10, font=("Times New Roman", 12))
        self.height_maze_entry.pack(side=RIGHT)

        m_label = Label(self.frame, font=("Times New Roman", 12), text="Podaj wysokość(1-30):")
        m_label.pack(side=RIGHT)

        self.frame.pack(side=TOP)

        button_ok = Button(self.window, text="ok", width=20, command=self.button_action)
        button_ok.pack(side=TOP)

        self.coordinate_frame = Frame(self.window)
        get_coordinate_label = Label(self.coordinate_frame, font=("Times New Roman", 12),
                                     text="Kliknij  lewym(Start) i prawym (Koniec) przyciskiem myszy")
        get_coordinate_label.pack(side=TOP)

        start_coordinate_label = Label(self.coordinate_frame, text="Start:")
        start_coordinate_label.pack(side=LEFT)
        self.chosen_start_coordinate = StringVar()

        start_value_label = Label(self.coordinate_frame, textvariable=self.chosen_start_coordinate)
        start_value_label.pack(side=LEFT)

        self.value2 = StringVar()
        finish_coordinate_label = Label(self.coordinate_frame, textvariable=self.value2)
        finish_coordinate_label.pack(side=RIGHT)

        finish_value_label = Label(self.coordinate_frame, text="Finish:")
        finish_value_label.pack(side=RIGHT)

        self.coordinate_frame.pack(side=TOP)

        self.window.mainloop()

    def left_click_mouse(self, event):
        """
        Obsługa lewego przycisku myszy
        """
        if event.x < WIDTH_HOL or event.x > self.canvas.winfo_width() - WIDTH_HOL - 3  \
                or event.y < WIDTH_HOL or event.y > self.canvas.winfo_height() - WIDTH_HOL - 3:
            self.warning.set("Wyszedłes poza labirynt")
            self.window.update()
        else:
            self.x_start = int(event.x / WIDTH_HOL) * WIDTH_HOL
            self.y_start = int(event.y / WIDTH_HOL) * WIDTH_HOL
            self.canvas.create_rectangle(
                (self.x_start + 1, self.y_start + 1, self.x_start + WIDTH_HOL - 1, self.y_start + WIDTH_HOL - 1),
                fill="#00ff00", width=0)
            self.chosen_start_coordinate.set((self.x_start - WIDTH_HOL, self.y_start - WIDTH_HOL))
            self.window.update()

    def right_click_mouse(self, event):
        """
        Obsługa prawego przycisku myszy
        """
        if event.x < WIDTH_HOL or event.x > self.canvas.winfo_width() - WIDTH_HOL - 3 \
                or event.y < WIDTH_HOL or event.y > self.canvas.winfo_height() - WIDTH_HOL - 3:
            self.warning.set("Wyszedłes poza labirynt")
            self.window.update()
        else:
            self.x_finish = int(event.x / WIDTH_HOL) * WIDTH_HOL
            self.y_finish = int(event.y / WIDTH_HOL) * WIDTH_HOL

            self.canvas.create_rectangle(
                (self.x_finish + 1, self.y_finish + 1, self.x_finish + WIDTH_HOL - 1, self.y_finish + WIDTH_HOL - 1),
                fill="#0000ff", width=0)
            self.value2.set((self.x_finish - WIDTH_HOL, self.y_finish - WIDTH_HOL))
            self.window.update()

    def input_is_valid(self):
        """
        Sprawdzenie czy zostały podane wymiary labiryntu
        """
        if self.width_maze_entry.get() == '' or self.height_maze_entry.get() == '':
            self.warning.set("Nie podałeś wartości")
            self.window.update()
            return False

        self.width_maze = int(self.width_maze_entry.get())
        self.height_maze = int(self.height_maze_entry.get())
        if 31 > self.width_maze > 0 and 31 > self.height_maze > 0:
            return True

        self.warning.set("Podałeś złe wartości")
        self.window.update()
        return False

    def button_action(self):
        """
        Obsługa przycisku ok
        """
        if self.input_is_valid() and self.iter == 1:
            down_frame = Frame(self.window)
            self.canvas = Canvas(down_frame, width=(self.width_maze + 2) * WIDTH_HOL,
                                 height=(self.height_maze + 2) * WIDTH_HOL)
            self.canvas.pack(side=BOTTOM)
            self.draw_maze(self.height_maze, self.width_maze)
            self.canvas.bind("<Button-1>", self.left_click_mouse)
            self.canvas.bind("<Button-3>", self.right_click_mouse)

            new_button = Button(down_frame, text="NEW MAZE", width=20, command=self.play_maze)

            down_frame.pack(side=BOTTOM)
            new_button.pack(side=BOTTOM)
            self.iter += 1

    def draw_maze(self, m, n):
        """
        Rysowanie pustej siatki  o zadanych wymiarach
        """
        y = WIDTH_HOL
        for a in range(1, m + 1):
            x = WIDTH_HOL

            for b in range(1, n + 1):
                if check_coordinate_line(self.canvas, x, y, 2, - 2, 4, 2):
                    self.canvas.create_line((x, y, x + WIDTH_HOL, y), width=2)
                if check_coordinate_line(self.canvas, x, y, WIDTH_HOL + 2, 2, WIDTH_HOL - 2, 4):
                    self.canvas.create_line((x + WIDTH_HOL, y, x + WIDTH_HOL, y + WIDTH_HOL), width=2)
                if check_coordinate_line(self.canvas, x, y, 2, WIDTH_HOL + 2, 4, WIDTH_HOL - 2):
                    self.canvas.create_line((x, y + WIDTH_HOL, x + WIDTH_HOL, y + WIDTH_HOL), width=2)
                if check_coordinate_line(self.canvas, x, y, - 2, 4, 2, 6):
                    self.canvas.create_line((x, y, x, y + WIDTH_HOL), width=2)
                self.window.update()
                x = x + WIDTH_HOL
            y = y + WIDTH_HOL


if __name__ == '__main__':
    i = Interface()
