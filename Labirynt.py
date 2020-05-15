from tkinter import *
import time
import random

class Labirynt():
    def wywolaj(self):
        self.okno.destroy()

    def __init__(self, M=1, N=1,rodzic=None,xStart=None,yStart=None,xKoniec=None,yKoniec=None):
        self.okno = Toplevel(rodzic)
        self.okno.title("GL - Wizualizacja")
        self.okno.geometry("800x800")
        self.okno.resizable(width=False, height=False)
        self.M=M
        self.N=N
        self.grid=[]
        self.stack=[]
        self.visited=[]
        self.solution={}
        self.wSiatki=20  #szerokośc korytarzu
        self.a=0
        self.b=0
        self.xStart=xStart
        self.yStart=yStart
        self.xKoniec=xKoniec
        self.yKoniec=yKoniec
        self.x=0
        self.y=0

        PrzyciskClose = Button(self.okno, text="Close Project", width=20, command=self.wywolaj)
        PrzyciskClose.pack(side=BOTTOM)

        self.canvas = Canvas(self.okno,width=(M+2)*self.wSiatki, height=(N+2)*self.wSiatki,bg="blue")
        self.canvas.place(x=(800-(M+2)*self.wSiatki)/2, y=100)



        label = Label(self.okno, font=("Times New Roman", 12), text="Labirynt", justify=CENTER)
        label.pack(side=TOP)

        self.buduj_Siatke(M,N)


        self.carve_out_maze(self.xStart,self.yStart)
        self.plot_route_back(self.xKoniec,self.yKoniec,self.xStart,self.yStart)

        self.Postac=self.canvas.create_oval((xStart+3, yStart+3, xStart + self.wSiatki-6, yStart + self.wSiatki-6), fill="#000000")
        self.okno.update()
        self.x2 = xStart
        self.y2 = yStart

        self.okno.bind("<KeyPress-Left>", lambda e: self.left(e))
        self.okno.bind("<KeyPress-Right>", lambda e: self.right(e))
        self.okno.bind("<KeyPress-Up>", lambda e: self.up(e))
        self.okno.bind("<KeyPress-Down>", lambda e: self.down(e))

        print("Kurde koniec")
        self.okno.mainloop()

    def up(self,event):

        if(self.canvas.find_overlapping(self.x2 + 2, self.y2 - 2, self.x2 + 4, self.y2 + 2) == ()):

            print("up",self.x2,self.y2)
            self.x=0
            self.y=-self.wSiatki
            self.x2=self.x2+self.x
            self.y2=self.y2+self.y
            self.canvas.move(self.Postac, self.x , self.y )

    def down(self,event):

        if (self.canvas.find_overlapping(self.x2 + 2, self.y2 + self.wSiatki + 2, self.x2 + 4, self.y2 + self.wSiatki - 2) == ()):

            print("down",self.x2,self.y2)
            self.x=0
            self.y=self.wSiatki
            self.x2 = self.x2 + self.x
            self.y2 = self.y2 + self.y
            self.canvas.move(self.Postac, self.x , self.y )

    def left(self,event):

        if (self.canvas.find_overlapping(self.x2 - 2, self.y2 + 4, self.x2 + 2, self.y2 + 6) == ()):

            print("l",self.x2,self.y2)
            self.x=-self.wSiatki
            self.y=0
            self.x2 = self.x2 + self.x
            self.y2 = self.y2 + self.y
            self.canvas.move(self.Postac, self.x , self.y )

    def right(self,event):

        if (self.canvas.find_overlapping(self.x2 + self.wSiatki + 2, self.y2 + 2, self.x2 + self.wSiatki - 2, self.y2 + 4) == ()):

            print("r",self.x2,self.y2)
            self.x=self.wSiatki
            self.y=0
            self.x2 = self.x2 + self.x
            self.y2 = self.y2 + self.y
            self.canvas.move(self.Postac, self.x, self.y)


    def buduj_Siatke(self,M,N):
        y=self.wSiatki
        for i in range(1,M+1):
            x=self.wSiatki

            for j in range(1,N+1):
                if(self.canvas.find_overlapping(x+2,y-2,x+4,y+2)==()):
                    #print("gora")
                    self.canvas.create_line((x, y, x+self.wSiatki, y), width = 2)

                if (self.canvas.find_overlapping(x + self.wSiatki+2, y+2,x + self.wSiatki-2, y+4)==()):
                    #print("pra")
                    self.canvas.create_line((x + self.wSiatki, y, x+self.wSiatki, y+ self.wSiatki), width = 2)
                if (self.canvas.find_overlapping(x+2 , y+ self.wSiatki+2,x+4 , y+ self.wSiatki-2)==()):
                    #print("dol")
                    self.canvas.create_line((x , y+ self.wSiatki, x+self.wSiatki, y+ self.wSiatki), width = 2)
                if (self.canvas.find_overlapping(x-2 , y+4,x+2 , y+6)==()):
                    #print("le")
                    self.canvas.create_line((x, y, x, y+ self.wSiatki), width = 2)
                self.okno.update()
                self.grid.append((x,y))
                x=x+self.wSiatki
            y=y+self.wSiatki


    def carve_out_maze(self,x, y):
        self.single_cell(x, y)
        self.stack.append((x, y))
        self.visited.append((x, y))
        while len(self.stack) > 0:
            cell = []
            if (x + self.wSiatki, y) not in self.visited and (x + self.wSiatki, y) in self.grid:
                cell.append("right")  # if yes add to cell list

            if (x - self.wSiatki, y) not in self.visited and (x - self.wSiatki, y) in self.grid:
                cell.append("left")

            if (x, y + self.wSiatki) not in self.visited and (x, y + self.wSiatki) in self.grid:
                cell.append("down")

            if (x, y - self.wSiatki) not in self.visited and (x, y - self.wSiatki) in self.grid:
                cell.append("up")

            if len(cell) > 0:
                cell_chosen = (random.choice(cell))

                if cell_chosen == "right":
                    self.push_right(x, y)
                    self.solution[(x + self.wSiatki, y)] = x, y
                    x = x + self.wSiatki
                    self.visited.append((x, y))
                    self.stack.append((x, y))

                elif cell_chosen == "left":
                    self.push_left(x, y)
                    self.solution[(x - self.wSiatki, y)] = x, y
                    x = x - self.wSiatki
                    self.visited.append((x, y))
                    self.stack.append((x, y))

                elif cell_chosen == "down":
                    self.push_down(x, y)
                    self.solution[(x, y + self.wSiatki)] = x, y
                    y = y + self.wSiatki
                    self.visited.append((x, y))
                    self.stack.append((x, y))

                elif cell_chosen == "up":
                    self.push_up(x, y)
                    self.solution[(x, y - self.wSiatki)] = x, y
                    y = y - self.wSiatki
                    self.visited.append((x, y))
                    self.stack.append((x, y))
            else:
                x, y = self.stack.pop()
                self.single_cell(x, y)
                self.backtracking_cell(x, y)




    def push_up(self,x,y):

        tym=self.canvas.find_overlapping(x+2,y-2,x+4,y+2)
        self.canvas.delete(tym)

        self.okno.update()
    def push_down(self,x,y):
        tym = self.canvas.find_overlapping(x+2 , y+ self.wSiatki+2,x+4 , y+ self.wSiatki-2)
        self.canvas.delete(tym)

        self.okno.update()
    def push_left(self, x, y):
        tym = self.canvas.find_overlapping(x-2 , y+4,x+2 , y+6)
        self.canvas.delete(tym)

        self.okno.update()
    def push_right(self, x, y):
        tym = self.canvas.find_overlapping(x + self.wSiatki+2, y+2,x + self.wSiatki-2, y+4)
        self.canvas.delete(tym)


        self.okno.update()
    def single_cell(self,x,y):
        #self.canvas.create_rectangle((x + 1, y + 1, x + self.wSiatki - 1, y + self.wSiatki - 1), fill="#0000ff", width = 0)
        self.okno.update()
    def backtracking_cell(self,x,y):
        #self.canvas.create_rectangle((x + 1, y + 1, x + self.wSiatki - 1, y + self.wSiatki - 1), fill="#ff0000", width = 0)
        self.okno.update()
    def solution_cell(self,x,y):
        self.canvas.create_oval((x + 8, y + 8, x + self.wSiatki - 8, y + self.wSiatki -8), fill="#00ff00", width = 0)
        self.okno.update()
    def plot_route_back(self,x,y,x1,x2):
        self.solution_cell(x,y)
        while (x,y)!=(x1,x2):
            x,y=self.solution[x,y]
            self.solution_cell(x,y)


