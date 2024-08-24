import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import tkinter as tk

def create_chart(parent_frame, file_name):
    df = pd.read_csv(file_name)

    open_array = np.array([])
    close_array = np.array([])
    high_array = np.array([])
    low_array = np.array([])
    lines = 0

    for i in range(len(df)):
        open = df.iloc[i, 1]
        close = df.iloc[i, 4]
        high = df.iloc[i, 2]
        low = df.iloc[i, 3]
        open_array = np.append(open_array, open)
        close_array = np.append(close_array, close)
        high_array = np.append(high_array, high)
        low_array = np.append(low_array, low)
        lines = lines+1

    stock_prices = pd.DataFrame({'open': open_array, 
                                 'close': close_array, 
                                 'high': high_array, 
                                 'low': low_array}, 
                                index=pd.date_range("2023-02-06", periods=lines, freq="d")) 

    fig = Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)

    fig.patch.set_facecolor('#212121')
    ax.set_facecolor('#212121')

    up = stock_prices[stock_prices.close >= stock_prices.open] 
    down = stock_prices[stock_prices.close < stock_prices.open] 

    up_color = 'green'
    down_color = 'red'

    width = .1
    width2 = .01

    up_rects = ax.bar(up.index, up.close-up.open, width, bottom=up.open, color=up_color) 
    ax.bar(up.index, up.high-up.close, width2, bottom=up.close, color=up_color) 
    ax.bar(up.index, up.low-up.open, width2, bottom=up.open, color=up_color) 

    down_rects = ax.bar(down.index, down.close-down.open, width, bottom=down.open, color=down_color) 
    ax.bar(down.index, down.high-down.open, width2, bottom=down.open, color=down_color) 
    ax.bar(down.index, down.low-down.close, width2, bottom=down.close, color=down_color) 

    ax.tick_params(axis='x', colors='white', rotation=30)
    ax.tick_params(axis='y', colors='white')

    for spine in ax.spines.values():
        spine.set_color('white')

    # Add the canvas without the toolbar
    canvas = FigureCanvasTkAgg(fig, master=parent_frame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(fill='both', expand=True)

    # Bind mouse motion event
    canvas.mpl_connect('motion_notify_event', lambda event: on_hover(event, up_rects, down_rects))
    # Bind scroll event for zooming
    canvas.mpl_connect('scroll_event', lambda event: on_zoom(event, ax))
    # Bind mouse button release event for panning
    canvas.mpl_connect('button_press_event', lambda event: on_pan_start(event, ax))
    canvas.mpl_connect('button_release_event', lambda event: on_pan_end(event, ax))
    canvas.mpl_connect('motion_notify_event', lambda event: on_pan(event, ax, canvas_widget))

    return canvas


def on_hover(event, up_rects, down_rects):
    if event.inaxes is not None:
        for rect in up_rects + down_rects:
            if rect.contains(event)[0]:
                rect.set_color('yellow')
            else:
                rect.set_color('green' if rect in up_rects else 'red')
        event.canvas.draw()

def on_zoom(event, ax):
    base_scale = 1.2
    cur_xlim = ax.get_xlim()
    cur_ylim = ax.get_ylim()

    xdata = event.xdata  # get event x location
    ydata = event.ydata  # get event y location

    if event.button == 'up':
        # Zoom in
        scale_factor = 1 / base_scale
    elif event.button == 'down':
        # Zoom out
        scale_factor = base_scale
    else:
        # Unknown event, just return
        return

    # Set new limits
    new_width = (cur_xlim[1] - cur_xlim[0]) * scale_factor
    new_height = (cur_ylim[1] - cur_ylim[0]) * scale_factor

    relx = (cur_xlim[1] - xdata) / (cur_xlim[1] - cur_xlim[0])
    rely = (cur_ylim[1] - ydata) / (cur_ylim[1] - cur_ylim[0])

    ax.set_xlim([xdata - new_width * (1 - relx), xdata + new_width * (relx)])
    ax.set_ylim([ydata - new_height * (1 - rely), ydata + new_height * (rely)])

    event.canvas.draw()

def on_pan_start(event, ax):
    if event.button == 1:  # Left mouse button
        ax._pan_start = event.x, event.y
        ax._pan_xlim = ax.get_xlim()
        ax._pan_ylim = ax.get_ylim()

def on_pan(event, ax, canvas_widget):
    if hasattr(ax, '_pan_start') and event.button == 1:  # Left mouse button and dragging
        dx = event.x - ax._pan_start[0]
        dy = event.y - ax._pan_start[1]

        cur_xlim = ax._pan_xlim
        cur_ylim = ax._pan_ylim

        # Invert the direction for panning
        ax.set_xlim([cur_xlim[0] - dx * (cur_xlim[1] - cur_xlim[0]) / canvas_widget.winfo_width(),
                     cur_xlim[1] - dx * (cur_xlim[1] - cur_xlim[0]) / canvas_widget.winfo_width()])
        ax.set_ylim([cur_ylim[0] - dy * (cur_ylim[1] - cur_ylim[0]) / canvas_widget.winfo_height(),
                     cur_ylim[1] - dy * (cur_ylim[1] - cur_ylim[0]) / canvas_widget.winfo_height()])

        event.canvas.draw()

def on_pan_end(event, ax):
    if hasattr(ax, '_pan_start') and event.button == 1:  # Left mouse button
        del ax._pan_start
        del ax._pan_xlim
        del ax._pan_ylim