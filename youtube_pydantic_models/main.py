import requests


class YoutubeClient:
    def __init__(self, api_key: str) -> None:
        if not api_key:
            raise Exception("API_KEY param is required")
        
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
    ) -> dict:
        available_part = "snippet, contentDetails, statistics, topicDetails, status, brandingSettings, contentOwnerDetails"
        params = {
            'id': id,
            'part': part
        }

        response = self._get_request(
            endpoint = "channels",
            params = params
        )
        return response

    def get_playlist(
        self,
        id: str,
        part: str
    ) -> dict:
        available_part = "snippet, contentDetails, player, status, id, localizations"
        params = {
            'id': id,
            'part': part
        }

        response = self._get_request(
            endpoint = "playlists",
            params = params
        )
        return response

    def get_video(
        self,
        id: str,
        part: str
    ) -> dict:
        available_part = "snippet, contentDetails, statistics, topicDetails, status, player, recordingDetails, localizations, liveStreamingDetails"
        params = {
            'id': id,
            'part': part
        }

        response = self._get_request(
            endpoint = "videos",
            params = params
        )
        return response

    def search(
        self,
        channel_id: str,
        part: str,
        type: str
    ) -> dict:
        available_part = "id, snippet"
        params = {
            'id': channel_id,
            'part': part,
            'type': type
        }

        response = self._get_request(
            endpoint = "search",
            params = params
        )
        return response
    
    def _get_request(
        self,
        endpoint: str,
        params: dict
    ) -> dict | list:
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
