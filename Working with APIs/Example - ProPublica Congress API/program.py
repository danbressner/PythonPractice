import congress_api
from pprint import pprint


def main():
    recent_votes = congress_api.get_recent_house_votes()
    print(f'Identified {len(recent_votes)} recent House votes. Printing the most recent 5: ')
    print()
    for idx, vote in enumerate(recent_votes[:5], 1):
        pprint(f"{idx}. Date: {vote.date} -  {vote.bill['title']}")
        print()
        pprint(f"Latest action: {vote.bill['latest_action']}")
        print()
        pprint(f'Result: {vote.result}')
        print('-' * 100)

    print('The 10 House members who vote along party lines the most:')
    alignment = congress_api.get_house_alignment()
    for idx, member in enumerate(alignment[:10], 1):
        print(f'{idx}. {member.name} - {member.party} {member.party_votes_pct}')

    print()
    print('-'*100)
    keyword = input('Enter a search term to see recent statements: ')
    statements = congress_api.get_statements(keyword)
    for statement in statements:
        print(f'{statement.date}: {statement.name} {statement.party}, {statement.state} - Title: {statement.title}')
        print(statement.url)
        print('-'*100)


if __name__ == '__main__':
    main()

