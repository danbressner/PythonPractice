import congress_api
from pprint import pprint


def main():
    recent_votes = congress_api.get_recent_house_votes()
    print(f'Identified {len(recent_votes)} recent House votes.')
    print()
    for r in recent_votes:
        pprint(f"Date: {r.date} -  {r.bill['title']}")
        print()
        pprint(f"Latest action: {r.bill['latest_action']}")
        pprint(f'Result: {r.result}')
        print('-' * 100)

    print('The 10 House members who vote along party lines the most:')
    alignment = congress_api.get_house_alignment()
    for idx, member in enumerate(alignment[:10], 1):
        print(f'{idx}. {member.name} - {member.party} {member.party_votes_pct}')


if __name__ == '__main__':
    main()
