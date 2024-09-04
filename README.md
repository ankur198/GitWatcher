# GitWatcher

GitWatcher is a utility that monitors a specified Git repository for changes and sends notifications to a Microsoft Teams channel via a webhook when changes matching a specified pattern are detected.

## Features

- Monitors a Git repository for changes.
- Filters changed files based on a specified pattern.
- Sends notifications to a Microsoft Teams channel using an adaptive card.

## Configuration

The configuration for GitWatcher is stored in a `config.json` file. The file should contain the following fields:

```json
{
    "git_repo_dir": "/path/to/your/repo",
    "pattern": "main",
    "webhook_url": "https://your-teams-webhook-url"
}
```

- `git_repo_dir`: The directory of the Git repository to monitor.
- `pattern`: The pattern to filter the changed files.
- `webhook_url`: The Microsoft Teams webhook URL to send notifications to. Create webhook by following the following article: [Send Adaptive Cards to Microsoft Teams using Incoming Webhook](https://prod.support.services.microsoft.com/en-us/office/create-incoming-webhooks-with-workflows-for-microsoft-teams-8ae491c7-0394-4861-ba59-055e33f75498)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/GitWatcher.git
cd GitWatcher
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Create and configure the `config.json` file as described above.

##Usage

Run the GitWatcher utility:

```bash
python gitwatcher.py
```

The utility will start monitoring the specified Git repository for changes and send notifications to the configured Microsoft Teams channel when changes matching the specified pattern are detected.

## License
This project is licensed under the MIT License. See the LICENSE file for details.