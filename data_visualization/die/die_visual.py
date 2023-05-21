from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

die = Die()

results = []
for roll_num in range(1000):
    res = die.roll()
    results.append(res)

# Проаналізувати результати
freauencies = []
for value in range(1, die.num_slides+1):
    frequency = results.count(value)
    freauencies.append(frequency)

# Візуалізувати результати
x_values = list(range(1, die.num_slides+1))
data = [Bar(x=x_values, y=freauencies)]

x_axis_config = {'title': 'Результат'}
y_axis_config = {'title': 'Частота результату'}
my_layout = Layout(title='Результати жбурляння шестигранного кубика 1000 разів.', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')