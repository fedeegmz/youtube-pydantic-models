# youtube-pydantic-models

A **Python** library that contains the most popular YouTube models based on Pydantic. If you are working with the **YouTube API**, **youtube-pydantic-models** can help you validate, manipulate, and retrieve data.  
Use the YoutubeClient class to get data about channels, playlists, videos and more.  
The YouTube API returns data using camel case, but you can choose to return data using camel case or snake case. With the parameter ```by_alias=True```, data is returned using camel case. When using the model, every parameter is accessed using snake case.

- Author: [fedeegmz](https://github.com/fedeegmz)
- Source: [GitHub](https://github.com/fedeegmz/youtube_pydantic_models)
- [**Docs**](https://fedeegmz.github.io/youtube-pydantic-models/)

## Features

- Validate YouTube API responses using Pydantic models
- Convert data between camel case and snake case
- Easy-to-use interface for common YouTube resources
- Make requests to YouTube API using the client

## Requirements

- Python 3.7+
- A YouTube Data API Key

## Installation

You can install the library using pip:

```sh
pip install youtube-pydantic-models
```

## Example usage

### YoutubeClient

```python
from youtube_pydantic_models import YoutubeClient

client = YoutubeClient("MY_API_KEY")
channel = client.get_channel(
    id="UC_x5XG1OV2P6uZZ5FSM9Ttw",
    part="snippet, statistics"
)

if channel:
    print(channel.id) # -> UC_x5XG1OV2P6uZZ5FSM9Ttw
```

### Channel Model

```python
import requests
from youtube_pydantic_models import YoutubeChannelResource

params = {
    'id': "UC_x5XG1OV2P6uZZ5FSM9Ttw",
    'key': "YOUR_API_KEY",
    'part': "snippet, contentDetails"
}
response = requests.get(
    "https://www.googleapis.com/youtube/v3/channels",
    params=params
).json()

channel = YoutubeChannelResource(**response)
print(channel.id)
print(channel.snippet.custom_url)
channel_dict = channel.model_dump(
    by_alias=True,
    exclude_none=True
)
```

### Playlist Model

```python
import requests
from youtube_pydantic_models import YoutubePlaylistResource

params = {
    'channelId': "UC_x5XG1OV2P6uZZ5FSM9Ttw",
    'key': "YOUR_API_KEY",
    'part': "snippet, player"
}
response = requests.get(
    "https://www.googleapis.com/youtube/v3/playlists",
    params=params
).json()

playlist = YoutubePlaylistResource(**response)
print(playlist.snippet.channel_title)
print(playlist.player.embed_html)
playlist_dict = playlist.model_dump(
    by_alias=True,
    exclude_none=True
)
```

### Video Model

```python
import requests
from youtube_pydantic_models import YoutubeVideoResource

params = {
    'id': "PJm8WNajZtw",
    'key': "YOUR_API_KEY",
    'part': "statistics"
}
response = requests.get(
    "https://www.googleapis.com/youtube/v3/videos",
    params=params
).json()

video = YoutubeVideoResource(**response)
print(video.id)
print(video.statistics.view_count)
video_dict = video.model_dump(
    by_alias=True,
    exclude_none=True
)
```

### Search Model

```python
import requests
from youtube_pydantic_models import YoutubeSearchResource

params = {
    'channelId': "UC_x5XG1OV2P6uZZ5FSM9Ttw",
    'key': "YOUR_API_KEY",
    'part': "id, snippet"
}
response = requests.get(
    "https://www.googleapis.com/youtube/v3/search",
    params=params
).json()

resource = YoutubeSearchResource(**response)
print(resource.id.kind)
print(resource.snippet.thumbnails.default.url)
resource_dict = resource.model_dump(
    by_alias=True,
    exclude_none=True
)
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request on GitHub.

### Recommendations

To ensure code quality and prevent issues, we recommend setting up Git hooks for this project. These hooks will automatically run a linter before each commit and run tests before pushing to the repository.

The pre-commit hook will run the [Ruff](https://github.com/charliermarsh/ruff) linter to check for any code style or formatting issues. Add the following to your `.git/hooks/pre-commit` file:

```bash
#!/bin/sh
# Ejecutar Ruff linter
ruff format && ruff check --fix
status=$?
if [ $status -ne 0 ]; then
  echo "Error: Ruff linter or formatter found issues. Please fix them before committing."
  exit 1
fi
```

Make sure the hook file is executable:

```bash
chmod +x .git/hooks/pre-commit
```

The pre-push hook will run the Pytest testing suite before pushing code to the repository. Add the following to your .git/hooks/pre-push file:

```bash
#!/bin/sh
# Ejecutar Pytest antes del push
pytest tests/unit
status=$?
if [ $status -ne 0 ]; then
  echo "Error: Pytest found failing tests. Please fix them before pushing."
  exit 1
fi
```

Similarly, ensure the hook file is executable:

```bash
chmod +x .git/hooks/pre-push
```

By following this setup, you'll help maintain high code standards and prevent common errors from reaching the repository.


## License

This project is licensed under the MIT License.
