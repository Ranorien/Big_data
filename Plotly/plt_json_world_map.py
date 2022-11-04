# https://plotly.com/python/ - examples of charts

import json
from plotly.graph_objs import Layout, Figure
from plotly import offline

def main():
    """main function"""

    filename = 'data/eq_data_30_day_m1.json'
    readable_file = 'data/readable_eq_data.json'

    all_eq_data = read_and_convert_to_readable(filename, readable_file)
    if not all_eq_data:
        return False

    all_eq_dict = all_eq_data['features'] #take all data with key 'features'

    
    # create new dictionary with lists and with following structure
    data = {'mags':[], 'lons': [], 'lats': [], 'text': []}

    for eq_dict in all_eq_dict:
        data['mags'].append(eq_dict['properties']['mag'])
        data['lons'].append(eq_dict['geometry']['coordinates'][0])
        data['lats'].append(eq_dict['geometry']['coordinates'][1])
        data['text'].append(eq_dict['properties']['title'])

    # draw map
    pltdata = {
        'type': 'scattergeo',
        'lon': data['lons'],
        'lat': data['lats'],
        'text': data['text'],
        'marker': {
            'size': [5*mag for mag in data['mags']], #10 - just formating rate for point on map
            'color': data['mags'],
            'colorscale': 'Viridis',
            'reversescale': True,
            'colorbar': {'title': 'Magnitude'}
        }
    }


    my_layout = Layout(title = 'Global Earthquakes')
    fig = {'data': pltdata, 'layout': my_layout}

    offline.plot(fig, filename = 'plt_json_world_map.html')

    

def read_and_convert_to_readable(original_file, readable_file):
    """convert file to readable format"""

    try:
        with open(original_file, 'r') as f:
            data = json.load(f)
        
    except FileNotFoundError:
        print(f'File {original_file} does not exist')
        return False

    else:
        with open(readable_file, 'w') as f:
            json.dump(data, f, indent = 4) #indent = 4 readable file format

        return data


if __name__ == '__main__':
    main()