# Demo client for "https://consumerservicesapi.talkpython.fm"
from blog_client import BlogClient


def main():
    val = 'RUN'

    while val:
        print('What would you like to do next?')
        val = input('[w]rite a post or [r]ead them? - ')

        if val == 'w':
            write_entries()
        elif val == 'r':
            read_entries()


def write_entries():
    svc = BlogClient()
    title = input('Title: ')
    content = input('Body contents: ')
    view_count = int(input('View count (int): '))
    # published = datetime.now().isoformat()

    resp = svc.add_new_entry(title, content, view_count)
    print()
    print(f'Created new entry with ID: {resp.json().get("id")}')
    print()


def read_entries():
    svc = BlogClient()
    response = svc.all_entries()
    posts = response.json()
    for idx, p in enumerate(posts, 1):
        print(f'{idx}. {p.get("view_count")} - {p.get("title")}')

    selected = int(input('Which post do you want to view? - '))
    selected_id = posts[selected - 1].get('id')
    response = svc.entry_by_id(selected_id)
    selected_post = response.json()
    print()
    print(f'Fetching blog with id: {selected_id}')
    print(f'Title: {selected_post.get("title")}')
    print(f'Published on: {selected_post.get("published")}')
    print(f'Total views: {selected_post.get("view_count")}')
    print(f'Content: {selected_post.get("content")}')


if __name__ == '__main__':
    main()
