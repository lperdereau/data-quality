# -*- coding: utf-8 -*-
import argparse
import ntpath
import matplotlib.pyplot as plt
from numpy import isnan, nanmin, nanmax, genfromtxt, transpose, searchsorted

parser = argparse.ArgumentParser()
parser.add_argument("--csv", help="List of path to the csv files separated by a coma", required=True)
args = parser.parse_args()

files = args.csv.split(',')
files_name = [ntpath.basename(file).split('.')[0] for file in files]

class Cursor(object):
    def __init__(self, ax, x, y, color, i, j):
        self.ax = ax
        self.ly = ax.axvline(color='k', alpha=0.2)  # the vert line
        self.marker, = ax.plot([0],[0], marker="o", color=color, zorder=3)
        self.color = color
        self.x = x
        self.y = y
        self.i = i
        self.j = j
        self.txt = ax.text(0.7, 0.9, '')

    def mouse_move(self, event):
        if not event.inaxes: return
        x, y = event.xdata, event.ydata
        indx = searchsorted(self.x, [x])[0]
        x = self.x[indx+1]
        y = self.y[indx]
        self.ly.set_xdata(x)
        self.marker.set_data([x],[y])
        self.txt.set_text(f'jour {x}, {y}°C')
        self.txt.set_color(self.color)
        self.txt.set_position((0,self.j-(3*self.i)-2))
        self.ax.figure.canvas.draw_idle()

def generate_year(file):
    year = transpose(genfromtxt(file, delimiter=';', dtype=float, skip_header=True)).flatten()
    return year[~isnan(year)]

def generate_ui(years, files_name):
    fig, ax = plt.subplots()
    plt.subplots_adjust(bottom=0.2)
    
    plt.title(f"Comparaison")
    plt.xlabel('Jours')
    plt.ylabel('Degré')
    
    min_temp = nanmin(years)
    max_temp = nanmax(years)

    plt.axis([1, 366, min_temp-5, max_temp+5])
    plt.grid(True)

    days = range(0, 365)
    cursors = []
    for i, year in enumerate(years):
        plot = plt.plot(year, label=files_name[i])
        celsius_degree = year[days]
        cursors.append(Cursor(ax, days, celsius_degree, plot[0].get_color(), i, min_temp-6))
        plt.connect('motion_notify_event', cursors[i].mouse_move)

    plt.legend()
    plt.show()


years = [generate_year(file) for file in files]
generate_ui(years, files_name)