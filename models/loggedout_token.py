from .base_model import BaseModel
from peewee import *

class LoggedoutToken(BaseModel):

    token = CharField(max_length=200, unique=True)


def make_loggedout_token_if_new(token):

    if is_token_in_loggedout_tokens(token) is False:
        # It is okay to have a duplicate just means we will ignore adding it
        LoggedoutToken.create(token=token)


def is_token_in_loggedout_tokens(token):
    return LoggedoutToken.get(LoggedoutToken.token == token) is not None
