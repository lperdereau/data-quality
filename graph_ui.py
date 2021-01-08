import matplotlib.pyplot as plt
from matplotlib.widgets import Button
from numpy import isnan, nanmin, nanmax, searchsorted, arange, array, append


class Cursor(object):
    def __init__(self, ax, x, y):
        self.ax = ax
        self.ly = ax.axvline(color='k', alpha=0.2)  # the vert line
        self.marker, = ax.plot([0],[0], marker="o", color="crimson", zorder=3) 
        self.x = x
        self.y = y
        self.txt = ax.text(0.7, 0.9, '')

    def mouse_move(self, event):
        if not event.inaxes: return
        x, y = event.xdata, event.ydata
        indx = searchsorted(self.x, [x])[0]
        x = self.x[indx]
        y = self.y[indx]
        self.ly.set_xdata(x)
        self.marker.set_data([x],[y])
        self.txt.set_text(f'jour {x}, {y}°C')
        self.txt.set_color("crimson")
        self.txt.set_position((x,y+1))
        self.ax.figure.canvas.draw_idle()

def generate_ui(months, array_climat):

    year_array = array([])
    for i, month in enumerate(months, start=0):
        year_array = append(year_array, array_climat[:, i])
    year_array = year_array[~isnan(year_array)]

    month = 0
    fig, ax = plt.subplots()

    plt.subplots_adjust(bottom=0.2)
    
    title = plt.title(f"Vue du mois : {months[month]}")
    plt.xlabel('Jours')
    plt.ylabel('Degré')
    
    plt.axis([0, 32, nanmin(year_array)-5, nanmax(year_array)+5])
    plt.grid(True)
    l, = plt.plot(range(0, 31, 1), array_climat[:, month], "b:o", lw=2)
    ax.set_xlim(right=32)
    x = [x for x in arange(1, 32) if x%5==0 ]
    ax.set_xticks(x)
    ax.set_xticklabels(x)
    l.set_xdata(range(1, 32))

    class Index:
        ind = 0

        def __init__(self, cursor):
            self.cursor = cursor

        def next(self, event):
            if self.ind < 11:
                self.ind += 1
                title.set_text(f"Vue du mois : {months[self.ind]}")
                l.set_ydata(array_climat[:, self.ind])
                self.cursor.x = arange(len(array_climat[:, self.ind]))
                self.cursor.y = array_climat[:, self.ind]
                plt.draw()
            elif self.ind == 11:
                self.ind += 1
                title.set_text(f"Vue de l'année")
                x = [x for x in arange(0, 365) if x%30==0 ]
                ax.set_xlim(right=366)
                ax.set_xticks(x)
                ax.set_xticklabels(x)
                l.set_xdata(range(1, 366))
                l.set_ydata(year_array)
                self.cursor.x = arange(1, 366)
                self.cursor.y = year_array
                plt.draw()

        def prev(self, event):
            if self.ind > 0:
                self.ind -= 1
                title.set_text(f"Vue du mois : {months[self.ind]}")
                l.set_ydata(array_climat[:, self.ind])
                self.cursor.x = arange(len(array_climat[:, self.ind]))
                self.cursor.y = array_climat[:, self.ind]
                if self.ind == 11:
                    x = [x for x in arange(0, 31) if x%5==0 ]
                    ax.set_xlim(right=32)
                    ax.set_xticks(x)
                    ax.set_xticklabels(x)
                    l.set_xdata(range(1, 32))
                plt.draw()

    days = arange(0, 31)
    celsius_degree = array_climat[days, 0]
    cursor = Cursor(ax, days, celsius_degree)
    plt.connect('motion_notify_event', cursor.mouse_move)

    callback = Index(cursor)
    axprev = plt.axes([0.7, 0.05, 0.1, 0.075])
    axnext = plt.axes([0.81, 0.05, 0.1, 0.075])
    bnext = Button(axnext, 'Next')
    bnext.on_clicked(callback.next)
    bprev = Button(axprev, 'Previous')
    bprev.on_clicked(callback.prev)
    plt.show()