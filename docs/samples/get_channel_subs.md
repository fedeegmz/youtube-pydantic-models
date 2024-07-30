# Get Channel Subscriber Count

```python
from youtube_pydantic_models import (
    YoutubeClient,
    YoutubeChannelResource
)


def get_client(api_key: str) -> YoutubeClient:
    client = YoutubeClient(api_key)
    return client

def get_channel_subs(
    client,
    channel_id: str
) -> int | None:
    channel: YoutubeChannelResource | None = client.get_channel(
        id=channel_id,
        part="statistics"
    )

    if channel:
        return channel.statistics.subscriber_count


### MAIN ###
print("Getting data")
yt_client = get_client("MY_SECRET_API_KEY")
example_id = "UC_x5XG1OV2P6uZZ5FSM9Ttw"
subs = get_channel_subs(yt_client, example_id)

print(f"Subscribers of '{example_id}': {subs}")
```
