import tkinter as tk
import numpy as np
from collections import deque
from tkinter import messagebox

root = tk.Tk()

maze = [
    [1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1],
    [0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1],
    [0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1],
    [0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0],
    [1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1]
]

cnt = 0

maze = np.array(maze)
root.title("Path_Finder")

root.resizable(0, 0)
# root.geometry("800x700")
dst_max = 1
dst_arr = np.full((15, 15), -1)
w = tk.Canvas(root, width=601, height=601)
brdr = w.create_rectangle(2, 2, 600, 600, fill='#e1e6ed')
opt_cnv = tk.Canvas(root, bg="white",  height=601, width=211)
opt_cnv.create_rectangle(2, 2, 210, 600, fill='#e1e6ed')


class pos:
    def __init__(self, i, j):
        self.row = i
        self.col = j


strt = [pos(0, 1)]
w.create_oval(45, 5, 75,  35, fill="#5FC052", tag="src")
# w.create_oval((j*40)+5, (i*40)+5, ((j+1)*40)-5,  ((i+1)*40)-5, fill = "#FFFF00", tag = "path")
dest = [pos(1, 1)]
w.create_oval(45, 45, 75,  75, fill="#CB3030", tag="dst")
src = None
dst = None


def ls_fill(ls_pos, node):
    global dst_arr, cnt
    i = node.row
    j = node.col
    if (i-1 >= 0):
        if (maze[i-1][j] == 0):
            if (dst_arr[i-1, j] == -1) or (dst_arr[i-1, j] > dst_arr[i, j] + 1):
                dst_arr[i-1, j] = dst_arr[i, j] + 1
                ls_pos.appendleft(pos(i-1, j))
                cnt = cnt + 1

    if (i+1 < 15):
        if (maze[i+1][j] == 0):
            if (dst_arr[i+1, j] == -1) or (dst_arr[i+1, j] > dst_arr[i, j] + 1):
                dst_arr[i+1, j] = dst_arr[i, j] + 1
                ls_pos.appendleft(pos(i+1, j))
                cnt = cnt + 1

    if (j-1 >= 0):
        if (maze[i][j-1] == 0):
            if (dst_arr[i, j-1] == -1) or (dst_arr[i, j-1] > dst_arr[i, j] + 1):
                dst_arr[i, j-1] = dst_arr[i, j] + 1
                ls_pos.appendleft(pos(i, j-1))
                cnt = cnt + 1

    if (j+1 < 15):
        if (maze[i][j+1] == 0):
            if (dst_arr[i, j+1] == -1) or (dst_arr[i, j+1] > dst_arr[i, j] + 1):
                dst_arr[i, j+1] = dst_arr[i, j] + 1
                ls_pos.appendleft(pos(i, j+1))
                cnt = cnt + 1


def all_short_path(strt):
    ls_pos = deque([])
    dst_arr[strt.row, strt.col] = 0
    ls_fill(ls_pos, strt)
    while(len(ls_pos) > 0):
        # val = ls_pos.pop()
        ls_fill(ls_pos, ls_pos.pop())


def short_path(strt, dest):
    global dst_max, cnt
    ls_pos = deque([])
    ls_path = []
    dst_arr[strt.row, strt.col] = 0
    ls_fill(ls_pos, strt)
    while(len(ls_pos) > 0):
        val = ls_pos.pop()
        # ls_fill(ls_pos, ls_pos.pop())

        if(val.row == dest.row) and (val.col == dest.col):
            i = val.row
            j = val.col
            dst_arr[i, j]
            while(dst_arr[i, j] != 0):
                flag = 0
                if (i-1 >= 0):
                    if (dst_arr[i-1, j] != -1) and (dst_arr[i-1, j] < dst_arr[i, j]):
                        i = i-1
                        ls_path.append(pos(i, j))
                        flag = 1
                if (i+1 < 15) and (flag == 0):
                    if (dst_arr[i+1, j] != -1) and (dst_arr[i+1, j] < dst_arr[i, j]):
                        i = i+1
                        ls_path.append(pos(i, j))
                        flag = 1
                if (j-1 >= 0) and (flag == 0):
                    if (dst_arr[i, j-1] != -1) and (dst_arr[i, j-1] < dst_arr[i, j]):
                        j = j-1
                        ls_path.append(pos(i, j))
                        flag = 1
                if (j+1 < 15) and (flag == 0):
                    if (dst_arr[i, j+1] != -1) and (dst_arr[i, j+1] < dst_arr[i, j]):
                        j = j+1
                        ls_path.append(pos(i, j))
            break
        ls_fill(ls_pos, val)
        for s in ls_pos:
            print(dst_arr[s.row, s.col])
        # print("end")
        print("cnt: ", cnt)
        if (dst_max < dst_arr[val.row, val.col]):
            dst_max = dst_arr[val.row, val.col]
    return ls_path


# def m_move( event ):
#   tup=w.coords(oval)
#   t=5
#   print(int(tup[0])//40, int(tup[1]-5)//40)
#   if(15>(tup[0]//40)>=0) and (15>(tup[1]//40)>=0):
#     if (event.char=="w") and (maze[int(tup[1]-t)//40][int(tup[0])//40]==0) :

#       w.move(oval, 0, -t)

#     elif (event.char=="a") and (maze[int(tup[1])//40][int(tup[0]-t)//40]==0):

#       w.move(oval, -t, 0)

#     elif event.char=="s" and (15>(int(tup[3]+t)//40)):#(maze[int(tup[3]+t)//40][int(tup[2])//40]==0):
#       if  (maze[int(tup[3]+t)//40][int(tup[2])//40]==0):
#         w.move(oval, 0, t)

#     elif event.char=="d" and (15>(int(tup[2]+t)//40)):#(maze[int(tup[3])//40][int(tup[2]+t)//40]==0):
#       if (maze[int(tup[3])//40][int(tup[2]+t)//40]==0):
#         w.move(oval, t, 0)


def show_msg(*val):
    tk.messagebox.showerror("error", val[0])


def explored_node(dst_arr, dest):
    try:
        w.delete("expl")
    except:
        pass
    red = 255
    grn = 255
    blu = 255
    l, m = dest.row, dest.col
    mul = int(255/(dst_max+10))
    print(mul)
    # print(mul, grn - mul*dst_arr[i, j], blu - mul*dst_arr[i, j])
    for i in range(15):
        for j in range(15):
            if (dst_arr[i, j] > 0) and not((i == l) and (j == m)):
                clr = '#' + hex(red)[2:] + hex(grn - mul*dst_arr[i, j]
                                               )[2:] + hex(blu - mul*dst_arr[i, j])[2:]
                w.create_rectangle((j*40), (i*40), ((j+1)*40),
                                   ((i+1)*40), fill=clr, tag="expl")


def m_path():
    global dst_arr, cnt
    try:
        w.delete("path")
    except:
        pass
    cnt = 0
    ls_path = short_path(strt[0], dest[0])
    print(dst_arr)
    # print(ls_path)
    explored_node(dst_arr, dest[0])

    if len(ls_path) != 0:
        p = len(ls_path)
        for tr in range(p-1):
            i = ls_path[tr].row
            j = ls_path[tr].col
            w.create_oval((j*40)+5, (i*40)+5, ((j+1)*40)-5,
                          ((i+1)*40)-5, fill="#FFFF00", tag="path")
    dst_arr = np.full((15, 15), -1)
    return


def def_strt(event, strt):
    # global dest

    j = int(event.x)//40
    i = int(event.y - 5)//40
    if (maze[i][j] == 1):
        show_msg("can'nt be on wall")
        return

    if (dest != None):
        if (dest[0].row == i) and (dest[0].col == j):
            show_msg("source and destination are same")
            return
    try:
        w.delete("src")
    except:
        pass
    try:
        w.delete("path")
    except:
        pass
    try:
        w.delete("expl")
    except:
        pass
    strt[0] = pos(i, j)
    print(strt[0].row, strt[0].col)
    w.create_oval((j*40)+5, (i*40)+5, ((j+1)*40)-5,
                  ((i+1)*40)-5, fill="#5FC052", tag="src")
    # return strt
    # print(i, j)


def def_dest(event, dest):

    j = int(event.x)//40
    i = int(event.y - 5)//40
    if (maze[i][j] == 1):
        show_msg("can'nt be on wall")
        return
    if (strt != None):
        if (strt[0].row == i) and (strt[0].col == j):
            show_msg("source and destination are same")
            return
    try:
        w.delete("dst")
    except:
        pass
    try:
        w.delete("path")
    except:
        pass
    try:
        w.delete("expl")
    except:
        pass
    dest[0] = pos(i, j)
    w.create_oval((j*40)+5, (i*40)+5, ((j+1)*40)-5,
                  ((i+1)*40)-5, fill="#CB3030", tag="dst")
    # return dest
    # print(i, j)

# print(maze)


def maze_creater():
    try:
        w.delete("wall")
    except:
        pass
    j = 0
    for i in maze:
        for k in i:

            if(k == 1):
                w.create_rectangle((j % 15)*40, (j//15)*40, ((j % 15)+1)
                                   * 40, ((j//15)+1)*40, fill="#35393d", tag="wall")

            j = j+1


def wall_crt(event, strt, dest):
    global maze
    j = int(event.x)//40
    i = int(event.y - 5)//40
    try:
        w.delete("path")
    except:
        pass
    try:
        w.delete("expl")
    except:
        pass

    if (strt != None):
        if (strt[0].row == i) and (strt[0].col == j):
            show_msg("wall on source not possible")
            return

    if (dest != None):
        if (dest[0].row == i) and (dest[0].col == j):
            show_msg("wall on destination not possible")
            return

    if maze[i, j] == 1:
        maze[i, j] = 0

    else:
        maze[i, j] = 1
        # w.create_rectangle((j*40), (i*40), ((j+1)*40),  ((i+1)*40), fill = "#35393d"  , tag = "wall")
    maze_creater()


def e_maze():
    global maze
    try:
        w.delete("path")
    except:
        pass
    try:
        w.delete("expl")
    except:
        pass
    try:
        w.delete("wall")
    except:
        pass
    maze = np.zeros((15, 15))
    maze_creater()


# oval=w.create_oval(50, 10, 70,  30, fill =  'green')


# root.bind( "<Key>", m_move )

w.bind("<Button-1>", lambda event: def_strt(event, strt))

w.bind("<Button-3>", lambda event: def_dest(event, dest))

w.bind("<Button-2>", lambda event: wall_crt(event, strt, dest))
# button for opt_cnv

b_fn_path = tk.Button(root, text="Find Path", command=m_path)
opt_cnv.create_window(100, 50, window=b_fn_path)

b_empty_path = tk.Button(root, text="Empty Maze", command=e_maze)
opt_cnv.create_window(100, 100, window=b_empty_path)

instct = tk.LabelFrame(root, text="instructions", height=200, width=150)
opt_cnv.create_window(105, 300, window=instct)

l1 = tk.Label(instct, text="left mouse: starting node")
l1.pack()

l2 = tk.Label(instct, text="right mouse: ending node")
l2.pack()

l3 = tk.Label(instct, text="middle mouse: create or distroy wall")
l3.pack()

maze_creater()


w.grid(row=1, column=1, padx=10, pady=10)
opt_cnv.grid(row=1, column=2, padx=10, pady=10)

tk.mainloop()
