# Auth API

## docker

```
docker run --name authapi -v $pwd:/app --rm -p 8081:8081 -it anypythondockerimage bash
```


## setup

```
pip install --upgrade pip
pip install -r requirements.txt

cd app
python3 -m flask db init
python3 -m flask db migrate
python3 -m flask db upgrade

python3 seed.py

SECRET_KEY="mysecretkeysomesecrets" python3 app/app.py
```
