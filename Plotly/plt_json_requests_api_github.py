import requests
from plotly import offline

def main():
    
    language = 'python'
    url = f'https://api.github.com/search/repositories?q=language:{language}&sort=stars'
    headers = {'Accept': 'application/vnd.github.v3+json'}
    r = requests.get(url, headers=headers)
    
    print(f'Status code: {r.status_code}')
    if r.status_code != 200:
        return
    
    response_json = r.json()
    repo_dicts = response_json['items']


    # create new dictionary with lists and with following structure
    data = {'links':[], 'stars': [], 'labels': []}

    for repo_dict in repo_dicts:
        data['links'].append(f"<a href='{repo_dict['html_url']}'>{repo_dict['name']}</a>")
        data['stars'].append(repo_dict['stargazers_count'])
        data['labels'].append(f"{repo_dict['owner']['login']}<br>{repo_dict['description']}")

    # draw map
    pltdata = [{
        'type': 'bar',
        'x': data['links'],
        'y': data['stars'],
        'hovertext': data['labels'],
        'marker': {
            'color': 'rgb(60, 100, 150)',
            'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
        },
        'opacity': 0.6
        }]
    
    my_layout = {
        'title': f'Most-Starred {language.title()} Projects on GitHub',
        'titlefont': {'size': 28},
        'xaxis': {
            'title': 'Repository',
            'titlefont': {'size': 24},
            'tickfont': {'size': 14}
            },
        'yaxis': {
            'title': 'Stars',
            'titlefont': {'size': 24},
            'tickfont': {'size': 14}
            }
    }
    
    fig = {'data': pltdata, 'layout': my_layout}
    offline.plot(fig, filename='plt_json_requests_api_github.html')

if __name__ == '__main__':
    main()