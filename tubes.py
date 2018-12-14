from Tkinter import *
import easygui as eg
import skimage.io as io
from PIL import ImageTk, Image
import numpy as np
from matplotlib import cm
from matplotlib import pyplot as plt
import numpy as np

path='empty.png'

# Task 5

# Edge Detection

def edgeDetection():
    pixel = Image.open(path)
    len1, len2 = pixel.size
    pixelNew = Image.new('RGB',(len1, len2))
    print(len1, len2)
    m1 = 0
    m2 = 1
    m3 = 0
    m4 = 1
    m5 = -4
    m6 = 1
    m7 = 0
    m8 = 1
    m9 = 0
    for i in range(len1-2):
        for j in range(len2-2):
            r1,g1,b1 = pixel.getpixel((i,j))
            r2,g2,b2 = pixel.getpixel((i+1,j))
            r3,g3,b3 = pixel.getpixel((i+2,j))
            r4,g4,b4 = pixel.getpixel((i,j+1))
            r5,g5,b5 = pixel.getpixel((i+1,j+1))
            r6,g6,b6 = pixel.getpixel((i+2,j+1))
            r7,g7,b7 = pixel.getpixel((i,j+2))
            r8,g8,b8 = pixel.getpixel((i+1,j+2))
            r9,g9,b9 = pixel.getpixel((i+2,j+2))
            rSum = (m1*r1) + (m2*r2) + (m3*r3) + (m4*r4) + (m5*r5) + (m6*r6) + (m7*r7) + (m8*r8) + (m9*r9)
            gSum = (m1*g1) + (m2*g2) + (m3*g3) + (m4*g4) + (m5*g5) + (m6*g6) + (m7*g7) + (m8*g8) + (m9*g9)
            bSum = (m1*b1) + (m2*b2) + (m3*b3) + (m4*b4) + (m5*b5) + (m6*b6) + (m7*b7) + (m8*b8) + (m9*b9)  
            pixelNew.putpixel((i+1,j+1),(rSum, gSum, bSum))
    img = ImageTk.PhotoImage(pixelNew)
    panel.configure(image=img)
    panel.image = img

# Blur Function

def blur():
    pixel = Image.open(path)
    len1, len2 = pixel.size
    pixelNew = Image.new('RGB',(len1, len2))
    print(len1, len2)
    m1 = 1/9
    m2 = 1/9
    m3 = 1/9
    m4 = 1/9
    m5 = 1/9
    m6 = 1/9
    m7 = 1/9
    m8 = 1/9
    m9 = 1/9
    for i in range(len1-2):
        for j in range(len2-2):
            r1,g1,b1 = pixel.getpixel((i,j))
            r2,g2,b2 = pixel.getpixel((i+1,j))
            r3,g3,b3 = pixel.getpixel((i+2,j))
            r4,g4,b4 = pixel.getpixel((i,j+1))
            r5,g5,b5 = pixel.getpixel((i+1,j+1))
            r6,g6,b6 = pixel.getpixel((i+2,j+1))
            r7,g7,b7 = pixel.getpixel((i,j+2))
            r8,g8,b8 = pixel.getpixel((i+1,j+2))
            r9,g9,b9 = pixel.getpixel((i+2,j+2))
            rSum = (m1*r1) + (m2*r2) + (m3*r3) + (m4*r4) + (m5*r5) + (m6*r6) + (m7*r7) + (m8*r8) + (m9*r9)
            gSum = (m1*g1) + (m2*g2) + (m3*g3) + (m4*g4) + (m5*g5) + (m6*g6) + (m7*g7) + (m8*g8) + (m9*g9)
            bSum = (m1*b1) + (m2*b2) + (m3*b3) + (m4*b4) + (m5*b5) + (m6*b6) + (m7*b7) + (m8*b8) + (m9*b9)  
            pixelNew.putpixel((i+1,j+1),(rSum, gSum, bSum))
    img = ImageTk.PhotoImage(pixelNew)
    panel.configure(image=img)
    panel.image = img

# Sharp Function

def sharp():
    pixel = Image.open(path)
    len1, len2 = pixel.size
    pixelNew = Image.new('RGB',(len1, len2))
    print(len1, len2)
    m1 = 0
    m2 = -1
    m3 = 0
    m4 = -1
    m5 = 5
    m6 = -1
    m7 = 0
    m8 = -1
    m9 = 0
    for i in range(len1-2):
        for j in range(len2-2):
            r1,g1,b1 = pixel.getpixel((i,j))
            r2,g2,b2 = pixel.getpixel((i+1,j))
            r3,g3,b3 = pixel.getpixel((i+2,j))
            r4,g4,b4 = pixel.getpixel((i,j+1))
            r5,g5,b5 = pixel.getpixel((i+1,j+1))
            r6,g6,b6 = pixel.getpixel((i+2,j+1))
            r7,g7,b7 = pixel.getpixel((i,j+2))
            r8,g8,b8 = pixel.getpixel((i+1,j+2))
            r9,g9,b9 = pixel.getpixel((i+2,j+2))
            rSum = (m1*r1) + (m2*r2) + (m3*r3) + (m4*r4) + (m5*r5) + (m6*r6) + (m7*r7) + (m8*r8) + (m9*r9)
            gSum = (m1*g1) + (m2*g2) + (m3*g3) + (m4*g4) + (m5*g5) + (m6*g6) + (m7*g7) + (m8*g8) + (m9*g9)
            bSum = (m1*b1) + (m2*b2) + (m3*b3) + (m4*b4) + (m5*b5) + (m6*b6) + (m7*b7) + (m8*b8) + (m9*b9)  
            pixelNew.putpixel((i+1,j+1),(rSum, gSum, bSum))
    img = ImageTk.PhotoImage(pixelNew)
    panel.configure(image=img)
    panel.image = img

# Task 4

# Histogram

def histogram():
    red = [0] * 256
    green = [0] * 256
    blue = [0] * 256
    redMax = 0
    redMin = 9999
    greenMax = 0
    greenMin = 9999
    blueMax = 0
    blueMin = 9999
    i = 0
    j = 0
    pixel = Image.open(path)
    len1, len2 = pixel.size
    for i in range(len1):
        for j in range(len2):
            r,g,b = pixel.getpixel((i,j))
            red[r] = red[r] + 1
            green[g] = green[g] + 1
            blue[b] = blue[b] + 1 
    width = 1/1.5
    plt.title("Red")
    plt.bar(np.arange(256), red,  color="red")
    plt.bar(np.arange(256), green,  color="green")
    plt.bar(np.arange(256), blue,  color="blue")
    plt.show()

# Task 3

# Geser Kiri

def geserKiri():
    pixel = Image.open(path)
    len1, len2 = pixel.size
    pixelNew = Image.new("RGB", (len1-40, len2))
    x = 0
    y = 0
    for i in range(40,len1):
        for j in range(len2):
            r, g, b = pixel.getpixel((i, j))
            pixelNew.putpixel((x,y), (r, g, b))
            y = y+1
        x = x+1
        y = 0
    img = ImageTk.PhotoImage(pixelNew)
    panel.configure(image=img)
    panel.image = img 

# Brigtness++ - Metode Kali

def brightKali():
    i = 0
    j = 0
    pixel = Image.open(path)
    len1, len2 = pixel.size
    for i in range(len1):
        for j in range(len2):
            r,g,b = pixel.getpixel((i,j))
            r = r*2
            g = g*2
            b = b*2
            pixel.putpixel((i,j),(r, g, b))
    img = ImageTk.PhotoImage(pixel)
    panel.configure(image=img)
    panel.image = img

# Brigthness-- - Metode Bagi

def brightBagi():
    i = 0
    j = 0
    pixel = Image.open(path)
    len1, len2 = pixel.size
    for i in range(len1):
        for j in range(len2):
            r,g,b = pixel.getpixel((i,j))
            r = r/2
            g = g/2
            b = b/2
            pixel.putpixel((i,j),(r, g, b))
    img = ImageTk.PhotoImage(pixel)
    panel.configure(image=img)
    panel.image = img

# Brightness++ - Metode Tambah

def brightTambah():
    i = 0
    j = 0
    pixel = Image.open(path)
    len1, len2 = pixel.size
    for i in range(len1):
        for j in range(len2):
            r,g,b = pixel.getpixel((i,j))
            r = r+r
            g = g+g
            b = b+b
            pixel.putpixel((i,j),(r, g, b))
    img = ImageTk.PhotoImage(pixel)
    panel.configure(image=img)
    panel.image = img

# Brightness-- - Metode Kurang

def brightKurang():
    i = 0
    j = 0
    pixel = Image.open(path)
    len1, len2 = pixel.size
    for i in range(len1):
        for j in range(len2):
            r,g,b = pixel.getpixel((i,j))
            r = r-(r/2)
            g = g-(g/2)
            b = b-(b/2)
            pixel.putpixel((i,j),(r, g, b))
    img = ImageTk.PhotoImage(pixel)
    panel.configure(image=img)
    panel.image = img

# Task 2

# Smaller Image Function

def makeSmaller():
    pixel = Image.open(path)
    len1, len2 = pixel.size
    pixelNew = Image.new("RGB", (len1/2, len2/2))
    x = 0
    y = 0
    for i in range(len1/2):
        for j in range(len2/2):
            r, g, b = pixel.getpixel((x, y))
            pixelNew.putpixel((i,j), (r, g, b))
            y = y+2
        x = x+2
        y = 0
    img = ImageTk.PhotoImage(pixelNew)
    panel.configure(image=img)
    panel.image = img 

# Bigger Image Function

def makeBigger():
    i = 0
    j = 0
    pixel = Image.open(path)
    len1, len2 = pixel.size
    pixelNew = Image.new("RGB", (len1*2, len2*2))
    x = 0
    y = 0
    for i in range(len1):
        for j in range(len2):
            r, g, b = pixel.getpixel((i, j))
            pixelNew.putpixel((x,y), (r, g, b))
            pixelNew.putpixel((x+1,y), (r, g, b))
            pixelNew.putpixel((x,y+1), (r, g, b))
            pixelNew.putpixel((x+1,y+1), (r, g, b))
            y = y+2
        x = x+2
        y = 0
    img = ImageTk.PhotoImage(pixelNew)
    panel.configure(image=img)
    panel.image = img

# Grayscale Function

def makeGrayScale():
    i = 0
    j = 0
    pixel = Image.open(path)
    len1, len2 = pixel.size
    for i in range(len1):
        for j in range(len2):
            r,g,b = pixel.getpixel((i,j))
            grey = (r + g + b) / 3
            pixel.putpixel((i,j),(grey, grey, grey))
    img = ImageTk.PhotoImage(pixel)
    panel.configure(image=img)
    panel.image = img

# Task 6

def on_configure(event):
    canvas.configure(scrollregion=canvas.bbox('all'))

def findRegion(x, y, maxX, maxY, rStart, gStart, bStart, th, pixel, pixelNew):
    if (x-1>=0):
        r, g, b = pixel.getpixel((x-1, y))
        if ((r>=(rStart-th) and r<=(rStart+th)) and (g>=(gStart-th) and g<=(gStart+th)) and (b>=(bStart-th) and b<=(bStart+th))):
            rN, gN, bN = pixelNew.getpixel((x-1, y))
            if (rN!=255 or gN!=255 or bN!=255):
                pixelNew.putpixel((x-1, y), (255, 255, 255))
                findRegion(x+1, y, maxX, maxY, rStart, gStart, bStart, th, pixel, pixelNew)
    if (x+1<=maxX):
        r, g, b = pixel.getpixel((x+1, y))
        if ((r>=(rStart-th) and r<=(rStart+th)) and (g>=(gStart-th) and g<=(gStart+th)) and (b>=(bStart-th) and b<=(bStart+th))):
            rN, gN, bN = pixelNew.getpixel((x+1, y))
            if (rN!=255 or gN!=255 or bN!=255):
                pixelNew.putpixel((x+1, y), (255, 255, 255))
                findRegion(x+1, y, maxX, maxY, rStart, gStart, bStart, th, pixel, pixelNew)
    if (y-1>=0):
        r, g, b = pixel.getpixel((x, y-1))
        if ((r>=(rStart-th) and r<=(rStart+th)) and (g>=(gStart-th) and g<=(gStart+th)) and (b>=(bStart-th) and b<=(bStart+th))):
            rN, gN, bN = pixelNew.getpixel((x, y-1))
            if (rN!=255 or gN!=255 or bN!=255):
                pixelNew.putpixel((x, y-1), (255, 255, 255))
                findRegion(x, y-1, maxX, maxY, rStart, gStart, bStart, th, pixel, pixelNew)
    if (y+1<=maxY):
        r, g, b = pixel.getpixel((x, y+1))
        if ((r>=(rStart-th) and r<=(rStart+th)) and (g>=(gStart-th) and g<=(gStart+th)) and (b>=(bStart-th) and b<=(bStart+th))):
            rN, gN, bN = pixelNew.getpixel((x, y+1))
            if (rN!=255 or gN!=255 or bN!=255):
                pixelNew.putpixel((x, y+1), (255, 255, 255))
                findRegion(x, y+1, maxX, maxY, rStart, gStart, bStart, th, pixel, pixelNew)

# Region Growth Function

def regionGrowth():
    threshold1 = 0
    coordX = 0
    coordY = 0
    if (inputThresholdBase2.get()!=''):
        threshold1 = int(inputThresholdBase2.get())
    if (inputStartValueX.get()!=''):
        coordX = int(inputStartValueX.get())
    if (inputStartValueY.get()!=''):
        coordY = int(inputStartValueY.get())
    # print("{} - {} - {}".format(threshold1, coordX, coordY))
    pixel = Image.open(path)
    len1, len2 = pixel.size
    pixelNew = Image.new('RGB',(len1, len2))
    r, g, b = pixel.getpixel((coordX, coordY))
    findRegion(coordX, coordY, len1, len2, r, g, b, threshold1, pixel, pixelNew)
    img = ImageTk.PhotoImage(pixelNew)
    panel.configure(image=img)
    panel.image = img

# Threshold Base

def thresholdBase():
    startValue = 0
    threshold2 = 0
    if (inputStartValue.get()!=''):
        startValue = int(inputStartValue.get())
    if (inputThresholdBase.get()!=''):
        threshold2 = int(inputThresholdBase.get())
    # print("{} - {}".format(startValue, threshold2))
    pixel = Image.open(path)
    len1, len2 = pixel.size
    pixelNew = Image.new('RGB',(len1, len2))
    for i in range(len1):
        for j in range(len2):
            r, g, b = pixel.getpixel((i,j))
            if ((r>=(startValue-threshold2) and r<=(startValue+threshold2)) and (g>=(startValue-threshold2) and g<=(startValue+threshold2)) and (b>=(startValue-threshold2) and b<=(startValue+threshold2))):
                pixelNew.putpixel((i, j), (255, 255, 255))
    img = ImageTk.PhotoImage(pixelNew)
    panel.configure(image=img)
    panel.image = img

# Task 1

def uploadImage():
    global path
    path = eg.fileopenbox()
    img2 = ImageTk.PhotoImage(Image.open(path))
    panel.configure(image=img2)
    panel.image = img2

# Main Program

master = Tk()

master.title("Tugas Besar - Pengolahan Citra Digital")

canvas = Canvas(master)
canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)

scrollbar = Scrollbar(master, command=canvas.yview)
scrollbar.pack(side=LEFT, fill='y')

canvas.configure(yscrollcommand = scrollbar.set)

canvas.bind('<Configure>', on_configure)

frame = Frame(canvas)
canvas.create_window((0,0), window=frame, anchor='nw')

text = Label(frame, text="\nTugas Besar - Pengolahan Citra Digital\n\n=====================\n\nMuhammad Satrio Wicaksono\n1301150052\n\n=====================\n\nSilahkan upload gambar dengan menekan tombol dibawah ini\n\n")
text.pack()

buttonBrowseFile = Button(frame, text="Upload Gambar", command = uploadImage)
buttonBrowseFile.pack()

img = ImageTk.PhotoImage(Image.open(path))

panel = Label(frame, image = img)

panel.pack()

textLine = Label(frame, text="\n========\nTask 2\n=========\n")
textLine.pack()

buttonGrayScale = Button(frame, text="Make Grey", command = makeGrayScale)
buttonGrayScale.pack()

buttonBigger = Button(frame, text="Make Bigger", command = makeBigger)
buttonBigger.pack()

buttonSmaller = Button(frame, text="Make Smaller", command = makeSmaller)
buttonSmaller.pack()

text3 = Label(frame, text="\n========\nTask 3\n=========\n")

text3.pack()

buttonGeserKiri = Button(frame, text="Geser Kiri", command = geserKiri)
buttonGeserKiri.pack()

buttonBigger = Button(frame, text="Bright++ (Kali)", command = brightKali)
buttonBigger.pack()

buttonSmaller = Button(frame, text="Bright++ (Tambah)", command = brightTambah)
buttonSmaller.pack()

buttonBigger = Button(frame, text="Bright-- (Bagi)", command = brightBagi)
buttonBigger.pack()

buttonSmaller = Button(frame, text="Bright-- (Kurang)", command = brightKurang)
buttonSmaller.pack()

text4 = Label(frame, text="\n========\nTask 4\n=========\n")

text4.pack()

buttonHistogram = Button(frame, text="Show Histogram", command=histogram)
buttonHistogram.pack()

text5 = Label(frame, text="\n========\nTask 5\n=========\n")

text5.pack()

buttonEdge = Button(frame, text="Edge Detection", command=edgeDetection)
buttonEdge.pack()

buttonBlur = Button(frame, text="Blur", command=blur)
buttonBlur.pack()

buttonSharp = Button(frame, text="Sharp", command=sharp)
buttonSharp.pack()

text6 = Label(frame, text="\n========\nTask 6\n=========\n")

text6.pack()

textTitle = Label(frame, text="\n===============\n\nThreshold Base Method\n")
textTitle.pack()

textInput1 = Label(frame, text="Threshold")
textInput1.pack()

inputThresholdBase = Entry(frame, width=10)
inputThresholdBase.pack()
inputThresholdBase.focus_set()

textInput2 = Label(frame, text="Value")
textInput2.pack()

inputStartValue = Entry(frame, width = 10)
inputStartValue.pack()
inputStartValue.focus_set()

buttonMethod1 = Button(frame, text="Proccess", command = thresholdBase)
buttonMethod1.pack()

textTitle2 = Label(frame, text="\n===============\n\nRegion Growth Method\n")
textTitle2.pack()

textInput3 = Label(frame, text="Threshold")
textInput3.pack()

inputThresholdBase2 = Entry(frame, width=10)
inputThresholdBase2.pack()
inputThresholdBase2.focus_set()

textInput4 = Label(frame, text="Coordinat X Start:")
textInput4.pack()

inputStartValueX = Entry(frame, width = 10)
inputStartValueX.pack()
inputStartValueX.focus_set()

textInput4 = Label(frame, text="Coordinat Y Start:")
textInput4.pack()

inputStartValueY = Entry(frame, width = 10)
inputStartValueY.pack()
inputStartValueY.focus_set()

buttonMethod2 = Button(frame, text="Proccess", command = regionGrowth)
buttonMethod2.pack()

mainloop()