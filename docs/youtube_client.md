# YouTube Client

YouTube's client based on requests.

```python
from youtube_pydantic_models import YoutubeClient


client = YoutubeClient("YOUR_API_KEY")

channel = client.get_channel("example_id", "snippet, statistics")
print(channel.snippet.title)
print(client.get_current_quota())
```

## Init args

- **api_key** (str): secret YouTube API key.
- **qouta_per_day** (int): limit per day of YouTube quota. By default is 10000.
- **quotas_table** (Enum): table of quota's cost. By default is [Quotas class](https://github.com/fedeegmz/youtube-pydantic-models/blob/main/youtube_pydantic_models/quotas.py)

## Methods

- get_api_service_name(): returns the value of _api_service_name private attribute.
- get_api_version(): returns the value of _api_version private attribute.
- get_quota_per_day(): returns the value of _quota_per_day private attribute.
- set_quota_per_day(): set a value of _quota_per_day private attribute.
- get_current_quota(): returns the value of _current_quota private attribute.
- **get_channel(id: str, part: str)**: returns a YoutubeChannelResource or None.
- **get_playlist(id: str, part: str)**: returns a YoutubePlaylistResource or None.
- **get_video(id: str, part: str)**: returns a YoutubeVideoResource or None.
- **search(id: str, part: str, type: str)**: returns a YoutubeSearchResource or None.

### get_channel()

Search a YouTube channel by id. Select part of the resource.  
Returns a **YoutubeChannelResource** or None.

- **Parameters (required):**  
    - **id** (str): channel id to search.
    - **part** (str): resource's parts separated by comma (,). Available parts: (snippet, contentDetails, statistics, topicDetails, status, brandingSettings, contentOwnerDetails).

- **Errors:**  
    - **QuotaException**: unavailable YouTube quota.

### get_playlist()

Search a YouTube playlist by id. Select part of the resource.  
Returns a **YoutubePlaylistResource** or None.

- **Parameters (required):**
    - **id** (str): playlist id to search.
    - **part** (str): resource's parts separated by comma (,). Available parts: (snippet, contentDetails, player, status, localizations).

- **Errors:**
    - **QuotaException**: unavailable YouTube quota.

### get_video()

Search a YouTube video by id. Select part of the resource.  
Returns a **YoutubeVideoResource** or None.

- **Parameters (required):**
    - **id** (str): video id to search.
    - **part** (str): resource's parts separated by comma (,). Available parts: (snippet, contentDetails, statistics, topicDetails, status, player, recordingDetails, localizations, liveStreamingDetails).

- **Errors:**
    - **QuotaException**: unavailable YouTube quota.

### search()

Search a YouTube resource by channel id. Select part of the resource.  
Returns a **YoutubeSearchResource** or None.

- **Parameters (required):**
    - **channel_id** (str): channel id to search.
    - **part** (str): resource's parts separated by comma (,). Available parts: (snippet).
    - **type** (str): resource's type to filter. Available types: (channel, playlist, video).

- **Errors:**
    - **QuotaException**: unavailable YouTube quota.
