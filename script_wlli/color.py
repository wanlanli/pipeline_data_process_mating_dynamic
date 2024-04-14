
import matplotlib as mpl


def color_base(color_set):
    set_list = []
    for r, g, b in color_set:
        set_list.append((r/255, g/255, b/255))
    set_list = mpl.colors.ListedColormap(set_list)
    return set_list


def color_set5():
    color_set = [(241, 157, 57), (83, 182, 241), (250, 223, 75), (173, 216, 234), (16, 43, 205)]
    set5 = color_base(color_set)
    return set5


def color_pm():
    colors_green_red = [(127, 188, 56), (225, 99, 42)]
    set2 = color_base(colors_green_red)
    return set2


def color_linespace():
    colors_list = [(202, 58, 32), (241, 165, 58), (249, 222, 75), (247, 240, 220), (135, 235, 233), (151, 200, 233)]
    colors_gaudi_list = []
    for r, g, b in colors_list:
        colors_gaudi_list.append((r/255, g/255, b/255))
    line_space = mpl.colors.LinearSegmentedColormap.from_list("", colors_gaudi_list)
    return line_space


COLOR_SET5 = color_set5()
COLOR_SET2 = color_pm()
COLORLINE = color_linespace()
