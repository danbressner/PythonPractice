# CSV manipulation practice
# Data from FiveThirtyEight: https://github.com/fivethirtyeight/data/

import research


def main():
    print("Weather research for Seattle, 2014-2015")
    print()
    research.init()

    print("The hottest 5 days:")
    days = research.hot_days()
    for idx, day in enumerate(days[:5], 1):
        print(f'{idx}. {day.actual_max_temp} on {day.date}')
    print()

    print("The coldest 5 days:")
    days = research.cold_days()
    for idx, day in enumerate(days[:5], 1):
        print(f'{idx}. {day.actual_min_temp} on {day.date}')
    print()

    print("The wettest 5 days:")
    days = research.wet_days()
    for idx, day in enumerate(days[:5], 1):
        print(f'{idx}. {day.actual_precipitation} on {day.date}')
    print()


if __name__ == '__main__':
    main()
