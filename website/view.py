from flask import Blueprint, render_template#, redirect, request, flash, session
from .db import *
from .github import get_repos

view = Blueprint('view', __name__)

GITHUB_USER = 'MrPsyghost'

@view.route('/')
def home():
    repos = get_repos(GITHUB_USER)
    return render_template("index.html", repos=repos)
