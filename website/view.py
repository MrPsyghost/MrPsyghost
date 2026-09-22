from flask import Blueprint, render_template, redirect, request, flash, session
from .db import *
from random import randint
from urllib.parse import unquote

view = Blueprint('view', __name__)

@view.route('/')
def home():
    return render_template("index.html")
