import secrets
secret_key=secrets.token_hex(16)
print(f"{secret_key=}") #16 byte length
import os
os.system(f"export FLASK_KEY={secret_key}")