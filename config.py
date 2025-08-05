#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8403544311:AAG5eDkyybOv3N_-TmTXyifFO8jtIhuj7r8")
    API_ID = int(os.environ.get("API_ID", "20073998"))
    API_HASH = os.environ.get("API_HASH", "20073998")
    AUTH_USERS = "7991573040"


