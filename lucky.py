from tkinter import *
from random import sample

# script file modifier to include image
def resource_path(relative_path):
    absolute_path = os.path.abspath(__file__)
    root_path = os.path.dirname(absolute_path)
    base_path = getattr(sys, '_MEIPASS', root_path)
    return os.path.join(base_path, relative_path)

# create objects - window and logo
window = Tk()
img = PhotoImage(file = resource_path('lotto.gif'))

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

# dynamic properties

    # generates numbers
def pick():
    nums = sample(range(1, 60), 6)
    label1.configure(text = nums[0])
    label2.configure(text = nums[1])
    label3.configure(text = nums[2])
    label4.configure(text = nums[3])
    label5.configure(text = nums[4])
    label6.configure(text = nums[5])
    getBtn.configure(state = DISABLED)
    resBtn.configure(state = NORMAL)

    # revert numbers back to ellipses
def reset():
    label1.configure(text='...')
    label2.configure(text='...')
    label3.configure(text='...')
    label4.configure(text='...')
    label5.configure(text='...')
    label6.configure(text='...')
    getBtn.configure(state = NORMAL)
    resBtn.configure(state = DISABLED)

    # assign functions to the buttons
getBtn.configure(command = pick)
resBtn.configure(command = reset)

# loop sustains the window
window.mainloop()