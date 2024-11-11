# The Analytica Dummy Tool

## Description
<!-- One liner explaining the idea and goal of the tool -->
The sceleton of a new catalyst analytica tool that can be used to facilitate the development of new tools.


## How to add a new tool to the Catalyst Analyitcs Tool - A Step by Step Guide

### Step 1: Create the tool in a new repository using dash
1. Create the tool (preferably using dash)
1. For consistency name the main file **app.py**
1. Make sure ***gunicorn*** is in the requirements.txt file

#### What did I just do?
The tool is now working by itself and should run locally without crashing

### Step 2: Create a Docker file
<!-- gunicorn, etc.... -->
1. Create a ***Docker*** file in the project/tools root directory. 
You can use this one most of the time:
``` Docker
FROM python:3.11-slim

COPY requirements.txt .
RUN pip install --no-cache-dir --requirement requirements.txt
COPY . .

EXPOSE 8060

CMD ["gunicorn", "-b", "0.0.0.0:8060", "--timeout", "120", "--workers", "4", "app:server"]
```

#### What did I just do?
The tool is 'dockerized' now, meaning that it can be managed using docker, which the catalyst analytics tool relies upon. 

### Step 3: Create a GitHub Actions Workflow
1. Craete a GitHub Action: ***github.com --> phelas --> Your-repo --> Actions***
1. Click on '***setup workflow by yourself***'
1. Create a new ***'push-main.yml'*** file
    - You can copy this from any of the other tools (it can be found in the tools' root directory under '***.github/workflows/push-main.yml***')
1. Using your admin acces you should now add the GHCR_TOKEN:
    - Go to ***github.com --> phelas --> your-repo --> Settings --> Secrets and Variables --> Actions --> New repository secret***
    - Then paste the Token which can be found in 1Password under '***GitHub User Automation (MachineUser)***' and '***Token phelas party***'

#### What did I just do?
The new tool is now connected to the analytics tool and can be accessed by it

### Step 4: *Deploy the image in the server
******DevOps acces required*****
- ssh into discoverer and create a new folder docker/compositions/catalyst-analytica-tools/tools/your-tool
- add the docker-compose.yml file
- add the .env file
- Use docker in the tool directory:
```bash
docker compose pull
docker compose up -d
docker compose logs -f # (optional)
```

#### What did I just do?


### Step 5: *Deploy the application in Analytica
******DevOps acces required*****
1. Create a new entry in the analytica server config/config.json
```json
    ...
    {
    "path": "/<YOUR-TOOL>",
    "title": "<YOUR-TOOL>",
    "nav_title": "<YOUR-TOOL>",
    "url": "https://<YOUR-TOOL>.catalyst2.phelas.com/"
    }
```
go the the analytica root path and use docker to update the catalyst analytics tool:
```shell
docker compose down
docker compose pull
docker compose up -d
```
#### What did I just do?
You successfully deployed the server on the catalyst analytics server! The new tool should now show up in the side bar and lead the user straight to the new tool.

### Step 6: Updating the tools (optional)
Once the tools are online and some changes are made to the github tool repository in the main branch a simple set of docker commands in the server update the tool to the latest version.

```bash
docker compose down
docker compose pull
docker compose up -d
```

---
