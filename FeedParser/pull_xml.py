import requests

URL = 'https://www.congress.gov/rss/notification.xml'

if __name__ == '__main__':
    print(f'Fetching {URL}')
    r = requests.get(URL)
    r.raise_for_status()
    with open('congress_sys_alerts.xml', 'wb') as f:
        f.write(r.content)
    print('Complete!')

