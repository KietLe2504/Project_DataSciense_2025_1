import clickhouse_connect
import pandas as pd
import numpy as np

data = np.load('data/youtube_comments.npy', allow_pickle=True)
col = ['channel_name', 'channel_id', 'video_name', 'video_id', 'author', 'comment_text', 'likes', 'time', 'comment_id']
df = pd.DataFrame(data, columns=col)

client = clickhouse_connect.get_client(
    host='localhost',
    port=8123,
    username='admin',
    password='youtubedata'
)

create_table_query = f"""
CREATE TABLE IF NOT EXISTS comments (
    channel_name Nullable(Varchar),
    channel_id Varchar,
    video_name Nullable(Varchar),
    video_id Varchar,
    author Nullable(Varchar),
    comment_text Nullable(Text),
    likes Nullable(Int),
    time Nullable(Varchar),
    comment_id Varchar
) ENGINE = MergeTree()
ORDER BY comment_id;
"""

client.command(create_table_query)
client.insert_df('comments', df)

channels_df = pd.read_csv('data/channel_info_5000.csv')
channels_df.columns = ['channel_name', 'channel_ID', 'subscriberCount', 'videoCount', 'totalView', 'country']
channels_df = channels_df.replace({np.nan: None})

create_table_query = f"""
CREATE TABLE IF NOT EXISTS channels (
    channel_name Nullable(Varchar),
    channel_ID Varchar,
    subscriberCount Nullable(Int),
    videoCount Nullable(Int),
    totalView Nullable(Bigint),
    country Nullable(Varchar)
) ENGINE = MergeTree()
ORDER BY channel_ID;
"""

client.command(create_table_query)
client.insert_df('channels', channels_df)