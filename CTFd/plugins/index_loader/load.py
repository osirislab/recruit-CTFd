# Plugin Entry Point
# from CTFd.api import CTFd_API_v1
from flask import render_template
# from CTFd.utils.decorators import admins_only


def load(app):
    # app.view_functions["views.settings"] = view_settings
    @app.route("/")
    def index():
        return render_template("index.html")
