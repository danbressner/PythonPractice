from uplink_helpers import raise_for_status
from datetime import datetime
import requests
import uplink


@uplink.json
@raise_for_status
class BlogClient(uplink.Consumer):

    def __init__(self):
        super().__init__(base_url='https://consumerservicesapi.talkpython.fm')

    @uplink.get('api/blog')
    def all_entries(self) -> requests.models.Response:
        """Gets all entries from the server"""
        pass

    @uplink.get('api/blog/{post_id}')
    def entry_by_id(self, post_id: uplink.Path("post_id")) -> requests.models.Response:
        """Get a single entry by passing its ID"""
        pass

    def add_new_entry(self, title: str, content: str,
                      views: int = 0, published: str = None) -> requests.models.Response:
        if published is None:
            published = datetime.now().isoformat()

        return self.__add_new_entry(title=title,
                                    content=content,
                                    view_count=views,
                                    published=published
                                    )

    @uplink.post('/api/blog')
    def __add_new_entry(self, **kwargs: uplink.Body) -> requests.models.Response:
        """Create a new post"""
        pass
