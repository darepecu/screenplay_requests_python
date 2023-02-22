# Screenplay using pytest-bdd, screenpy with python

---

## Config environment

```bash
    python3 -m venv env-python
    source env-python/bin/activate
    pip3 install --upgrade --force-reinstall -r requirements.txt
```

For end the local environment use `deactivate`
and start the env use `source env-python/bin/activate`

## Up Docker compose

```bash
    docker compose -f "docker-compose.yml" up -d --build 
```

## Run test

```bash
    pytest --alluredir=./tmp/allure-results --log-cli-level=info  
```

## Open Report

<http://localhost:9988/allure-docker-service/projects/default/reports/latest/index.html>
