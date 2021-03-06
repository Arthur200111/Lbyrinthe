import tkinter as tk


class Labyrinthe:
    def __init__(self, lab, coords):
        
        self.lab = lab
        self.height = len(lab)
        self.length = len(lab[0])
        self.place = "0"
        self.X = coords[0]
        self.Y = coords[1]

        self.deplacement()


    def deplacement(self):
        self.lab[self.Y][self.X] = "T"
        for line in self.lab :
            print(" ".join(line))
        self.lab[self.Y][self.X] = "0"
        self.movement = input()
        self.check_next(self.movement)
        self.deplacement()


    def check_next(self, movement):
        if movement == 'z':
            if self.lab[self.Y - 1][self.X] != "X":
                self.Y -= 1
        elif movement == 's':
            if self.lab[self.Y + 1][self.X] != "X":
                self.Y += 1
        elif movement == 'q':
            if self.lab[self.Y][self.X - 1] != "X":
                self.X -= 1
        elif movement == 'd':
            if self.lab[self.Y][self.X + 1] != "X":
                self.X += 1
        
        if self.lab[self.Y][self.X] == "E":
            self.win()


    def win(self):
        print("Gagné")


coord = [4, 1]
liste = [
    ["X", "E", "X", "X", "X", "X"],
    ["X", "0", "0", "0", "0", "X"],
    ["X", "0", "0", "X", "0", "X"],
    ["X", "X", "X", "X", "X", "X"]
]

Labyrinthe(liste, coord)
