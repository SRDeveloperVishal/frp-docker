# generate.py
import os
import toml
from dotenv import load_dotenv
from pathlib import Path
load_dotenv()

OUTPUT_TOML = Path("/frp/config/frps.toml")

def generate_config():
    token = os.getenv("FRP_AUTH_TOKEN")
    if not token:
        raise ValueError("FRP_AUTH_TOKEN is not set in the environment.")
    
    user = os.getenv("dash_user")
    if not user:
        raise ValueError("dash_user is not set in the environment.")
    
    passwd = os.getenv("dash_pass")
    if not passwd:
        raise ValueError("dash_pass is not set in the environment.")
    
    config = {
    "bindPort": 7000,
    "vhostHTTPPort": 80,
    "vhostHTTPSPORT": 443,
    "auth": {
        "method": "token",
        "token": token,
    },
    "webServer": {
        "addr": "0.0.0.0",
        "port": 7500,
        "user": user,
        "password": passwd
    }
    }

    OUTPUT_TOML.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_TOML, "w") as f:
        toml.dump(config, f)
    print("✅ frps.toml generated from hosts file")

if __name__ == "__main__":
    generate_config()