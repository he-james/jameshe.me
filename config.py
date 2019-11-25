# enable development enviornment
DEBUG = True

# app directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# SQLite db, if needed
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
DATABASE_CONNECT_OPTIONS = {}

# application threads
THREADS_PER_PAGE = 2

# CSRF
CSRF_ENABLED = True

# Secret Keys
CSRF_SESSION_KEY = "in43ng0rewvmdnfv0in3qroivadv09wq309ufwaouds09tu4398hq9waur09szdf09ae"
SECRET_KEY = "09rjq0394jf093jvq0943jf0943jf093jfwareiijfaiewjv09zjucx9vzu"

