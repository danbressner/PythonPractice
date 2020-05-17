import research


def main():
    research.init()
    print('Breakdown of post-Sandy 311 calls')
    print()

    print('Top 5 days for total calls')
    days = research.call_days()
    for idx, row in enumerate(days[:5], 1):
        print(f'{idx}. {row.date}: {row.total}')
    print()

    print('Top 5 days for FEMA-associated calls.')
    days = research.fema_calls()
    for idx, row in enumerate(days[:5], 1):
        print(f'{idx}. {row.date}: {row.FEMA}')
    print()

    research.day_lookup()


if __name__ == '__main__':
    main()
