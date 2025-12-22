# Troubleshoot

This repo is created to troubeshoot how to
do reverse proxy with prefix for multiple Django
projects.

## Commands

```bash
docker compose down nginx && docker compose up nginx --build -d
docker compose down app0 && docker compose up app0 --build -d
docker compose down app1 && docker compose up app1 --build -d
docker compose down app2 && docker compose up app2 --build -d

```
