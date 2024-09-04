import os
import sys
import subprocess
import re
import json
import requests
from time import sleep


def load_config(config_file):
    with open(config_file, 'r') as file:
        return json.load(file)


def get_diff_files(repo_dir):
    diff_files = []
    try:
        subprocess.check_output(['git', '-C', repo_dir, 'fetch'])
        diff_files = subprocess.check_output(
            ['git', '-C', repo_dir, 'diff', '@{u}', '--name-only']).decode('utf-8').split('\n')
        subprocess.check_output(['git', '-C', repo_dir, 'pull'])
    except subprocess.CalledProcessError as e:
        print("Error: ", e)
    return diff_files


def get_diff_files_with_pattern(diff_files, pattern):
    diff_files_with_pattern = []
    for file in diff_files:
        if re.search(pattern, file):
            diff_files_with_pattern.append(file)
    return diff_files_with_pattern


def main():
    config = load_config('config.json')
    repo_dir = config['git_repo_dir']
    pattern = config['pattern']

    while True:
        diff_files = get_diff_files(repo_dir)
        print("Diff files: ", diff_files)
        diff_files_with_pattern = get_diff_files_with_pattern(
            diff_files, pattern)
        print("Diff files with pattern '{}': ".format(
            pattern), diff_files_with_pattern)

        if len(diff_files_with_pattern) > 0:
            # webhook to teams adaptive card
            webhook_url = config['webhook_url']
            message = {
                "type": "message",
                "attachments": [
                    {
                        "contentType": "application/vnd.microsoft.card.adaptive",
                        "content": {
                            "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
                            "type": "AdaptiveCard",
                            "version": "1.0",
                            "body": [
                                {
                                    "type": "TextBlock",
                                    "text": "Changes detected in the repository",
                                    "size": "large",
                                    "weight": "bolder"
                                },
                                {
                                    "type": "TextBlock",
                                    "text": "Files with pattern '{}':".format(pattern),
                                    "size": "medium",
                                    "weight": "bolder"
                                }
                            ],
                            "actions": []
                        }
                    }
                ]
            }

            for file in diff_files_with_pattern:
                message["attachments"][0]["content"]["body"].append({
                    "type": "TextBlock",
                    "text": file,
                    "size": "medium"
                })

            response = requests.post(webhook_url, json=message)
            print("Response: ", response.text)

        sleep(60*5)


if __name__ == "__main__":
    main()
