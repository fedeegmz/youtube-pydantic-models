import requests
from datetime import datetime
from enum import Enum
from youtube_pydantic_models.channel_resource import YoutubeChannelResource
from youtube_pydantic_models.playlist_resource import YoutubePlaylistResource
from youtube_pydantic_models.video_resource import YoutubeVideoResource
from youtube_pydantic_models.search_resource import YoutubeSearchResource
from youtube_pydantic_models.quotas import (
    DEFAULT_LIMIT_PER_DAY,
    Quotas
)
from youtube_pydantic_models.errors import (
    InvalidArgException,
    RequiredArgException,
    QuotaException
)


class YoutubeClient:
    
    def __init__(
        self,
        api_key: str,
        quota_per_day: int = DEFAULT_LIMIT_PER_DAY,
        quotas_table: Enum = Quotas
    ) -> None:
        """
        Constructor.

        Parameters (required)
        ----------
            api_key : str
                secret YouTube API key
        
        Parameters (optional)
        ----------
            quota_per_day : int
                limit per day of YouTube quota. By default is 10000
            quotas_table : Enum
                table of quota's cost
        """
        if not api_key:
            raise RequiredArgException("api_key")
        
        self._quotas_table = quotas_table
        self._quota_per_day = quota_per_day
        self._current_quota = quota_per_day
        self._last_request = None
        self._api_key: str = api_key
        self._api_version: str = "v3"
        self._api_service_name: str = "youtube"
        self._api_base_path: str = f"https://www.googleapis.com/"
        self._api_path: str = f"{self._api_base_path}{self._api_service_name}/{self._api_version}/"

    def get_api_service_name(self) -> str:
        return self._api_service_name
    
    def get_api_version(self) -> str:
        return self._api_version
    
    def get_quota_per_day(self) -> int:
        return self._quota_per_day
    
    def set_quota_per_day(self, new_quota: int) -> None:
        if type(new_quota) != int or new_quota <= 0:
            raise InvalidArgException
        
        self._quota_per_day = new_quota
    
    def get_current_quota(self) -> int:
        return self._current_quota
    
    def get_channel(
        self,
        id: str,
        part: str
    ) -> YoutubeChannelResource | None:
        """
        Search a YouTube channel by id. 
        Select part of the resource.

        Parameters (required)
        ----------
            id : str
                channel id to search
            part : str
                resource's parts separated by comma (,). 
                Available parts: (snippet, contentDetails, statistics, 
                topicDetails, status, brandingSettings, contentOwnerDetails)
        
        Returns
        -------
        YoutubeChannelResource or None

        Errors
        ------
            QuotaException : unavailable YouTube quota
        """
        params = {
            'id': id,
            'part': part
        }

        response = self._get_request(
            endpoint = "channels",
            params = params,
            quota = self._quotas_table.LIST_CHANNEL.value
        )

        if response and response['pageInfo']['totalResults'] > 0:
            data = response['items'][0]
            return YoutubeChannelResource(**data)
        return None

    def get_video(
        self,
        id: str,
        part: str
    ) -> YoutubeVideoResource | None:
        """
        Search a YouTube video by id. 
        Select part of the resource.

        Parameters (required)
        ----------
            id : str
                video id to search
            part : str
                resource's parts separated by comma (,). 
                Available parts: (snippet, contentDetails, statistics, topicDetails, 
                status, player, recordingDetails, localizations, liveStreamingDetails)
        
        Returns
        -------
        YoutubeVideoResource or None

        Errors
        ------
            QuotaException : unavailable YouTube quota
        """
        params = {
            'id': id,
            'part': part
        }

        response = self._get_request(
            endpoint = "videos",
            params = params,
            quota = self._quotas_table.LIST_VIDEO.value
        )

        if response and response['pageInfo']['totalResults'] > 0:
            data = response['items'][0]
            return YoutubeVideoResource(**data)
        return None
    
    def get_playlists(
        self,
        part: str,
        channel_id: str | None = None,
        id: str | None = None,
        max_results: int | None = None,
        page_token: str | None = None
    ) -> list[YoutubePlaylistResource] | None:
        """
        Search a YouTube playlist by id. 
        Select part of the resource.

        Parameters (required)
        ----------
            part : str
                resource's parts separated by comma (,). 
                Available parts: (snippet, contentDetails, player, status, localizations)
            
        Parameters (optional)
        ----------
            channel_id : str
                channel id to search
            id : str
                playlist id to search
            max_results : int
                integer between 0 and 50
            page_token : str
                token that represents a page of results
        
        Returns
        -------
        list of YoutubePlaylistResource or None

        Errors
        ------
            QuotaException : unavailable YouTube quota
        """
        params = {
            'channelId': channel_id,
            'part': part
        }
        if id:
            params.update({'id': id})
        if max_results:
            if max_results < 0 or max_results > 50:
                raise InvalidArgException()
            params.update({'maxResults': max_results})
        if page_token:
            params.update({'pageToken': page_token})

        response = self._get_request(
            endpoint = "playlists",
            params = params,
            quota = self._quotas_table.LIST_PLAYLIST.value
        )

        if response and response['pageInfo']['totalResults'] > 0:
            return [
                YoutubePlaylistResource(**item)
                for item in response['items']
            ]
        return None

    def search(
        self,
        channel_id: str,
        part: str,
        type: str
    ) -> list[YoutubeSearchResource] | None:
        """
        Search a YouTube resource by channel id. 
        Select part of the resource.

        Parameters (required)
        ----------
            channel_id : str
                channel id to search
            part : str
                resource's parts separated by comma (,). 
                Available parts: (snippet)
            type : str
                resource's type to filter.
                Available types: (channel, playlist, video)
        
        Returns
        -------
        list of YoutubeSearchResource or None

        Errors
        ------
            QuotaException : unavailable YouTube quota
        """
        params = {
            'channelId': channel_id,
            'part': part,
            'type': type
        }

        response = self._get_request(
            endpoint = "search",
            params = params,
            quota = self._quotas_table.SEARCH.value
        )

        if response and response['pageInfo']['totalResults'] > 0:
            return [
                YoutubeSearchResource(**item)
                for item in response['items']
            ]
        return None
    
    def iter_playlists(
        self,
        channel_id: str,
        part: str = "snippet, contentDetails, player, status, localizations",
        max_results: int = 50,
    ) -> YoutubePlaylistResource | None:
        """
        Search YouTube playlists by channel id. 
        Select part of the resource.

        Parameters (required)
        ----------
            channel_id : str
                channel id to search
            
        Parameters (optional)
        ----------
            part : str
                resource's parts separated by comma (,). 
                Available parts: (snippet, contentDetails, player, status, localizations)
            max_results : int
                integer between 0 and 50. By default is 50
        
        Yield
        -------
        YoutubePlaylistResource or None

        Errors
        ------
            QuotaException : unavailable YouTube quota
        """
        request_quota = self._quotas_table.LIST_PLAYLIST.value
        base_params = {
            'channelId': channel_id,
            'part': part,
            'maxResults': max_results,
            'pageToken': None
        }

        while True:
            response = self._get_request(
                endpoint = "playlists",
                params = base_params,
                quota = request_quota
            )
            for item in response['items']:
                yield YoutubePlaylistResource()
            
            if not response.get("nextPageToken"):
                break
            base_params['pageToken'] = response['nextPageToken']
    
    def _get_request(
        self,
        endpoint: str,
        params: dict,
        quota: int
    ) -> dict | list | None:
        if not self._check_available_quota(quota):
            raise QuotaException()
        
        response = requests.get(
            self._api_path + endpoint,
            params = self._set_key_param(params)
        )

        if response.status_code != 200:
            return None
        
        self._sub_quota(quota)
        return response.json()
    
    def _set_key_param(self, params: dict) -> dict:
        params['key'] = self._api_key
        return params
    
    def _check_available_quota(self, next_quota: int) -> bool:
        now = datetime.now()
        if self._last_request and self._last_request.date() < now.date():
            self._current_quota = self._quota_per_day
        
        next_current_quota = self._current_quota - next_quota
        return self._quota_per_day >= next_current_quota
    
    def _sub_quota(self, sub: int) -> int:
        if type(sub) != int or sub <= 0:
            raise InvalidArgException
        
        self._last_request = datetime.now()
        self._current_quota -= sub
        return self._current_quota
