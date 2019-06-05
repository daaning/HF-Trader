
# bokeh serve --show graph.py
from bokeh.plotting import figure, curdoc
from bokeh.driving import linear
import random
import database

p = figure(plot_width=1600, plot_height=800)
r1 = p.line([], [], color="firebrick", line_width=2)
r2 = p.line([], [], color="navy", line_width=2)
r3 = p.line([], [], color="green", line_width=2)
r4 = p.line([], [], color="blue", line_width=2)
r5 = p.line([], [], color="yellow", line_width=2)
r6 = p.line([], [], color="red", line_width=2)
r7 = p.line([], [], color="black", line_width=2)

ds1 = r1.data_source
ds2 = r2.data_source
ds3 = r3.data_source
ds4 = r4.data_source
ds5 = r5.data_source
ds6 = r6.data_source
ds7 = r7.data_source

data = database.get_predictions(1)
print(data)

@linear()
def update(step):
    data = database.get_predictions(1)
    print(data)
    ds1.data['x'].append(data[0])
    ds1.data['y'].append(data[1])
    ds2.data['x'].append(data[0])
    ds2.data['y'].append(data[2])
    ds3.data['x'].append(data[0])
    ds3.data['y'].append(data[3])
    ds4.data['x'].append(data[0])
    ds4.data['y'].append(data[4])
    ds5.data['x'].append(data[0])
    ds5.data['y'].append(data[5])
    ds6.data['x'].append(data[0])
    ds6.data['y'].append(data[6])
    ds7.data['x'].append(data[0])
    ds7.data['y'].append(data[7])



    if len(ds1.data1['x']) > 100:
        ds1.data['x'].pop(0)
        ds1.data['y'].pop(0)
        ds2.data['x'].pop(0)
        ds2.data['y'].pop(0)
        ds3.data['x'].pop(0)
        ds3.data['y'].pop(0)
        ds4.data['x'].pop(0)
        ds4.data['y'].pop(0)
        ds5.data['x'].pop(0)
        ds5.data['y'].pop(0)
        ds6.data['x'].pop(0)
        ds6.data['y'].pop(0)
        ds7.data['x'].pop(0)
        ds7.data['y'].pop(0)

    ds1.trigger('data', ds1.data, ds1.data)
    ds2.trigger('data', ds2.data, ds2.data)
    ds3.trigger('data', ds3.data, ds3.data)
    ds4.trigger('data', ds4.data, ds4.data)
    ds5.trigger('data', ds5.data, ds5.data)
    ds6.trigger('data', ds6.data, ds6.data)
    ds7.trigger('data', ds7.data, ds7.data)


curdoc().add_root(p)
curdoc().add_periodic_callback(update, 500)