import tkinter as tk
from tkinter import ttk
import customtkinter
from market_list import create_market_list
from indicator_list import create_indicator_list
from watchlist import create_watchlists
from clock import create_clock
from alerts import create_alerts
from recently_visited import create_recently_visited
from brokerage_link import create_link
from profile_page import create_profile_page
from chart import create_chart
from indicator_dates import display_dates

customtkinter.set_appearance_mode("dark")  # default
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"
window = customtkinter.CTk()
window_width= window.winfo_screenwidth() 
window_height= window.winfo_screenheight()

window.columnconfigure(0, weight = 1, uniform = 'a')
window.columnconfigure(1, weight = 2, uniform = 'a')
window.columnconfigure(2, weight = 2, uniform = 'a')
window.rowconfigure(0, weight = 1, uniform = 'a')
window.rowconfigure(1, weight = 4, uniform = 'a')
window.rowconfigure(2, weight = 4, uniform = 'a')
window.rowconfigure(3, weight = 3, uniform = 'a')




top_frame = customtkinter.CTkFrame(window)
top_frame.grid(row=0, column=0, sticky='nsew', columnspan=3)

create_clock(top_frame)
create_alerts(top_frame)
create_recently_visited(top_frame)
create_link(top_frame)
create_profile_page(top_frame)

left_frame = customtkinter.CTkFrame(window)
left_frame.grid(row=1, column=0, sticky='nsew', rowspan=3)


chart1_frame = customtkinter.CTkFrame(window)
chart1_frame.grid(row=1, column=1, sticky='nsew', rowspan=2, columnspan=2)

canvas = create_chart(chart1_frame, 'test_data.csv')

create_market_list(left_frame, chart1_frame, canvas)
create_indicator_list(left_frame)
create_watchlists(left_frame)



chart2_frame = customtkinter.CTkFrame(window, fg_color='red')
chart2_frame.grid(row=3, column=2, sticky='nsew')

chart3_frame = customtkinter.CTkFrame(window)
chart3_frame.grid(row=3, column=1, sticky='nsew')

display_dates(chart3_frame)













window.geometry("%dx%d" % (window_width, window_height))
window.title('Major Work')
window.mainloop()