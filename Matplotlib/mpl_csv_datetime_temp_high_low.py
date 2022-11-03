import csv
from matplotlib import pyplot as plt
from datetime import datetime

def main():
    """main function"""

    filenames = ['data\sitka_weather_2018_simple.csv', 'data\deathvalley_2018_simple.csv']
    data = []

    for filename in filenames:

        data_row = {'dates': [], 'highs': [], 'lows': []}

        try:
            with open(filename, 'r') as f:
                reader = csv.reader(f)
                header_row = next(reader)

                columns = get_columns_ind(header_row)

                # read max temperatures
                for row in reader:

                    date = datetime.strptime(row[columns['DATE']], '%Y-%m-%d') # %Y - 2018, %y - 18, ...

                    try:
                        high = convert_f_to_c(row[columns['TMAX']])
                        low = convert_f_to_c(row[columns['TMIN']])
                        

                    except ValueError:
                        print(f'Missing data for {date}')
                    
                    else:
                        data_row['highs'].append(high)
                        data_row['lows'].append(low)
                        data_row['dates'].append(date)
            
        except FileNotFoundError:
            print(f'File {filename} does not exist')

        else:
            data_row['filename'] = filename.split('\\')[-1] #split() returns the list, we take only the last value
            data.append(data_row)

    for index, data_row in enumerate(data):
        file = data_row['filename'].split('_')[0] #split() returns the list, we take only the first value
        create_chart(file, data_row['dates'], data_row['highs'], data_row['lows'])

    # show all charts
    plt.show()

def convert_f_to_c(f):
    """convert fahrenheit to celsius"""

    return float((int(f) - 32) * (5/9))



def get_columns_ind(row):
    """get columns index based on header row"""
    columns = {}

    for index, column_header in enumerate(row): #return index of item in the list
        columns[column_header] = index          #create dictionary with indexes

    return columns

def create_chart(name, dates, highs, lows):
    """show charts"""

    # set window size and title
    fig, ax = plt.subplots(figsize=(10, 5), num = f'Temperature {name.title()}')

    # draw lines
    ax.plot(dates, highs, 'red', alpha = 0.5) # alpha = transparency
    ax.plot(dates, lows, 'blue', alpha = 0.5)

    plt.fill_between(dates, highs, lows, facecolor = 'blue', alpha = 0.3)

    # set chart tittle
    plt.title(f'Daily high and low temperatures, {name.title()}, 2018', fontsize = 24)
    plt.xlabel('', fontsize = 16)

    # show date on diagonal
    fig.autofmt_xdate()

    plt.ylabel('Temperature (\u00b0C)', fontsize = 16) #special symbol gradus \u00b0
    plt.tick_params(axis = 'both', which = 'major', labelsize = 16)

    # add simple grid
    ax.grid()

    # save plot in image file
    plt.savefig(f'mpl_csv_datetime_temp_high_low_{name}.png', bbox_inches = 'tight')


if __name__ == '__main__':
    main()