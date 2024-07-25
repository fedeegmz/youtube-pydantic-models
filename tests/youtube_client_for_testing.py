import unittest
from youtube_pydantic_models.main import YoutubeClient
from tests.config import config


class YoutubeClientForTesting(unittest.TestCase):
    def setUp(self):
        self.client = YoutubeClient(config["YT_API_KEY"])
