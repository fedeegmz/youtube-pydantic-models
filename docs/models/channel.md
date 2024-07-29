# Youtube Channel Resource

```python
from youtube_pydantic_models import YoutubeChannelResource
```

Represents a [-> YouTube channel](https://developers.google.com/youtube/v3/docs/channels).

```json
{
    "kind": "youtube#channel",
    "etag": etag,
    "id": string,
    "snippet": {
        "title": string,
        "description": string,
        "customUrl": string,
        "publishedAt": datetime,
        "thumbnails": {
            (key): {
            "url": string,
            "width": unsigned integer,
            "height": unsigned integer
        }
        },
        "defaultLanguage": string,
        "localized": {
            "title": string,
            "description": string
        },
        "country": string
    },
    "contentDetails": {
        "relatedPlaylists": {
            "likes": string,
            "favorites": string,
            "uploads": string
        }
    },
    "statistics": {
        "viewCount": unsigned long,
        "subscriberCount": unsigned long,  // this value is rounded to three significant figures
        "hiddenSubscriberCount": boolean,
        "videoCount": unsigned long
    },
    "topicDetails": {
        "topicIds": [
            string
        ],
        "topicCategories": [
            string
        ]
    },
    "status": {
        "privacyStatus": string,
        "isLinked": boolean,
        "longUploadsStatus": string,
        "madeForKids": boolean,
        "selfDeclaredMadeForKids": boolean
    },
    "brandingSettings": {
        "channel": {
            "title": string,
            "description": string,
            "keywords": string,
            "trackingAnalyticsAccountId": string,
            "unsubscribedTrailer": string,
            "defaultLanguage": string,
            "country": string
        },
        "watch": {
            "textColor": string,
            "backgroundColor": string,
            "featuredPlaylistId": string
        }
    },
    "auditDetails": {
        "overallGoodStanding": boolean,
        "communityGuidelinesGoodStanding": boolean,
        "copyrightStrikesGoodStanding": boolean,
        "contentIdClaimsGoodStanding": boolean
    },
    "contentOwnerDetails": {
        "contentOwner": string,
        "timeLinked": datetime
    },
    "localizations": {
        (key): {
            "title": string,
            "description": string
        }
    }
}
```
