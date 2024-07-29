# Youtube Playlist Resource

```python
from youtube_pydantic_models import YoutubePlaylistResource
```

Represents a [-> YouTube playlist](https://developers.google.com/youtube/v3/docs/playlists).

```json
{
    "kind": "youtube#playlist",
    "etag": etag,
    "id": string,
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
        "defaultLanguage": string,
        "localized": {
            "title": string,
            "description": string
        }
    },
    "status": {
        "privacyStatus": string
    },
    "contentDetails": {
        "itemCount": unsigned integer
    },
    "player": {
        "embedHtml": string
    },
    "localizations": {
        (key): {
            "title": string,
            "description": string
        }
    }
}
```
