from flask import Blueprint, render_template, abort#, redirect, request, flash, session
from .db import *
from .github import get_repos

view = Blueprint('view', __name__)

GITHUB_USER = 'MrPsyghost'

@view.route('/')
def home():
    repos = get_repos(GITHUB_USER)
    return render_template('index.html', repos=repos)

@view.route('/projects/<repo_name>')
def project(repo_name):
    for repo in get_repos(GITHUB_USER):
        if repo['name'] == repo_name:
            return render_template('project.html', repo=repo, url=f'https://raw.githubusercontent.com/{GITHUB_USER}/{repo_name}/main/portfolio/thumbnails')
    abort(404)
