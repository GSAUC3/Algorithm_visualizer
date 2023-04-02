from tkinter import * 
from tkinter import ttk,messagebox
from ttkbootstrap import *   
from numpy import random,linspace,uint16 
import time

class window: 
    sort_names = ['bubble','insertion','selection',
                               'merge','quick']
    sorts = {k:False for k in sort_names}
    buttons:list

    def __init__(self,root,title) -> None:
        self.root = root 
        self.root.title(title)
        #restricting window from resizing
        self.root.resizable(width=0,height=0) 
        # _______________BUttons___________________
        bubble_sort_btn = ttk.Button(self.root, text='Bubble Sort', style='info.TButton', padding=5, width=15,
                              command=self.bubble)
        bubble_sort_btn.grid(column=0, row=1, padx=5, pady=5)
        insertion_sort_btn = ttk.Button(self.root, text='Insertion Sort', style='info.TButton', padding=5, width=15,
                            command=self.insertion)
        insertion_sort_btn.grid(column=1, row=1, padx=5, pady=5)
        selection_sort_btn = ttk.Button(self.root, text='Selection Sort', style='info.TButton', padding=5, width=15,
                            command=self.selection)
        selection_sort_btn.grid(column=2, row=1, padx=5, pady=5)
        merge_sort_btn = ttk.Button(self.root, text='Merge Sort', style='info.TButton', padding=5, width=15,
                            command=self.merge)
        merge_sort_btn.grid(column=3, row=1, padx=5, pady=5)         
        quick_sort_btn = ttk.Button(self.root, text='Quick Sort', style='info.TButton', padding=5, width=15,
                            command=self.quick)
        quick_sort_btn.grid(column=4, row=1, padx=5, pady=5)          
        start_btn = ttk.Button(self.root, text='Start', padding=5, width=15,
                            command=self.start)
        start_btn.grid(column=5, row=2, padx=5, pady=5)   

        BUTTONS = [bubble_sort_btn,insertion_sort_btn,selection_sort_btn,
                        merge_sort_btn,quick_sort_btn,start_btn]  
        ttk.Button(self.root, text='Shuffle', style='info.Outline.TButton', padding=5, width=15,
                        command=self.shuffle).grid(column=5, row=1, padx=5, pady=5)
        
        
        self.buttons = {k:v for k,v in zip(self.sort_names,BUTTONS[:-1])}
        
        # _________________________________________________________
        ttk.Label(self.root, text='Speed & Array Size:').grid(row=2,column=0)
        self.arraysize=ttk.Scale(self.root,from_=6,to=120,length=380,style='success.Horizontal.TScale',value=10,
            command=lambda x:self.slide_function())
        self.arraysize.grid(row=2,column=1,columnspan=3)
        # ________________________________CANVAS_________________________
        self.canvas=Canvas(self.root, width=800-5, height=400,highlightbackground="dodgerblue",highlightthickness=2,
        bg='black')
        self.canvas.grid(row=4, padx=5, pady=10, columnspan=6)

        self.speed=0.2 #sorting speed
        self.N=10
        self.colours=['dodgerblue' for i in range(self.N)]
        self.shuffle() 

        # ________________ Color arrays _________________
        self.__sorted_array = ['lime' for _ in range(self.N)]
        self.__default_colours = ['dodgerblue' for i in range(self.N)]

    def display(self,N: int,a: list,rong: list)-> None:
        '''
        N = number of rectangles
        a = array of heights of rectangles
        rong = array of colours of each and every rectangle
        '''
        self.canvas.delete('all')
        width=(1570)/(3*N-1)
        gap=width/2

        for i in range(N):
            self.canvas.create_rectangle(7+i*width+i*gap,0,
                                         7+(i+1)*width+i*gap,a[i],fill=rong[i])

        self.root.update_idletasks()    
    
    def slide_function(self):
        '''
        This function helps to increase or decrease the number of 
        bars required for sorting
        '''
        self.N=int(self.arraysize.get())
        self.data=linspace(5,400,self.N,dtype=uint16)
        self.speed=5/self.arraysize.get()
        self.colours=['dodgerblue' for _ in range(self.N)]
        self.shuffle()
            
    def shuffle(self):
        self.canvas.delete('all')
        self.data=linspace(5,400,self.N,dtype=uint16)
        random.shuffle(self.data)
        self.display(self.N,self.data,self.colours)

     # ---------------button selection of sorting algos---------------------------

    
    def _helper(func):
        def inner(self):
            btn_name = func.__name__
            if self.sorts[btn_name] == False: 
                self.sorts[btn_name] = True
                for k in self.sorts.keys():
                    if k==btn_name:
                        self.buttons[k].config(style='success.TButton')
                    else: 
                        self.sorts[k]=False 
                        self.buttons[k].config(style='info.TButton')
            else: 
                self.sorts[btn_name]=False 
                self.buttons[btn_name].config(style='info.TButton')
        return inner


    @_helper
    def bubble(self):...
    @_helper
    def merge(self):...
    @_helper
    def selection(self):...
    @_helper
    def quick(self):...
    @_helper
    def insertion(self):...
 
    # -----------------------------------------------------------
    def __bubbleSort(self):
        pass 

    def start(self):
        if self.sorts['bubble'] is True:
            for i in range(self.N-1):
                for j in range(self.N-1-i):
                        self.display(self.N,self.data,['purple' if a==j or a==j+1 else 'green' if a>self.N-1-i else 'dodgerblue' for a in range(self.N)])
                        time.sleep(self.speed)
                        if self.data[j]>self.data[j+1]:
                            self.display(self.N,self.data,['red' if a==j or a==j+1 else 'green' if a>self.N-1-i else 'dodgerblue' for a in range(self.N)])
                            time.sleep(self.speed)
                            self.data[j],self.data[j+1]=self.data[j+1],self.data[j]
                            self.display(self.N,self.data,['lime' if a==j or a==j+1 else 'green' if a>self.N-1-i else 'dodgerblue' for a in range(self.N)])
                            time.sleep(self.speed)
            self.display(self.N,self.data,self.__sorted_array)

        elif self.sorts['insertion'] is True:
            for j in range(1,len(self.data)):
                key=self.data[j]
                i=j-1
                self.display(self.N,self.data,['purple' if a==i or a==i+1 else 'green' if a<=j else'dodgerblue' for a in range(self.N)])
                time.sleep(self.speed)
                while i>=0 and self.data[i]>key:
                        self.data[i+1]=self.data[i]
                        self.display(self.N,self.data,['yellow' if a==i else 'green' if a<=j else'dodgerblue' for a in range(self.N)])
                        time.sleep(self.speed)
                        i-=1
                self.data[i+1]=key
            self.display(self.N,self.data,self.__sorted_array)

        elif self.sorts['selection'] is True:
            for i in range(len(self.data)-1):
                min_index=i
                # loop to find the minimum element and its index
                for j in range(i+1,len(self.data)):
                        self.display(self.N,self.data,['yellow' if a==min_index or a==i else 'green' if a<=i else 'dodgerblue' for a in range(self.N)])
                        time.sleep(self.speed)
                        if self.data[min_index]>self.data[j]:
                            self.display(self.N,self.data,['red' if a==min_index or a==j else 'green' if a<=i else 'dodgerblue' for a in range(self.N)])
                            time.sleep(self.speed)
                            min_index=j
                if min_index!=i:
                        self.data[i], self.data[min_index]=self.data[min_index],self.data[i]
                        self.display(self.N,self.data,['lime' if a==min_index or a==i else 'green' if a<=i else 'dodgerblue' for a in range(self.N)])
                        time.sleep(self.speed)
            self.display(self.N,self.data,self.__sorted_array)
            

        elif self.sorts['merge'] is True:
            self.mergesort(self.data,0,self.N-1)
            self.display(self.N,self.data,self.__sorted_array)

        elif self.sorts['quick'] is True:
            self.quicksort(self.data,0,self.N-1)
            self.display(self.N,self.data,self.__sorted_array)

        else:
            #show messege box
            messagebox.showerror("Algorithm Visualizer", "You didn't select any sorting algorithm")
            

     # -----------merge sort algo-------------------------------------

    def mergesort(self,a,front,last):
        if front<last:
            mid= (front+last)//2

            self.mergesort(a,front,mid)
            self.mergesort(a,mid+1,last)


            self.display(self.N,self.data,self.__default_colours)
            
            rj=mid+1
            if a[mid]<=a[mid+1]:
                return 
            
            while front<=mid and rj<=last:
                self.display(self.N,self.data,['yellow' if x==front or x==rj else 'dodgerblue' for x in range(self.N)])
                time.sleep(self.speed)
                if a[front]<=a[rj]:
                        self.display(self.N,self.data,['lime' if x==front or x==rj else 'dodgerblue' for x in range(self.N)])
                        time.sleep(self.speed)
                        front+=1
                else:
                        self.display(self.N,self.data,['red' if x==front or x==rj else 'dodgerblue' for x in range(self.N)])
                        time.sleep(self.speed)
                        temp=a[rj]
                        i=rj
                        while i!=front:
                            a[i]=a[i-1]
                            i-=1
                        a[front]=temp
                        self.display(self.N,self.data,['lime' if x==front or x==rj else 'dodgerblue' for x in range(self.N)])
                        time.sleep(self.speed)

                        front+=1
                        mid+=1
                        rj+=1
        
            self.display(self.N,self.data,self.__default_colours)
            time.sleep(self.speed)
    
     #-----------------------------quick sort algo---------------

    def partition(self,a,i,j):
        '''
        a -> is  the array
        i -> index from front
        j -> index from back'''

        l=i # left index

        pivot=a[i]
        piv_index=i

        while i<j:
            while  i<len(a) and a[i]<= pivot:
                i+=1
                self.display(self.N,self.data,['purple' if x==piv_index else 'yellow' if x==i else "dodgerblue" for x in range(self.N)])
                time.sleep(self.speed)
            while a[j]>pivot:
                j-=1
            if i<j:
                self.display(self.N,self.data,['red' if x==i or x==j else "dodgerblue" for x in range(self.N)])
                time.sleep(self.speed)
                a[i],a[j]=a[j],a[i]
                self.display(self.N,self.data,['lime' if x==i or x==j else "dodgerblue" for x in range(self.N)])
                time.sleep(self.speed)
        a[j],a[l]=a[l],a[j]
        return j

    def quicksort(self,a,i,j):
        if i<j:
            x=self.partition(a,i,j)
            self.quicksort(a,i,x-1)
            self.quicksort(a,x+1,j)

if __name__ == '__main__':
     win = Style(theme='darkly').master
     obj = window(win, 'Sorting Algorithm Visualizer')

     win.mainloop()
