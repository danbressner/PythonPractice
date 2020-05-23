import requests
from collections import namedtuple
from typing import List

Movie = namedtuple('Movie', '''imdb_code title director
                   keywords duration genres rating year imdb_score''')


def find_movie_by_title(keyword: str) -> List[Movie]:
    '''Enter a string keyword to lookup relevant movies'''
    url = f'https://movieservice.talkpython.fm/api/search/{keyword}'
    headers = {'Accept': 'application/json'}

    resp = requests.request('GET', url, headers=headers)
    resp.raise_for_status()
    movies = []
    results = resp.json()
    for r in results.get('hits'):
        movies.append(Movie(**r))

    return movies
