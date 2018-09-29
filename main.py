import tkinter
import calendar
import time
import tkfontchooser
from tkinter import ttk
from datetime import datetime


def sequence(*functions):  # to run 2 or more functions on button click
    for function in functions:
        function()


def update(y, m, tx, curdate):  # generate calendar with right colors
    global holidays
   # print type(curdate)
    calstr = calendar.month(y, m)
    tx.configure(state=tkinter.NORMAL)
    tx.delete('0.0', tkinter.END)  # remove previous calendar
    tx.insert(tkinter.INSERT, calstr)
    for i in range(2, 9):
        tx.tag_add("others", '{}.0'.format(i), '{}.end'.format(i))  # tag days for coloring

        if len(tx.get('{}.0'.format(i), '{}.end'.format(i))) == 20:
            tx.tag_add("sun", '{}.end-2c'.format(i), '{}.end'.format(i))

    tx.tag_config("sun", foreground="#fb4622")
    tx.tag_config("others", foreground="#427eb5")
    tx.tag_add("head", '1.0', '1.end')

    for hold in (holidays):
       d = datetime.strptime(hold, '%b %d %Y')


       tt=d.timetuple()
       if tt[0] == y and tt[1] == m:

          index = tx.search(str(tt[2]), '2.0')
          tx.tag_add("hol", index, '{}+2c'.format(index))  # highlight holiday
          tx.tag_config("hol", foreground="#fb4622")


    if curdate[0] == y and curdate[1] == m:
        index = tx.search(str(curdate[2]), '2.0')  # search for today's date
        tx.tag_add("cur", index, '{}+2c'.format(index))  # highlight today's date
        tx.tag_config("cur", background="blue", foreground="white")
    tx.tag_config("head", font=segoe, foreground="#0d8241", justify=tkinter.CENTER)
    tx.configure(state=tkinter.DISABLED)  # make text view not editable


top = tkinter.Tk()
top.title("VTU Calendar")
top.minsize(300, 270)
top.maxsize(200, 200)
logo = tkinter.PhotoImage(file="r.gif")
top.tk.call('wm', 'iconphoto', top._w, logo)
segoe = tkfontchooser.Font(family='Segoe UI')
curtime = time.localtime()
year = tkinter.StringVar()
month = tkinter.StringVar()
yearInt = curtime[0]
monthInt = curtime[1]
dateInt = curtime[2]
HLayout = ttk.PanedWindow(top, orient=tkinter.HORIZONTAL)
ctx = tkinter.Text(top, padx=20, pady=20, bg="#f3e9ae", relief=tkinter.FLAT, height=9,
                   width=20)  # text view to passing to functions
holidays=['Jan 15 2018','Jan 26 2018','Feb 13 2018','Mar 29 2018','Mar 30 2018','Apr 18 2018','May 1 2018','Aug 15 2018','Aug 22 2018',
          'Sep 13 2018','Sep 21 2018','Oct 2 2018','Oct 8 2018','Oct 18 2018','Oct 19 2018','Oct 24 2018','Nov 1 2018','Nov 6 2018',
          'Nov 8 2018','Nov 21 2018','Nov 26 2018','Dec 25 2018']


def nextb():  # on click next button
    global monthInt, yearInt, ctx, curtime
    monthInt += 1
    if monthInt > 12:
        monthInt = monthInt % 12
        yearInt += 1
    update(yearInt, monthInt, ctx, curtime)


def prevb():  # on click previous button
    global monthInt, yearInt, ctx, curtime
    monthInt -= 1
    if monthInt < 1:
        monthInt = 12
        yearInt -= 1
    update(yearInt, monthInt, ctx, curtime)


def okcall():  # ok button click inside go to date window
    global monthInt, yearInt, ctx, curtime
    if (year.get().isdigit() and month.get().isdigit()) and (
                (0 < int(year.get()) < 10000) and (0 < int(month.get()) < 13)):
        yearInt = int(year.get())
        monthInt = int(month.get())
        update(yearInt, monthInt, ctx, curtime)

def holiday():
    t=tkinter.Toplevel()
    t.title("Holidays")
    t.maxsize(300,600)
    t.focus_set()
    HLayout=ttk.PanedWindow(t,orient=tkinter.HORIZONTAL)

    ttk.Label(HLayout, text="15.1.2018:Makara sankranti", font="Time 10 bold").pack()
    ttk.Label(HLayout, text="26.1.2018:Republic day", font="Time 10 bold").pack()
    ttk.Label(HLayout, text="13.2.2018:Mahashivaratri", font="Time 10 bold").pack()
    ttk.Label(HLayout, text="29.3.2018:Mahaveer Jayanti", font="Time 10 bold").pack()
    ttk.Label(HLayout, text="30.3.2018:Good friday", font="Time 10 bold").pack()
    ttk.Label(HLayout, text="18.4.2018:Basav Jayanti", font="Time 10 bold").pack()
    ttk.Label(HLayout, text="1.5.2018:Labour day", font="Time 10 bold").pack()
    ttk.Label(HLayout, text="16.6.2018:Ramzan", font="Time 10 bold").pack()
    ttk.Label(HLayout, text="15.8.2018:Independence day", font="Time 10 bold").pack()
    ttk.Label(HLayout, text="22.8.2018:Bakrid", font="Time 10 bold").pack()
    ttk.Label(HLayout, text="13.9.2018:Ganesh Chaturthi", font="Time 10 bold").pack()
    ttk.Label(HLayout, text="21.9.2018:Moharamm", font="Time 10 bold").pack()
    ttk.Label(HLayout, text="2.10.2018:Mahatma Gandhi Jayanti", font="Time 10 bold").pack()
    ttk.Label(HLayout, text="8.10.2018:Mahalaya Amavasye", font="Time 10 bold").pack()
    ttk.Label(HLayout, text="18.10.2018:Maha Navami/Ayudha pooja", font="Time 10 bold").pack()
    ttk.Label(HLayout, text="19.10.2018:Vijayadashami", font="Time 10 bold").pack()
    ttk.Label(HLayout, text="24.10.2018:Valmiki Jayanti", font="Time 10 bold").pack()
    ttk.Label(HLayout, text="1.11.2018:Kannada Rajyotsava", font="Time 10 bold").pack()
    ttk.Label(HLayout, text="6.11.2018:Naraka Chaturdashi", font="Time 10 bold").pack()
    ttk.Label(HLayout, text="8.11.2018:Deepavali", font="Time 10 bold").pack()
    ttk.Label(HLayout, text="21.11.2018:Id-E-Milad", font="Time 10 bold").pack()
    ttk.Label(HLayout, text="26.11.2018:Kanakadas Jayanti", font="Time 10 bold").pack()
    ttk.Label(HLayout, text="25.12.2018:Cristmas", font="Time 10 bold").pack()
    HLayout.pack()
    t.mainloop()


def gotod():  # go to date window creation
    newtop = tkinter.Toplevel()
    newtop.title("Calendar")
    newtop.maxsize(190, 190)
    newtop.focus_set()
   # newtop.tk.call('wm', 'iconphoto', newtop._w, logo)
    HLayout = ttk.PanedWindow(newtop, orient=tkinter.HORIZONTAL)
    HLayout2 = ttk.PanedWindow(newtop, orient=tkinter.HORIZONTAL)
    yearText = ttk.Label(HLayout, text="Year :")
    yearEdit = ttk.Entry(HLayout, textvariable=year)
    monthText = ttk.Label(HLayout2, text="Month:")
    monthEdit = ttk.Entry(HLayout2, textvariable=month)
    okb = ttk.Button(newtop, text="Ok", command=lambda: sequence(okcall, newtop.destroy))
    yearText.pack(side=tkinter.LEFT)
    yearEdit.pack(side=tkinter.RIGHT)
    monthText.pack(side=tkinter.LEFT)
    monthEdit.pack(side=tkinter.RIGHT)
    HLayout.pack()
    HLayout2.pack()
    okb.pack()
    newtop.mainloop()


update(yearInt, monthInt, ctx, curtime)  # for first run, generate calendar
prev = ttk.Button(HLayout, text="<<", command=prevb)
nex = ttk.Button(HLayout, text=">>", command=nextb)
goto = ttk.Button(top, text="Goto", command=gotod)
holiday = ttk.Button(top, text="Holiday", command=holiday)
menubar = tkinter.Menu(top, relief=tkinter.FLAT)
filemenu = tkinter.Menu(menubar, tearoff=0, relief=tkinter.FLAT)
helpmenu = tkinter.Menu(menubar, tearoff=0, relief=tkinter.FLAT)
filemenu.add_command(label="holiday", command=holiday)
filemenu.add_command(label="Goto", command=gotod)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=top.destroy)
top.config(menu=menubar)
prev.pack(side=tkinter.LEFT)
nex.pack(side=tkinter.RIGHT)
ctx.pack()
HLayout.pack()
top.config(menu=menubar)
goto.pack()
holiday.pack()
top.mainloop()
