import os
import subprocess
from django.conf import settings
def convert_bech32_to_hex(address):
    """Converts bech32 address to hex address"""
    process = subprocess.run([settings.KEY_CONVERTR_PATH, '--to-hex', address,], capture_output=True)
    hex_key = str(process.stdout).replace("b'", '').replace("\\n'", '')
    return hex_key