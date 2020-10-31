from tkinter import*

counter = 0
minutes = 0
seconds = 0
can = False

def start():
    global minutes
    global seconds
    global can
    if mins.get() and sec.get():
        can = True
        minutes = (int)(mins.get())
        seconds = (int)(sec.get())
        on_timeout()
def stop():
    global can
    can = False
    result['text'] = "00 : 00"
    return
def on_timeout():
    global minutes
    global seconds
    global can
    if not can:
        return
    if minutes == 0 and seconds == 0:
        print('\a')
        can = False
        result['text'] = "00 : 00"
        return
    elif seconds == 0:
        minutes -=1
        seconds = 59
    else:
        seconds -=1
    result['text'] = (str)(minutes) + " : " + (str)(seconds)
    root.after(1000, on_timeout)
        
root = Tk()
root.title("The timer on Tkinter")
root.geometry("135x115")
label1 = Label( text = "Put the time")
label1.place(x=30, y =5)
label2 = Label(text = "Minutes")
label2.place(x = 10, y = 30, height = 10, width = 50)
label3 = Label(text = "Seconds")
label3.place(x = 70, y = 30, height = 10, width = 50)
mins = Entry(width = 10, justify = CENTER)
mins.place(x = 20, y = 50, height = 20, width = 30)
sec = Entry(width = 10, justify = CENTER)
sec.place(x = 80, y = 50, height = 20, width = 30)
result = Label(text = "00 : 00", justify = CENTER, font=('Times New Roman bold', 10, 'bold'))
result.place(x = 40, y = 70, height = 20, width = 50)
button1 = Button(text = "Start",command = start)
button1.place(x = 10, y = 90, height = 20, width = 50)
button2 = Button(text = "Stop", command = stop)
button2.place(x = 70, y = 90, height = 20, width = 50)

root.mainloop()

