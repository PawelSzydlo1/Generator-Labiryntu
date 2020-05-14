
from tkinter import *
from Labirynt import Labirynt

class Interface():

    def wywolaj(self):

        self.Lab=Labirynt(int(self.widthMaze.get()),int(self.heightMaze.get()),self.okno,self.xStart,self.yStart,self.xKoniec,self.yKoniec);
        self.okno.quit()



    def __init__(self):
        self.okno = Tk()
        self.okno.title("Generator Labiryntu")
        self.okno.geometry("800x800")
        self.okno.resizable(width=False, height=False)
        self.wSiatki=20
        self.xStart = 200
        self.yStart = 200
        self.xKoniec = 800 - self.wSiatki + 1
        self.yKoniec = 800 - self.wSiatki + 1

        label =Label(self.okno,font = ("Times New Roman", 12),text="Witam w moim projekcie pt. \"Labirynt\"\nPodaj wymiary labiryntu:",justify=CENTER )
        label.pack(side=TOP)
        self.frame=Frame(self.okno)

        PodajN = Label(self.frame, font=("Times New Roman", 12), text="Podaj szerokość (1-30):")
        PodajN.pack(side=LEFT)

        self.widthMaze = Entry(self.frame, width=10, font=("Times New Roman", 12))
        self.widthMaze.pack(side=LEFT)

        self.heightMaze = Entry(self.frame, width=10, font=("Times New Roman", 12))
        self.heightMaze.pack(side=RIGHT)

        PodajM = Label(self.frame, font=("Times New Roman", 12), text="Podaj wysokość(1-30):")
        PodajM.pack(side=RIGHT)

        self.frame.pack(side=TOP)

        Przyciskok = Button(self.okno, text="ok", width=20, command=self.przycisk)
        Przyciskok.pack(side=TOP)

        self.wspolFrame=Frame(self.okno)
        PodajWspolrzedne = Label(self.wspolFrame, font=("Times New Roman", 12),text="Kliknij  lewym(Start) i prawym (Koniec) przyciskiem myszy")
        PodajWspolrzedne.pack(side=TOP)



        StartWspolrzedne = Label(self.wspolFrame,text="Start:")
        StartWspolrzedne.pack(side=LEFT)
        self.value1=StringVar()
        StartWspolrzedne1=Label(self.wspolFrame,textvariable=self.value1)
        StartWspolrzedne1.pack(side=LEFT)

        self.value2 = StringVar()
        KoniecWspolrzedne1 = Label(self.wspolFrame, textvariable=self.value2)
        KoniecWspolrzedne1.pack(side=RIGHT)

        KoniecWspolrzedne = Label(self.wspolFrame,text="Koniec:")
        KoniecWspolrzedne.pack(side=RIGHT)

        self.wspolFrame.pack(side=TOP)







        self.okno.mainloop()

    def lewyPrzycisk(self, event):
        self.xStart = int(event.x / self.wSiatki) * self.wSiatki
        self.yStart = int(event.y / self.wSiatki) * self.wSiatki
        self.canvas.create_rectangle((self.xStart + 1, self.yStart + 1, self.xStart + self.wSiatki - 1, self.yStart + self.wSiatki - 1),
            fill="#00ff00", width=0)
        self.value1.set((self.xStart-self.wSiatki,self.yStart-self.wSiatki))
        self.okno.update()

    def prawyPrzycisk(self, event):
        self.xKoniec = int(event.x / self.wSiatki) * self.wSiatki
        self.yKoniec = int(event.y / self.wSiatki) * self.wSiatki
        self.canvas.create_rectangle((self.xKoniec + 1, self.yKoniec + 1, self.xKoniec + self.wSiatki - 1, self.yKoniec + self.wSiatki - 1),
            fill="#0000ff", width=0)
        self.value2.set((self.xKoniec-self.wSiatki,self.yKoniec-self.wSiatki))
        self.okno.update()
    def przycisk(self):
        self.canvas = Canvas(self.okno, width=(int(self.widthMaze.get()) + 2) * self.wSiatki,height=(int(self.heightMaze.get()) + 2) * self.wSiatki)
        self.canvas.pack(side=BOTTOM)
        self.buduj_Siatke(int(self.widthMaze.get()),int(self.heightMaze.get()))
        self.canvas.bind("<Button-1>", self.lewyPrzycisk)
        self.canvas.bind("<Button-3>", self.prawyPrzycisk)



        PrzyciskNowy = Button(self.okno, text="Nowy Labirynt", width=20, command=self.wywolaj)
        PrzyciskNowy.pack(side=BOTTOM)



    def buduj_Siatke(self,M,N):
        y=self.wSiatki
        for i in range(1,M+1):
            x=self.wSiatki

            for j in range(1,N+1):
                self.canvas.create_line((x, y, x+self.wSiatki, y), width = 2)
                self.canvas.create_line((x + self.wSiatki, y, x+self.wSiatki, y+ self.wSiatki), width = 2)
                self.canvas.create_line((x , y+ self.wSiatki, x+self.wSiatki, y+ self.wSiatki), width = 2)
                self.canvas.create_line((x, y, x, y+ self.wSiatki), width = 2)
                self.okno.update()
                x=x+self.wSiatki
            y=y+self.wSiatki


i=Interface()