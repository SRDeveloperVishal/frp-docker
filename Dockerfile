FROM python:3.10-alpine

WORKDIR /frp

# Install toml lib
RUN pip install toml

# Copy files
COPY frpc /frp/frpc
COPY generate.py /frp/generate.py
COPY entrypoint.sh /frp/entrypoint.sh

RUN chmod +x /frp/frpc /frp/entrypoint.sh

ENTRYPOINT ["/frp/entrypoint.sh"]
