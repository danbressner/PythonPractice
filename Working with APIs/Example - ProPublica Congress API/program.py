import congress_api
from pprint import pprint


def main():
    results = congress_api.get_recent_house_votes()
    print(f'Identified {len(results)} recent House votes.')
    print()
    for r in results:
        pprint(f"Date: {r.date} -  {r.bill['title']}")
        pprint(r.result)
        print()


if __name__ == '__main__':
    main()