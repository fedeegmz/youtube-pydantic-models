# Youtube Search Resource

```python
from youtube_pydantic_models import YoutubeSearchResource
```

Represents a [-> YouTube search resource](https://developers.google.com/youtube/v3/docs/search).

```json
{
    "kind": "youtube#searchResult",
    "etag": etag,
    "id": {
        "kind": string,
        "videoId": string,
        "channelId": string,
        "playlistId": string
    },
    "snippet": {
        "publishedAt": datetime,
        "channelId": string,
        "title": string,
        "description": string,
        "thumbnails": {
            (key): {
                "url": string,
                "width": unsigned integer,
                "height": unsigned integer
            }
        },
        "channelTitle": string,
        "liveBroadcastContent": string
    }
}
```
