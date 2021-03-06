import requests
from typing import List
from collections import namedtuple

HouseVote = namedtuple('HouseVote', 'congress chamber session roll_call source url vote_uri bill amendment question '
                                    'question_text description vote_type date time result democratic republican '
                                    'independent total')

HouseMember = namedtuple('HouseMember', 'id api_uri name party state district total_votes votes_with_party '
                                        'party_votes_pct rank notes')

Statement = namedtuple('Statement', 'url date title statement_type member_id congress member_uri name chamber state '
                                    'party subjects')

api_key = 'yourkeyhere'


def get_recent_house_votes() -> List[HouseVote]:
    """Fetch recent house votes and store as a list of namedtuples"""
    url = f'https://api.propublica.org/congress/v1/house/votes/recent.json'
    headers = {'Accept': 'application/json',
               'X-API-Key': api_key}
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    results = resp.json()['results']['votes']
    votes = []
    for r in results:
        votes.append(HouseVote(**r))

    return votes


def get_house_alignment() -> List[HouseMember]:
    """Fetch voting record stats for each member and store as a list of namedtuples"""
    url = 'https://api.propublica.org/congress/v1/116/house/votes/party.json'
    headers = {'Accept': 'application/json',
               'X-API-Key': api_key}
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    results = resp.json()['results'][0]['members']
    voting_records = []

    for r in results:
        voting_records.append(HouseMember(**r))

    return sorted(voting_records, key=lambda x: x.party_votes_pct, reverse=True)


def get_statements(keyword) -> List[Statement]:
    """Fetch recent Congressional statements on a specific topic and store results as a list of namedtuples"""
    url = f'https://api.propublica.org/congress/v1/statements/search.json?query={keyword}'
    headers = {'Accept': 'application/json',
               'X-API-Key': api_key}
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    statements = []
    results = resp.json()['results']

    for r in results:
        statements.append(Statement(**r))

    return statements
