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
SESSION = os.environ.get('SESSION', 'BQCIBMcAYEOIDLlEo6JqLBX5_NAVMkxlQGx3tr13oyVj3c47yWYpnHUKx45hqCFWHOiWEBocQgANsFkMBu8G3MV8hlBJzDPSG5pvpA-sjJ7bPAb-anMsZapdU9DSyFHQgMTIWvTKZscTul2VO8s3icQqJrzcGx6cFEbnLGQyYg62uMHF2EoMP8NyLJWmxoOUvH-nNTLlaWMnQpuJyGHWZ0N1a4jclbpciUYS5Q9HyPE-ZKlDFERoxOMgkh7z_rmFzAzBfbLaPp3MmQbWEkDlTPD8H5okCqn9cNOTFjfxsDQ227z_cA3S5C3siXqjTxep0W5iBmgW9F-XUOGpfWXi4vtFcJE52AAAAABQBxP_AA')
