import movie_api


def main():
    keyword = input('Keyword of title search: ')
    results = movie_api.find_movie_by_title(keyword)
    print(f'There are {len(results)} results:')
    print()
    for r in results:
        print(f'{r.title} with an imdb score of {r.imdb_score}')


if __name__ == '__main__':
    main()
