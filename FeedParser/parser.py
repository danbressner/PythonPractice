import feedparser
import pandas as pd

FEED_FILE = 'congress_sys_alerts.xml'

feed = feedparser.parse(FEED_FILE)

if 'title' in feed.entries[0]:
    for entry in feed.entries:
        print(f'{entry.published} - {entry.title}')
        print('-'*100)
else:
    print('Did not find "title" in the first feed entry. Was your XML file pulled correctly?')

df = pd.DataFrame(feed.entries)
df['timestamp'] = df['published'].str.extract('(\d{2}:\d{2}:\d{2})')
df['date'] = df['published'].str.extract('(\d{2} \w{3} \d{4})')
df['weekday'] = df['published'].str.extract('(^\w{3})')

print(df.timestamp.head(1))
print(df.date.head(1))
print(df.weekday.head(1))