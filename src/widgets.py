from flask_login import current_user
from src import app


def campaigns_list():
    campaigns = current_user.campaigns
    return campaigns


app.jinja_env.globals.update(campaigns_list=campaigns_list)
