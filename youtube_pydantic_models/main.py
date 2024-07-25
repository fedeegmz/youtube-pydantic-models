import requests
from youtube_pydantic_models.channel_resource import YoutubeChannelResource
from youtube_pydantic_models.playlist_resource import YoutubePlaylistResource
from youtube_pydantic_models.video_resource import YoutubeVideoResource
from youtube_pydantic_models.search_resource import YoutubeSearchResource


class YoutubeClient:
    def __init__(self, api_key: str) -> None:
        if not api_key:
            raise Exception("api_key param is required")
        
        self._api_key: str = api_key
        self._api_version: str = "v3"
        self._api_service_name: str = "youtube"
        self._api_base_path: str = f"https://www.googleapis.com/"
        self._api_path: str = f"{self._api_base_path}{self._api_service_name}/{self._api_version}/"
    
    def get_api_service_name(self) -> str:
        return self._api_service_name
    
    def get_api_version(self) -> str:
        return self._api_version
    
    def get_channel(
        self,
        id: str,
        part: str
    ) -> YoutubeChannelResource | None:
        """ Search a YouTube channel by id and return a YoutubeChannelResource or None.
        Arguments:
        id [str] -- channel id to search
        part [str] -- resource's parts separated by comma (,). 
        Available parts: snippet, contentDetails, statistics, topicDetails, status, brandingSettings, contentOwnerDetails
        """
        params = {
            'id': id,
            'part': part
        }

        response = self._get_request(
            endpoint = "channels",
            params = params
        )
        if not response:
            return None
        elif response['pageInfo']['totalResults'] > 0:
            data = response['items'][0]
            return YoutubeChannelResource(**data)
        return None

    def get_playlist(
        self,
        id: str,
        part: str
    ) -> YoutubePlaylistResource | None:
        """ Search a YouTube playlist by id and return a YoutubePlaylistResource or None.
        Arguments:
        id [str] -- channel id to search
        part [str] -- resource's parts separated by comma (,). 
        Available parts: snippet, contentDetails, player, status, localizations
        """
        params = {
            'id': id,
            'part': part
        }

        response = self._get_request(
            endpoint = "playlists",
            params = params
        )
        if not response:
            return None
        elif response['pageInfo']['totalResults'] > 0:
            data = response['items'][0]
            return YoutubePlaylistResource(**data)
        return None

    def get_video(
        self,
        id: str,
        part: str
    ) -> YoutubeVideoResource | None:
        """ Search a YouTube video by id and return a YoutubeVideoResource or None.
        Arguments:
        id [str] -- channel id to search
        part [str] -- resource's parts separated by comma (,). 
        Available parts: snippet, contentDetails, statistics, topicDetails, status, player, recordingDetails, localizations, liveStreamingDetails
        """
        params = {
            'id': id,
            'part': part
        }

        response = self._get_request(
            endpoint = "videos",
            params = params
        )
        if not response:
            return None
        elif response['pageInfo']['totalResults'] > 0:
            data = response['items'][0]
            return YoutubeVideoResource(**data)
        return None

    def search(
        self,
        channel_id: str,
        part: str,
        type: str
    ) -> YoutubeSearchResource | None:
        """ Search a YouTube channel by id and return a YoutubeSearchResource or None.
        Arguments:
        id [str] -- channel id to search
        part [str] -- resource's parts separated by comma (,). Available parts: snippet.
        type [str] -- type of resource. Available types: channel, playlist, video
        """
        params = {
            'channelId': channel_id,
            'part': part,
            'type': type
        }

        response = self._get_request(
            endpoint = "search",
            params = params
        )
        if not response:
            return None
        elif response['pageInfo']['totalResults'] > 0:
            data = response['items'][0]
            return YoutubeSearchResource(**data)
        return None
    
    def _get_request(self, endpoint: str, params: dict) -> dict | list:
        response = requests.get(
            self._api_path + endpoint,
            params=self._set_key_param(params)
        )

        if response.status_code != 200:
            return None
        return response.json()
    
    def _set_key_param(self, params: dict) -> dict:
        params['key'] = self._api_key
        return params
