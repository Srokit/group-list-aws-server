from .base_model import BaseModel
from peewee import *

class LoggedoutToken(BaseModel):

    token = CharField(max_length=200, unique=True)


def make_loggedout_token_if_new(token):

    if LoggedoutToken.select().where(LoggedoutToken.token == token).first() is not None:
        # It is okay to have a duplicate just means we will ignore adding it
        return True, None

    logged_out_token = LoggedoutToken.create(token=token)

    if logged_out_token is not None:
        return True, None

    return False, 'Could not add logged out token %s to list' % token
