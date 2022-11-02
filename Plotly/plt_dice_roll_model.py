# https://plotly.com/python/ - examples of charts

from random import randint
from plotly.graph_objs import Bar, Layout
from plotly import offline

class Die():
    """class for die"""

    def __init__(self, num_sides = 6):
        """initialization"""
        self.num_sides = num_sides

    def roll(self):
        """roll the die"""
        return randint(1, self.num_sides)


def main():
    die_1 = Die()
    die_2 = Die(10)

    results = []
    for roll_num in range(50000):
        result = die_1.roll() + die_2.roll()
        results.append(result)

    frequencies  = []
    max_result = die_1.num_sides + die_2.num_sides
    for value in range(2, max_result + 1):
        frequency = results.count(value)
        frequencies.append(frequency)

    # show results
    x_values = list(range(2, max_result + 1))
    data = [Bar(x = x_values, y = frequencies)]

    x_axis_config = {'title': 'Result', 'dtick': 1}
    y_axis_config = {'title': 'Frequency of Result'}

    my_layout = Layout(title = 'Results of rolling a D6 and D10 dice 50 000 times', xaxis = x_axis_config, yaxis = y_axis_config)
    offline.plot({'data': data, 'layout': my_layout}, filename = 'plt_dice_roll_model.html')

if __name__ == '__main__':
    main()