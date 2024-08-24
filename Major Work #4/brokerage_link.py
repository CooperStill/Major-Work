from tkinter import *
import customtkinter

customtkinter.set_appearance_mode("dark")  
customtkinter.set_default_color_theme("dark-blue")



def create_link(parent_frame):
    button = customtkinter.CTkButton(parent_frame, text='Brokerage Link')
    button.pack(padx=20, side='left', fill='x', expand='True')

