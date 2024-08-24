from tkinter import *
import customtkinter

#set theme and colour
customtkinter.set_appearance_mode("dark")  # default
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"


def create_watchlists(parent_frame):
    watchlists = customtkinter.CTkScrollableFrame(parent_frame,
    label_text='Watchlists')
    watchlists.pack(fill='x')

    button_1 = customtkinter.CTkButton(watchlists, text='Not Developed Yet')
    button_1.pack(pady=40, expand='True')





