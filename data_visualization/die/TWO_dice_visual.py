from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

quantity = 50_000
die_1 = Die()
die_2 = Die(10)

results = []
for roll_num in range(quantity):
    res = die_1.roll() + die_2.roll()
    results.append(res)



# Проаналізувати результати
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)



# Візуалізувати результати
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of result'}
my_layout = Layout(title=f'Result of rolling D6 adn D10 {quantity} times.', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, 
             filename=f'd{die_1.num_sides}_d{die_2.num_sides}.html') # e.g. d6_d10.html