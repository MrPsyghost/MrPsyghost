import requests, os, time
from typing import Any

t = time.monotonic()
data = None

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
            'user_name': user_name,
            'name': repo['name'],
            'description': repo['description'],
            'url': repo['html_url'],
            'language': repo['language'],
            'stars': repo['stargazers_count'],
            'updated': repo['updated_at'],
            'cover_img': f"https://raw.githubusercontent.com/{user_name}/{repo['name']}/main/portfolio/cover.png",
            'readme': requests.get(f"https://api.github.com/repos/{user_name}/{repo['name']}/readme", headers=headers).json(),
            'thumbnails': len(requests.get(f"https://api.github.com/repos/{user_name}/{repo['name']}/contents/portfolio/thumbnails", headers=headers).json()),
        }
        for repo in repos
        if "portfolio" in repo['topics']
    ]

def get_repos_with_cache(user_name: str, caching: bool=False, cachingTime: int=60) -> list[dict[str, Any]]:
    global data, t
    if not caching:
        return get_repos(user_name)
    else:
        if data is None or time.monotonic() - t > cachingTime:
            data = get_repos(user_name)
            t = time.monotonic()
            print('cache reset')
        return data