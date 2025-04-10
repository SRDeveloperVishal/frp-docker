# generate.py
import toml
from pathlib import Path

HOSTS_FILE = Path("./hosts")
OUTPUT_TOML = Path("./config/frpc.toml")

frpc_config = {
    "serverAddr": "40.81.224.57",
    "serverPort": 7000,
    "proxies": []
}

# Read the hosts file (format: domain ip[:port])
with HOSTS_FILE.open() as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split()
        if len(parts) != 2:
            continue

        domain, address = parts

        if ":" in address:
            ip, port = address.split(":")
            port = int(port)
        else:
            ip = address
            port = 80

        name_base = domain.replace(".", "_")

        # Always create both HTTP and HTTPS if port is 80 or 443
        if port == 80:
            frpc_config["proxies"].append({
                "name": f"{name_base}_http",
                "type": "http",
                "localIP": ip,
                "localPort": 80,
                "customDomains": [domain]
            })
        elif port == 443:
            frpc_config["proxies"].append({
                "name": f"{name_base}_https",
                "type": "https",
                "localIP": ip,
                "localPort": 443,
                "customDomains": [domain]
            })
        else:
            # For custom ports, just default to TCP forwarding
            frpc_config["proxies"].append({
                "name": f"{name_base}_tcp_{port}",
                "type": "tcp",
                "localIP": ip,
                "localPort": port,
                "remotePort": port
            })

# Write to TOML
OUTPUT_TOML.parent.mkdir(parents=True, exist_ok=True)
with OUTPUT_TOML.open("w") as f:
    toml.dump(frpc_config, f)

print("✅ frpc.toml generated from hosts")
