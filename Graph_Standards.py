"""
This code is for plotting graphs, to keep as a reference. Its classes can be imported to any project and from there
the preferred graph style can be selected.
Path of this file on my work Linux computer : '/home/jlarija/Desktop/PycharmProjects/OwnFiles'
"""

import seaborn as sns
from matplotlib import pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "sans-serif",
    "font.sans-serif": ["Helvetica"]})

class SeabornPlots:
    """Mainly for pandas plots, using seaborn that gives automatically color palettes so no colors have to be chosen
    """

    def __init__(self):
        pass

    def scatter(self, dataframe, x_data, y_data, xlabel, title):
        sns.set_style('dark')
        ax = sns.scatterplot(data=dataframe, x=x_data, y=y_data, hue=str(y_data), palette='pastel', legend=False)
        plt.grid()
        ax.set(xlabel=str(xlabel), ylabel=None, title=title)
        plt.tight_layout()

        return plt.show()

    def scatter_darkbackground(self, x_data, y_data, xlabel, ylabel, title, color):
        sns.set(style="darkgrid", context="talk")
        plt.style.use("dark_background")
        ax = sns.scatterplot(x=x_data, y=y_data, color=str(color), legend=False)
        ax.set(xlabel=str(xlabel), ylabel=str(ylabel), title=title)
        ax.tick_params(grid_linestyle=':')
        plt.tight_layout()
        return plt.show()

    def lineplot(self, x, y, xlabel, ylabel, title):
        sns.set_style('dark')

        plt.plot(x, y, color='#DDA0DD', marker='o')
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.yticks(y)
        plt.grid()
        plt.tight_layout()

        return plt.show()


class MatplotlibPlots:

    def __init__(self):
        pass

    def marker_plot(self, x, y, xlabel, ylabel, color, title, label):
        plt.scatter(x, y, color=color, label=label,
                    marker='.')  # list of markers at https://matplotlib.org/stable/api/markers_api.html

        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.grid()
        plt.title(title)

        plt.tight_layout()

        return plt.show()

    def legend_side_multiplecol(self, xtab, ytab, colors, label_lists, legend_columns, xlabel, ylabel, title):
        color_list_complete = colors

        color_list = color_list_complete[:len(xtab)]  # only select as many colors as points you are plotting

        fig, ax = plt.subplots(1, 1)

        index = 0

        for i in range(0, len(color_list)):  # Make the plot for each label

            ax.scatter(xtab[index], ytab[index], label=label_lists[index],
                       color=color_list[index])

            index += 1

        box = ax.get_position()
        ax.set_position([box.x0, box.y0, box.width * 0.88, box.height])
        ax.legend(ncol=legend_columns, loc='center left', bbox_to_anchor=(1, 0.5))
        ax.grid()
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.set_title(title, loc='left')

        return plt.show(), fig


def save_plot(location_name, figure):
    save_figure = PdfPages(str(location_name))
    figure.savefig(save_figure, dpi=300, format='pdf', transparent=True)
    save_figure.close()

    return 'Figure saved'


def TUDelft_colors():
    cyan = '#00A6D6'
    dark_blue = '#0066a2'
    light_blue = '#82d7c6'
    green = '#00a390'
    light_green = '#99d28c'
    red = '#c3312f'
    orange = '#eb7245'
    yellow = '#f1be3e'

    return cyan, dark_blue, light_blue, light_green, green, red, orange, yellow


'''-----------SPACE FOR ATTEMPTS-------------'''
if __name__== 'Main':

    x = [0,1,2]
    y=[0,1,2]
    plot = SeabornPlots()
    ciao = plot.scatter_darkbackground(x,y,'c','c','c',TUDelft_colors()[0])