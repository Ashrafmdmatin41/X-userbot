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
SESSION = os.environ.get('SESSION', 'BQCIBMcAHJhMtLySx1waLogSIIRij2oivAFY3oJQNH22O79u57QjT3SVX1Y4aeENua9_-0pVxExAKGSUyDrqYk7kl12B8XLkr3Ybhg9s0g4RqBTBm_8lH8LyvGrenInwRWj3cnQtoauTKey3bKs7DfaDhi231NRK63y4eTJJfsaXWsBM0lMF0gJlgT0Sgp0FuLQDmXd_jUFBvujqwwFq6LDGdap84CJBQ49CNl3ZsXVyK_GBwC2lZ9WApUYRLgC8QWCoDnIoZfKixBM7EiuEzqG9USefV3SSNQo7iFNS3579Cv333dwtLwNS_gqSLXLsdFfi0qQUC5g8kowzQFlH6ULFAdhu7QAAAABQBxP_AA')
