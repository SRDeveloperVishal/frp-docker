
# Dockerize FRP

Dockerize version of fast reverse proxy that allows you to expose a local server located behind a NAT or firewall to the Internet


## Lets start with FRP

#### Pre-installation Requirements
* A VM with Ubuntu (20.04/22.04 recommended)
* [Docker and Docker Compose installed](https://docs.docker.com/engine/install/ubuntu/)
* At least one VM with a Public IP (to act as the FRP Server)
* Another VM or your local machine as the FRP Client (behind NAT

## Setup FRP Server

#### Clone project
```bash 
  git clone https://github.com/srDeveloperVishal/frp-docker/
```
#### Go inside project
```bash
  cd frp-docker
```
#### Make env file
```bash
  vim .env 
```

#### Add variable 

| Parameter | Description |
| :-------- | :------- | 
| `FRP_AUTH_TOKEN=your_generated_token` | `openssl rand -hex 16` |
| `dash_user=your_username` | `username of your choice` |
| `dash_pass=your_password` | `password of your choice` |

#### Save changes

```bash
  :wq
```
#### Ready to start
```bash
  docker compose -f server.yml up -d
``` 

## Access frps dashboard
```bash
  public_ip:7500
```

## Setup FRP Client
#### Clone project
```bash 
  git clone https://github.com/srDeveloperVishal/frp-docker/
```
#### Go inside project
```bash
  cd frp-docker
```
#### Make env file
```bash
  vim .env 
```
#### Add variable 

| Parameter | Description |
| :-------- | :------- | 
| `FRP_AUTH_TOKEN=your_generated_token` | `Token created  for frp server ` |
| `FRP_SERVER_ADDR=your_server_ip` | `Public ip of frp server` |


#### Save changes

```bash
  :wq
```
#### Edit host file

```bash
  vim data/hosts
```
#### insert by

```bash
 press i
```

#### Add domain enrty with local vm ip

```bash
  192.168.*.* demo.com
```
#### Save changes

```bash
  :wq
```

#### Ready to start

```bash
  docker compose -f client.yml up -d
```

## Authors

- [@srdevelopervishal](https://www.github.com/srdevelopervishal)

