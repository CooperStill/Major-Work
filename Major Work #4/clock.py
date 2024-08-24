from tkinter import *
import time



def create_clock(parent_frame):
    def clock():
        hour = time.strftime('%H')
        minute = time.strftime('%M')
        second = time.strftime('%S')

        my_label.config(text=hour + ':' + minute + ':' + second, bg='#212121', fg='white', font=('Times New Roman', 30))
        my_label.after(1000, clock)




    def update():
        my_label.config(text='New Text')

    my_label = Label(parent_frame, text='')
    my_label.pack(pady=20, padx=20, side='left', expand='True')


    clock()

