from tkinter import *
from tkinter import ttk
from ttkbootstrap import *
import numpy as np
import time


class window:

     st = {'bubble': False, 'insertion': False, 'selection': False,
          'merge': False, 'bucket': False, 'quick': False}  # to select the sorts

     def __init__(self, root, title) -> None:
          self.root = root
          self.root.title(title)
          self.root.resizable(width=False, height=False)
          Label(self.root, text='Sorting Algorithm Visualizer').grid(
               row=0, columnspan=6)
          #  Buttons
          self.bs = ttk.Button(self.root, text='Bubble Sort', style='info.TButton', padding=5, width=15,
                              command=self.bubble)
          self.bs.grid(column=0, row=1, padx=5, pady=5)
          self.Is = ttk.Button(self.root, text='Insertion Sort', style='info.TButton', padding=5, width=15,
                              command=self.insertion)
          self.Is.grid(column=1, row=1, padx=5, pady=5)
          self.ss = ttk.Button(self.root, text='Selection Sort', style='info.TButton', padding=5, width=15,
                              command=self.selection)
          self.ss.grid(column=2, row=1, padx=5, pady=5)
          self.ms = ttk.Button(self.root, text='Merge Sort', style='info.TButton', padding=5, width=15,
                              command=self.merge)
          self.ms.grid(column=3, row=1, padx=5, pady=5)
          self.buckets = ttk.Button(self.root, text='Bucket Sort', style='info.TButton', padding=5, width=15,
                                   command=self.bucket)
          self.buckets.grid(column=4, row=1, padx=5, pady=5)
          self.qs = ttk.Button(self.root, text='Quick Sort', style='info.TButton', padding=5, width=15,
                              command=self.quick)
          self.qs.grid(column=5, row=1, padx=5, pady=5)
          
          self.start = ttk.Button(self.root, text='Start', padding=5, width=15,
                              command=self.start)
          self.start.grid(column=5, row=2, padx=5, pady=5)

          

          self.shuf = ttk.Button(self.root, text='Shuffle', style='info.TButton', padding=5, width=15,
                                   command=self.shuffle)
          self.shuf.grid(column=0, row=2, padx=5, pady=5)

          #    Canvas
          self.canvas=Canvas(self.root, width=800-5, height=400,
               bg='white')
          self.canvas.grid(row=4, padx=5, pady=10, columnspan=6)

          # some constants
          self.N=30
          self.colours=['blue' for i in range(self.N)]
          N=self.N
          self.data=np.linspace(5,400,N,dtype=np.uint16)
          np.random.shuffle(self.data)
          self.display(self.N,self.data,self.colours)
        
     
     def display(self,N: int,a: list,rong: list):
          '''
          N = number of rectangles
          a = array of heights of rectangles
          rong = array of colours of each and every rectangle'''

          self.canvas.delete('all')
          width=(2*(780/N))//3
          gap=(780/N)//3
          for i in range(N):
               self.canvas.create_rectangle(0+i*width+i*gap,0,0+(i+1)*width+i*gap,a[i],fill=rong[i])

          self.root.update_idletasks()

     
     '''  bubble sort'''
     def bubble(self):
          if self.st['bubble'] is False:
               self.st['bubble'] = True
               self.bs.config(style='success.TButton')

               for i in self.st:
                    if i != 'bubble':
                         self.st[i]=False

               self.qs.config(style='info.TButton')
               self.buckets.config(style='info.TButton')
               self.ms.config(style='info.TButton')
               self.ss.config(style='info.TButton')
               self.Is.config(style='info.TButton')
               # print(self.st)
          else:
               self.st['bubble'] = False
               self.bs.config(style='info.TButton')
               # print(self.st)

     '''  merge sort'''
     def merge(self):
          if self.st['merge'] is False:
               self.st['merge'] = True
               self.ms.config(style='success.TButton')

               for i in self.st:
                    if i != 'merge':
                         self.st[i]=False

               self.qs.config(style='info.TButton')
               self.buckets.config(style='info.TButton')
               self.bs.config(style='info.TButton')
               self.ss.config(style='info.TButton')
               self.Is.config(style='info.TButton')
               # print(self.st)
          else:
               self.st['merge'] = False
               self.ms.config(style='info.TButton')
               # print(self.st)

     '''  quick sort'''
     def quick(self):
          if self.st['quick'] is False:
               self.st['quick'] = True
               self.qs.config(style='success.TButton')

               for i in self.st:
                    if i != 'quick':
                         self.st[i]=False

               self.ms.config(style='info.TButton')
               self.buckets.config(style='info.TButton')
               self.bs.config(style='info.TButton')
               self.ss.config(style='info.TButton')
               self.Is.config(style='info.TButton')
               # print(self.st)
          else:
               self.st['quick'] = False
               self.qs.config(style='info.TButton')
               # print(self.st)

     '''  selection sort'''
     def selection(self):
          if self.st['selection'] is False:
               self.st['selection'] = True
               self.ss.config(style='success.TButton')

               for i in self.st:
                    if i != 'selection':
                         self.st[i]=False

               self.qs.config(style='info.TButton')
               self.buckets.config(style='info.TButton')
               self.bs.config(style='info.TButton')
               self.ms.config(style='info.TButton')
               self.Is.config(style='info.TButton')
               # print(self.st)
          else:
               self.st['selection'] = False
               self.ss.config(style='info.TButton')
               # print(self.st)

     '''  insertion sort'''
     def insertion(self):
          if self.st['insertion'] is False:
               self.st['insertion'] = True
               self.Is.config(style='success.TButton')


               for i in self.st:
                    if i != 'insertion':
                         self.st[i]=False
               self.qs.config(style='info.TButton')
               self.buckets.config(style='info.TButton')
               self.bs.config(style='info.TButton')
               self.ss.config(style='info.TButton')
               self.ms.config(style='info.TButton')
               # print(self.st)
          else:
               self.st['insertion'] = False
               self.Is.config(style='info.TButton')
               # print(self.st)

     '''  bucket sort'''
     def bucket(self):
          if self.st['bucket'] is False:
               self.st['bucket'] = True
               self.buckets.config(style='success.TButton')

               for i in self.st:
                    if i != 'bucket':
                         self.st[i]=False

               self.qs.config(style='info.TButton')
               self.Is.config(style='info.TButton')
               self.bs.config(style='info.TButton')
               self.ss.config(style='info.TButton')
               self.ms.config(style='info.TButton')
               # print(self.st)
          else:
               self.st['bucket'] = False
               self.buckets.config(style='info.TButton')
               # print(self.st)

     def shuffle(self):
          self.canvas.delete('all')
          np.random.shuffle(self.data)
          self.display(self.N,self.data,self.colours)
          # print(self.data)

     def start(self,T=0.2):
          if self.st['bubble'] is True:
               for i in range(self.N-1):
                    for j in range(self.N-1-i):
                         if self.data[j]>self.data[j+1]:
                              self.data[j],self.data[j+1]=self.data[j+1],self.data[j]
                              self.display(self.N,self.data,['purple' if a==j or a==j+1 else 'green' if a>self.N-1-i else 'blue' for a in range(self.N)])
                              time.sleep(T)
               self.display(self.N,self.data,['green' for _ in range(self.N)])

          elif self.st['insertion'] is True:
               for j in range(1,len(self.data)):
                    key=self.data[j]
                    i=j-1
                    while i>=0 and self.data[i]>key:
                         self.data[i+1]=self.data[i]
                         i-=1
                         self.display(self.N,self.data,['purple' if a==j or a==j+1 else 'green' if a<=j else'blue' for a in range(self.N)])
                         time.sleep(T)
                    self.data[i+1]=key
               self.display(self.N,self.data,['green' for _ in range(self.N)])

          elif self.st['selection'] is True:
               for i in range(len(self.data)-1):
                    min_index=i
                    # loop to find the minimum element and its index
                    for j in range(i+1,len(self.data)):
                         if self.data[min_index]>self.data[j]:
                              self.display(self.N,self.data,['purple' if a==j else 'green' if a<=i else 'blue' for a in range(self.N)])
                              time.sleep(T)
                              min_index=j
                    if min_index!=i:
                         self.data[i], self.data[min_index]=self.data[min_index],self.data[i]
               self.display(self.N,self.data,['green' for _ in range(self.N)])
               

          elif self.st['merge'] is True:
               self.data=self.mergesort(self.data)
               self.display(self.N,self.data,['green' for _ in range(self.N)])

               pass

          elif self.st['quick'] is True:
               pass

          elif self.st['bucket'] is True:
               pass

          else:
               '''show messege box'''
               pass

          # print(self.data)
     
 #----------------------------------------------------------------------    
     def mergeelements(self,l,r):

          i,j=0,0
          b=[]
          while i<len(l) and j<len(r):
               if l[i]<r[j]:
                    b.append(l[i])
                    i+=1
                    # self.display(self.N,b+self.data[len(b):],['green' if x<len(b) else 'purple' for x in range(self.N) ])
                    # time.sleep(0.2)     
               else:
                    b.append(r[j])
                    j+=1
                    # self.display(self.N,b+self.data[len(b):],['green' if x<len(b) else 'purple' for x in range(self.N) ])
                    # time.sleep(0.2)     
                  
          while i<len(l):
               b.append(l[i])
               i+=1
               # self.display(self.N,b+self.data[len(b):],['green' if x<len(b) else 'purple' for x in range(self.N) ])
               # time.sleep(0.2)     
               
          while j<len(r):
               b.append(r[j])
               j+=1
               # self.display(self.N,b+self.data[len(b):],['green' if x<len(b) else 'purple' for x in range(self.N) ])
               # time.sleep(0.2)     
               
          return b    
     
     
     def mergesort(self,a):
          size=len(a)
          if size<2:
               return a
          mid=size//2
          l=a[:mid]
          r=a[mid:]
          l=self.mergesort(l)
          r=self.mergesort(r)
          return self.mergeelements(l,r)
     
#---------------------------------------------------------------------------

win = Style(theme='cyborg').master
obj = window(win, 'Sorting Algorithm Visualizer')

win.mainloop()
