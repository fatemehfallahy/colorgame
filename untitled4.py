import tkinter
import random
colors = ['yellow','black','pink','blue','green','red','brown','white']
score = 0
timeleft = 30

def startgame(event):
    if timeleft ==30:
        countdown()
    nextcolor()
    
    
def nextcolor():
    global score
    global timeleft
    if timeleft > 0 :
        e.focus_set()
        if e.get().lower() ==colors[1].lower():
            score+=1
        e.delete(0,END)
        random,shuffel(colors)
        
        label.config(fg= str(colors[1]), text = str(colors[0]))
        scorelabel.config(text= 'امتیاز: '+ str(score), font=('Tahoma 17'))
        
def coundown():
    global timeleft
    if timeleft > 0:
        timeleft -= 1
        timeglobal.config(text='زمان: '+ str(timeleft), font =('Tahoma 17'))
        timeglobal.after(1000, coundown)
        
        
win=tkinter.Tk()
win.geometry('400x270')
win.resizable(0,0)
win.title('بازی رنگ ها')

scorelabel = tkinter.Label(win, text= 'Enter را بزنید و بازی را شروع کنید',font='Tahoma 17')
scorelabel.pack()

e=tkinter.Entry(win ,width = 20)
e.pack() 
e.focus_set()

win.baind('<Return>',startgame)

win.mainloop() 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    