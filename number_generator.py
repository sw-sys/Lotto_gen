from tkinter import *

# create objects - window and logo
window = Tk()
img = PhotoImage(file = 'lotto.gif')

# create widgets for numbers and buttons
imgLbl = Label(window, image = img)
label1 = Label(window,relief = 'groove', width = 2)
label2 = Label(window, relief = 'groove', width = 2)
label3 = Label(window, relief ='groove', width = 2)
label4 = Label(window, relief = 'groove', width = 2)
label5 = Label(window, relief = 'groove', width = 2)
label6 = Label(window, relief = 'groove', width = 2)
getBtn = Button(window)
resBtn = Button(window)

# place widgets in window using grid layout mgr
# padx arg adds padding of x value to left and right sides
imgLbl.grid(row = 1, column = 1, rowspan = 2)
label1.grid(row = 1, column = 2, padx = 10)
label2.grid(row = 1, column = 3, padx = 10)
label3.grid(row = 1, column = 4, padx = 10)
label4.grid(row = 1, column = 5, padx = 10)
label5.grid(row = 1, column = 6, padx = 10)
label6.grid(row = 1, column = 7, padx = (10, 20))

getBtn.grid(row = 2, column = 2, columnspan = 4)
resBtn.grid(row = 2, column = 6, columnspan = 2)

# static properties - never change
window.title('Lotto Number Picker')
    # prevents window resizing (width, height)
window.resizable(0,0)
getBtn.configure(text = 'Get My Lucky Numbers')
resBtn.configure(text = 'Reset')

#initial properties for numbers
label1.configure(text='...')
label2.configure(text='...')
label3.configure(text='...')
label4.configure(text='...')
label5.configure(text='...')
label6.configure(text='...')
resBtn.configure(state = DISABLED)

# loop sustains the window
window.mainloop()