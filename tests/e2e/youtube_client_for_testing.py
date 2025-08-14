import unittest

from tests.config import config
from youtube_pydantic_models.main import YoutubeClient


class YoutubeClientForTesting(unittest.TestCase):
    def setUp(self):
        self.client = YoutubeClient(config["YT_API_KEY"])
