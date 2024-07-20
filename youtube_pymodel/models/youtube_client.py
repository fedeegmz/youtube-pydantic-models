import googleapiclient.discovery


class YoutubeClient:
    def __init__(self, api_key: str) -> None:
        API_SERVICE_NAME = "youtube"
        API_VERSION = "v3"
        
        self.client = self.login(
            API_SERVICE_NAME,
            API_VERSION,
            api_key
        )
    
    def login(
        api_service_name: str,
        api_version: str,
        api_key: str
    ):
        try:
            client = googleapiclient.discovery.build(
                api_service_name,
                api_version,
                developerKey = api_key
            )
        except:
            raise Exception("Youtube client not connected")
        return client
    
    def get_client(self):
        return self.client
