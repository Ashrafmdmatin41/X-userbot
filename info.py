import re
import os
from os import environ
from pyrogram import enums

import asyncio
import json
from pyrogram import Client

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.strip().lower() in ["on", "true", "yes", "1", "enable", "y"]: return True
    elif value.strip().lower() in ["off", "false", "no", "0", "disable", "n"]: return False
    else: return default

API_ID = int(os.environ.get('API_ID', '8914119'))
API_HASH = os.environ.get('API_HASH', '652bae601b07c928b811bdb310fdb4b0')
SESSION = os.environ.get('SESSION', 'BQCIBMcAwCOxlNyOa9BWN-TVfANE70w3Wzs5crjJZPTP6XdPoibpz4Rm77GE8TvmnyvoNojW-aXbg7Fo4x-fAhquMSkKN1p04bkBc2kqrC8iymbM7uNI3ms5SycC_5qrOJkEEp3b_CvoyRv7kMqlmTyy2f_WLHp6OL_lrMt5j7KFbDYoXL7fUl20HIP5k8FZqgJI5EvpwWSboGm-EadJIvAaeAS84tfv_Mwv2_fOU5f2zYl6PTcNZPDqnGmgoTpiJBPUF8esa8ktKlAJvOvNwh9pvnwDkXVTtem6B6_m1tju1HyGMIIgtsBqRF3fNPoeCpFMSv6sc1tRT5BJFf4Kln009AnAAAAABQBxP_AA')
