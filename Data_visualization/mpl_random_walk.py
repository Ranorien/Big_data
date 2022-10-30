# Random walk modeling via matplotlib
from random import choice
import matplotlib.pyplot as plt

class RandomWalk():
    """Generation of random walking"""

    def __init__(self, num_points = 5000):
        """intialization"""

        self.num_points = num_points

        # init position
        self.x_values = [0]
        self.y_values = [0]

    def __get_step(self):
        """return step"""
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4])
        step = direction * distance
        return step

    def fill_walk(self):
        """generate all steps of walking"""

        while len(self.x_values) < self.num_points:

            x_step = self.__get_step()
            y_step = self.__get_step()

            if x_step == 0 and y_step == 0:
                continue

            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

def main():

    # create values of random walk
    rw = RandomWalk(100000)
    rw.fill_walk()

    # set window size and title
    fig, ax = plt.subplots(figsize=(10, 5), dpi = 128, num='Matplotlib Random walk')

    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c = point_numbers, cmap = plt.cm.Blues, edgecolors = 'none', s = 1)

    # add the firts and the last points
    ax.scatter(rw.x_values[0], rw.y_values[0], c = 'green', edgecolors = 'none', s = 100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c = 'red', edgecolors = 'none', s = 100)

    # add titles
    ax.set_title('Random walk', fontsize = 24)
    ax.set_xlabel('West <-> East', fontsize = 14)
    ax.set_ylabel('South <-> North', fontsize = 14)
    ax.tick_params(axis = 'both', which = 'major', labelsize = 14)


    # save plot in image file
    plt.savefig('mpl_random_walk.png', bbox_inches = 'tight')

    # show plot
    plt.show()

if __name__ == '__main__':
    main()