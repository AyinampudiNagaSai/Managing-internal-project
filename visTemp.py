# -*- coding: utf-8 -*-
"""
Created on Tue May 22 15:48:14 2018

@author: karri
"""

output_file("background.html")

p = figure(plot_width=400, plot_height=400)
p.background_fill_color = "beige"
p.background_fill_alpha = 0.5

p.circle([1, 2, 3, 4, 5], [2, 5, 8, 2, 7], size=10)

# change in axes , removing axes

p.xgrid.grid_line_color = None
p.ygrid.grid_line_color = None

p.xaxis.axis_line_color = None
p.yaxis.axis_line_color = None

p.xaxis.major_label_text_color = None
p.yaxis.major_label_text_color = None

p.xaxis.major_tick_line_color = None  # turn off x-axis major ticks
p.xaxis.minor_tick_line_color = None  # turn off x-axis minor ticks

p.yaxis.major_tick_line_color = None  # turn off y-axis major ticks
p.yaxis.minor_tick_line_color = None  # turn off y-axis minor ticks

#tool bar removal

p.toolbar_location =None

#background colour

p.background_fill_color = "black"

p.sizing_mode='stretch_both'


show(p)