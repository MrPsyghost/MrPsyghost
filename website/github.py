import requests, os
from typing import Any

def get_repos(user_name: str) -> list[dict[str, Any]]:
    url = f'https://api.github.com/users/{user_name}/repos'

    headers = {
        'Authorization': f"Bearer {os.getenv('GITHUB_TOKEN')}",
        'Accept': 'application/vnd.github+json',
    }

    params = {
        'sort': 'updated',
        'per_page': 100,
    }

    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()

    repos = response.json()

    return [
        {
            'name': repo['name'],
            'description': repo['description'],
            'url': repo['html_url'],
            'language': repo['language'],
            'stars': repo['stargazers_count'],
            'updated': repo['updated_at'],
            'cover_img': f"https://raw.githubusercontent.com/{user_name}/{repo['name']}/main/portfolio/cover.png",
        }
        for repo in repos
        if "portfolio" in repo['topics']
    ]