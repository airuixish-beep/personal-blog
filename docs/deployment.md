# Deployment Guide

AI Lab 7 is designed to run on a small Linux VPS for educational demonstrations.

## Recommended environment

- Ubuntu 24.04 LTS
- 2 vCPU
- 4 GB RAM
- 50 GB SSD
- Python 3.12+
- Nginx
- Docker (optional)

## Local start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## Intended server use

The hosted service will provide public educational documentation, lightweight API demonstrations, prompt experiments, and sample application endpoints. Large model inference is not planned to run locally on the server; external APIs or small mock examples will be used instead.

No commercial hosting, token resale, cryptocurrency mining, VPN/proxy service, bulk email, or resource resale is part of this project.
