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
SESSION = os.environ.get('SESSION', 'BQCIBMcAZqAcaQcTQ5AGRkKbRkFk3paDkBt-BR1CS0mb-tXMursGuTSdW9HhlW2L1XiuyE2KMYZDjhkY_UyXxabv-PlzLKt1IVvysyNnnrpTxlpO9TKcWGbRKTH6K9CoedOCMEzVyCotFFvqCL3FheV8vaIjCcaHt9ERI1fUwhRAPVm9LTYldAjV7m5LESjgQMLQUVylMg9Vnv9PDfnY6LPh4ndlNvsAdacpG4bs3nS12YRDzSYQmc9l3D3tiBC4E9LFMm3cldp54787Pa2nqAFi1oHb93zIgLhOyOo0bIQt3CroUT3SQLBRXqd4K5zwYBbrCtlYb4othOWXqTtefypNXpgi7wAAAABQBxP_AA')
