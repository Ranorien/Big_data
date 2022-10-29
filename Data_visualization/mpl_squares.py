import matplotlib.pyplot as plt

def main():
    input_values = [1, 2, 3, 4, 5]
    squares = [1, 4, 9, 16, 25]

    fig, ax = plt.subplots()

    # draw line
    ax.plot(input_values, squares, linewidth = 3)

    # add dots
    ax.scatter(2, 6, c='red', s=200)
    ax.scatter(3, 4, s=200)
    
    # add range of dots
    x_values = [1, 2, 3, 4, 5]
    y_values = [20, 20, 20, 20, 20]
    ax.scatter(x_values, y_values, c = (0, 0.9, 0.5), s = 100) #color in RGB

    # add automatic generated dots
    x_values = [i/10 for i in range(0, 101)] # 0.0, 0.1, 0.2, 0.3, ..., 10.0
    y_values = [x**2+10 for x in x_values]
    ax.scatter(x_values, y_values, c = y_values, cmap = plt.cm.Reds, s = 10) #using of colormap

    # add titles
    ax.set_title('Square Numbers', fontsize = 24)
    ax.set_xlabel('Value', fontsize = 14)
    ax.set_ylabel('Square of Value', fontsize = 14)
    ax.tick_params(axis = 'both', which = 'major', labelsize = 14)

    # add simple grid
    ax.grid()

    # set range of x and y
    ax.axis([0, 10, 0, 110])

    # save plot in image file
    plt.savefig('plot.png', bbox_inches = 'tight')

    # show plot
    plt.show()

if __name__ == '__main__':
    main()