from tkinter import Toplevel
from tkinter import Label
from tkinter import Button
from tkinter import Canvas
from tkinter import BOTTOM, TOP, CENTER
from stale import *
from HelperFunction import *
import random


class Maze:
    grid = []
    solution = {}

    def __init__(self, m=1, n=1, parent=None, x_start=None, y_start=None, x_finish=None, y_finish=None):
        self.window = Toplevel(parent)
        self.canvas = Canvas(self.window, width=(m + 2) * WIDTH_HOL, height=(n + 2) * WIDTH_HOL, bg="blue")
        self.initialize_window(m)

        self.draw_maze(m, n)

        self.create_maze(x_start, y_start)
        self.draw_solution_plot(x_finish, y_finish, x_start, y_start)
        self.hero = self.canvas.create_oval(
            (x_start + 3, y_start + 3, x_start + WIDTH_HOL - 6, y_start + WIDTH_HOL - 6), fill="#000000")
        self.x_hero = x_start
        self.y_hero = y_start

        self.window.mainloop()

    def initialize_window(self, m):
        self.window.title("Maze")
        self.window.geometry("{}x{}".format(WIDTH, HEIGHT))
        self.window.resizable(width=False, height=False)
        self.window.bind("<KeyPress-Left>", lambda _: self.hero_left())
        self.window.bind("<KeyPress-Right>", lambda _: self.hero_right())
        self.window.bind("<KeyPress-Up>", lambda _: self.hero_up())
        self.window.bind("<KeyPress-Down>", lambda _: self.hero_down())
        button_close = Button(self.window, text="Close Project", width=20, command=self.close_maze)
        button_close.pack(side=BOTTOM)
        self.canvas.place(x=(WIDTH - (m + 2) * WIDTH_HOL) / 2, y=HEIGHT / 8)
        label = Label(self.window, text="Labirynt", justify=CENTER)
        label.pack(side=TOP)

    def check_coordinate_hero(self, a, b, a1, b1):
        if self.canvas.find_overlapping(self.x_hero + a, self.y_hero + b, self.x_hero + a1, self.y_hero + b1) == ():
            return True
        else:
            return False

    def hero_up(self):
        if self.check_coordinate_hero(2, -2, 4, 2):
            self.y_hero -= WIDTH_HOL
            self.canvas.move(self.hero, 0, - WIDTH_HOL)

    def hero_down(self):
        if self.check_coordinate_hero(2, WIDTH_HOL + 2, 4, WIDTH_HOL - 2):
            self.y_hero += WIDTH_HOL
            self.canvas.move(self.hero, 0, WIDTH_HOL)

    def hero_left(self):
        if self.check_coordinate_hero(-2, 4, 2, 6):
            self.x_hero -= WIDTH_HOL
            self.canvas.move(self.hero, - WIDTH_HOL, 0)

    def hero_right(self):
        if self.check_coordinate_hero(WIDTH_HOL + 2, 2, WIDTH_HOL - 2, 4):
            self.x_hero += WIDTH_HOL
            self.canvas.move(self.hero, WIDTH_HOL, 0)

    def draw_maze(self, m, n):
        y = WIDTH_HOL
        for i in range(1, m + 1):
            x = WIDTH_HOL

            for j in range(1, n + 1):
                if check_coordinate_line(self.canvas, x, y, 2, - 2, 4, 2):
                    self.canvas.create_line((x, y, x + WIDTH_HOL, y), width=2)
                if check_coordinate_line(self.canvas, x, y, WIDTH_HOL + 2, 2, WIDTH_HOL - 2, 4):
                    self.canvas.create_line((x + WIDTH_HOL, y, x + WIDTH_HOL, y + WIDTH_HOL), width=2)
                if check_coordinate_line(self.canvas, x, y, 2, WIDTH_HOL + 2, 4, WIDTH_HOL - 2):
                    self.canvas.create_line((x, y + WIDTH_HOL, x + WIDTH_HOL, y + WIDTH_HOL), width=2)
                if check_coordinate_line(self.canvas, x, y, - 2, 4, 2, 6):
                    self.canvas.create_line((x, y, x, y + WIDTH_HOL), width=2)
                self.window.update()
                self.grid.append((x, y))
                x = x + WIDTH_HOL
            y = y + WIDTH_HOL

    def create_maze(self, x, y):
        stack = [(x, y)]
        visited = [(x, y)]
        while len(stack) > 0:
            cell = []
            if (x + WIDTH_HOL, y) not in visited and (x + WIDTH_HOL, y) in self.grid:
                cell.append("right")

            if (x - WIDTH_HOL, y) not in visited and (x - WIDTH_HOL, y) in self.grid:
                cell.append("left")

            if (x, y + WIDTH_HOL) not in visited and (x, y + WIDTH_HOL) in self.grid:
                cell.append("down")

            if (x, y - WIDTH_HOL) not in visited and (x, y - WIDTH_HOL) in self.grid:
                cell.append("up")

            if len(cell) > 0:
                cell_chosen = (random.choice(cell))

                if cell_chosen == "right":
                    self.clear_line(x + WIDTH_HOL + 2, y + 2, x + WIDTH_HOL - 2, y + 4)
                    self.solution[(x + WIDTH_HOL, y)] = x, y
                    x = x + WIDTH_HOL

                elif cell_chosen == "left":
                    self.clear_line(x - 2, y + 4, x + 2, y + 6)
                    self.solution[(x - WIDTH_HOL, y)] = x, y
                    x = x - WIDTH_HOL

                elif cell_chosen == "down":
                    self.clear_line(x + 2, y + WIDTH_HOL + 2, x + 4, y + WIDTH_HOL - 2)
                    self.solution[(x, y + WIDTH_HOL)] = x, y
                    y = y + WIDTH_HOL

                elif cell_chosen == "up":
                    self.clear_line(x + 2, y - 2, x + 4, y + 2)
                    self.solution[(x, y - WIDTH_HOL)] = x, y
                    y = y - WIDTH_HOL

                visited.append((x, y))
                stack.append((x, y))
            else:
                x, y = stack.pop()

    def clear_line(self, x1, y1, x2, y2):
        tym = self.canvas.find_overlapping(x1, y1, x2, y2)
        self.canvas.delete(tym)
        self.window.update()

    def draw_solution_cell(self, x, y, x_finish, y_finish):
        if x == x_finish and y == y_finish:
            self.canvas.create_rectangle((x + 6, y + 6, x + WIDTH_HOL - 6, y + WIDTH_HOL - 6), fill="#00ff00", width=0)
        else:
            self.canvas.create_oval((x + 8, y + 8, x + WIDTH_HOL - 8, y + WIDTH_HOL - 8), fill="#00ff00", width=0)
            self.window.update()

    def draw_solution_plot(self, x_finish, y_finish, x_start, y_start):
        x, y = x_finish, y_finish
        self.draw_solution_cell(x, y, x_finish, y_finish)
        while (x, y) != (x_start, y_start):
            x, y = self.solution[x, y]
            self.draw_solution_cell(x, y, x_finish, y_finish)

    def close_maze(self):
        self.window.destroy()
