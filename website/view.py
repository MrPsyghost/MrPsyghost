from flask import Blueprint, render_template, abort#, redirect, request, flash, session
from .db import *
from .github import get_repos, get_repos_with_cache
from pathlib import Path

view = Blueprint('view', __name__)

CONFIG_FILE = Path('website\\static\\github.cfg')

if not CONFIG_FILE.exists():
    CONFIG_FILE.write_text (
        'user=MrPsyghost\n'
        'caching=true\n'
        'cachingTime=60\n'
    )

cfg = {}

with CONFIG_FILE.open() as f:
    for line in f:
        line = line.strip()
        if not line or '=' in line:
            continue
        key, value = line.split('=', 1)
        cfg[key] = value

GITHUB_USER = cfg.get('user', 'MrPsyghost')
CACHING = cfg.get('caching', 'true').lower() == 'true'
CACHING_TIME = int(cfg.get('cachingTime', '60'))

@view.route('/')
def home():
    repos = get_repos_with_cache(GITHUB_USER, False, CACHING)
    return render_template('index.html', repos=repos)

@view.route('/projects/<repo_name>')
def project(repo_name):
    for repo in get_repos_with_cache(GITHUB_USER, True, CACHING, CACHING_TIME):
        if repo['name'] == repo_name:
            return render_template('project.html', repo=repo, url=f'https://raw.githubusercontent.com/{GITHUB_USER}/{repo_name}/main/portfolio/thumbnails')
    abort(404)
