# generate.py
import os
import toml
from dotenv import load_dotenv
from pathlib import Path
load_dotenv()

HOSTS_FILE = Path("/frp/data/hosts")
OUTPUT_TOML = Path("/frp/config/frpc.toml")

def parse_hosts():
    proxies = []
    with open(HOSTS_FILE, "r") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split()
            if len(parts) != 2:
                continue
            ip, domain = parts
            name = domain.replace(".", "_")  # proxy name can't have dots
            proxies.append({
                "name": f"{name}_http",
                "type": "http",
                "localIP": ip,  # resolved from /etc/hosts
                "localPort": 80,
                "customDomains": [domain]
            })
            proxies.append({
                "name": f"{name}_https",
                "type": "https",
                "localIP": ip,  # resolved from /etc/hosts
                "localPort": 443,
                "customDomains": [domain]
            })
    return proxies

def generate_config():
    token = os.getenv("FRP_AUTH_TOKEN")
    if not token:
        raise ValueError("FRP_AUTH_TOKEN is not set in the environment.")
    
    server_addr = os.getenv("FRP_SERVER_ADDR")
    if not server_addr:
        raise ValueError("FRP_SERVER_ADDR is not set in the environment.")
    
    config = {
        "serverAddr": server_addr,  # or any FRPS public IP/domain
        "serverPort": 7000,
        "proxies": parse_hosts(),
         "auth": {
        "method": "token",
        "token": token
    }
        
    }
    OUTPUT_TOML.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_TOML, "w") as f:
        toml.dump(config, f)
    print("✅ frpc.toml generated from hosts file")

if __name__ == "__main__":
    generate_config()