import os

KEYWORDS = ["Taiwan", "China"]
CONNECTION_STRING = "sqlite:///tweets.db"
OUTPUT_FILE = "tweets.csv"
OUTPUT_TABLE = "tweets"
SQL_DB = "sqlite:///tweets.db"

# Set secrets as environment variables before running
consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")
