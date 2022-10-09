from tkinter import *
from tkinter import ttk

import random
from turtle import speed
from colors import *
from Algorithms.bubblesort import bubble_sort
from Algorithms.mergesort import merge_sort
from Algorithms.quick_sort import quick_sort

main_window = Tk()

main_window.title("Sorting Algorithm Visualizer")
main_window.maxsize(1000,600)
main_window.config(bg = WHITE)

algo_name = StringVar()
algo_list = ["Bubble sort",'Merge sort','Quick sort']

speed_name = StringVar()
speed_list = ["fast","medium","slow"]

data = []

def drawData(data,colorsArray):
    canvas.delete("all")
    canvas_width = 800
    canvas_height = 400
    x_width = round(canvas_width/len(data)+1)
    offset = 4
    spacing = 2

    normalize_data = [i / max(data) for i in data]

    for i,val  in enumerate(normalize_data):
        x0 = i * x_width + offset + spacing
        y0 = canvas_height - val * 390
        x1 = (i + 1) * x_width + offset
        y1 = canvas_height
        canvas.create_rectangle(x0,y0,x1,y1,fill=colorsArray[i])
    main_window.update_idletasks()

def generate():
    global data
    data = []
    for i in range(100):
        val = random.randint(1,100)
        data.append(val)
    drawData(data,[BLUE for i in range(len(data))])

def set_speed():

    if speed_menu.get() == "slow":
        return 0.3
    elif speed_menu.get() == "medium":
        return 0.1
    else:
        return 0.01


def sort():
    global data
    timeTick = set_speed()

    if algo_menu.get() == "Bubble sort":
        bubble_sort(data,drawData,timeTick)
    elif algo_menu.get() == "Merge sort":
        merge_sort(data,0,len(data)-1,drawData,timeTick)
    elif algo_menu.get() == "Quick sort":
        quick_sort(data,0,len(data)-1,drawData,timeTick)
        

UI_frame = Frame(main_window,width = 800,height = 300,bg = WHITE)
UI_frame.grid(row=0,column=0,padx=10,pady=5)

l1 = Label(UI_frame,text="Algorithm : ",bg=WHITE)
l1.grid(row=0,column=0,padx=10,pady=5)
algo_menu = ttk.Combobox(UI_frame,textvariable=algo_name,values = algo_list)
algo_menu.grid(row=0,column=1,padx = 5,pady=5)
algo_menu.current(0)

l2 = Label(UI_frame,text="Speed : ",bg=WHITE)
l2.grid(row=2,column=0,padx=10,pady=5)
speed_menu = ttk.Combobox(UI_frame,textvariable=speed_name,values = speed_list)
speed_menu.grid(row=2,column=1,padx = 5,pady=5)
speed_menu.current(0)

b1 = Button(UI_frame,text="Sort",command=sort,bg = "cyan")
b1.grid(row=3,column=0,padx=10,pady=5)

b2 = Button(UI_frame,text="generate",command=generate,bg = "cyan")
b2.grid(row=3,column=1,padx=10,pady=5)

canvas = Canvas(main_window,width = 800,height=400,bg=WHITE)
canvas.grid(row=1,column=0,padx=10,pady=5)




main_window.mainloop()