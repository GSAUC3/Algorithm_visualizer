from tkinter import * 
from tkinter import ttk
from ttkbootstrap import *
from numpy import linspace, random, uint16 
import time 

class App:
    def __init__(self,root,title) -> None:
        self.root = root 
        self.root.title(title)
        self.root.geometry('805x440')
        ttk.Button(self.root,text = 'start sorting',command=self._start).grid(row=0,column=14)
        ttk.Button(self.root,text = 'shuffle',command=self._shuffle).grid(row=0,column=13)
        self.canvas = Canvas(self.root,width=800,height=405,highlightbackground='dodgerblue',
                             bg = 'black',highlightthickness=2)
        self.canvas.grid(row=1,columnspan=15)
        self.N = 50
        self.data = linspace(5,400,self.N)
        self._colors = ['dodgerblue' for _ in range(self.N)] 
        self._speed = 5/1000
        # colors  
        self._shuffle()

    def __reset_colors(self,color ='dodgerblue'):
        self._colors = [color for _ in range(self.N)] 

    def _shuffle(self):
        self.__reset_colors()
        random.shuffle(self.data)
        self._display(self._colors)

    def _display(self,array_color:list):
        g = self.N*0.01 # gap
        width = lambda x:(800-99*x)/self.N
        self.canvas.delete('all')
    
        for i in range(self.N):
            # self.canvas.create_rectangle(x0,y0,
            #                              x1,y1,
            # fill='blue')
            x0 = i*width(g)+i*g
            y0 = 0
            x1 = (i+1)*width(g)+i*g
            y1 = self.data[i]
            self.canvas.create_rectangle(x0,y0,x1,y1,fill=array_color[i])

        self.root.update_idletasks()

    def _start(self):
        for steps in range(self.N-1):
            a = self.N-1-steps
            for i in range(a):
                self._colors[i] = self._colors[i+1] = 'yellow'
                self._display(self._colors)
                time.sleep(self._speed)
                if self.data[i]>self.data[i+1]:
                    self._colors[:a+1] = ['dodgerblue']*(a+1)
                    self._colors[i] = self._colors[i+1] = 'red'
                    self._display(self._colors)
                    time.sleep(self._speed)
                    self.data[i],self.data[i+1]=self.data[i+1],self.data[i]
                    self._colors[i] = self._colors[i+1] = 'lime'
                    self._display(self._colors)
                    time.sleep(self._speed)
                self._colors[i] = self._colors[i+1] = 'dodgerblue'
            self._colors[a:] = ['green']*(self.N-a)
        self._display(self._colors)
        self.__reset_colors('green')
        self._display(self._colors)


        

if __name__ == '__main__':
    window = Style(theme = 'darkly').master 
    App(window,'Bubble sort')
    window.mainloop()