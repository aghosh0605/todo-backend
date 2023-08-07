# todo-backend

Please look into the problem [here](./Problem.pdf)

## Important Commands to setup project

```bash
python3 -m venv env               # Set up a virtual environment
source env/bin/activate           #	Activate the virtual environment
python -m pip install django
python -m pip freeze > requirements.txt        # Install Django
django-admin startproject backend       # Set up a Django project
python manage.py startapp todo          # Start a Django app
```

**Django Admin Dashboard Username and Password**

- username: admin
- password: github

## How to start

- Clone the repo with `git clone https://github.com/aghosh0605/todo-backend.git`
- cd into the folder `cd todo-backend`
- Install the python dependencies `pip install -r requirements.txt` or `python3 -m pip install -r requirements.txt`
- cd into the Django project root directory `cd backend`
- Run the below commands

```bash
python3 manage.py makemigrations  # Responsible for creating new migrations based on the changes you have made to your models
python3 manage.py migrate   # Responsible for applying and unapplying migrations.
python3 manage.py runserver         # TO start the server
```

## Importtant Commands to depoy with Nginx Reverse Proxy

1. **Run the command on your server**

Tested with Ubuntu 20.04LTS

```bash
cd /etc/nginx/sites-available/
touch task.cybersupport.in
ln -s /etc/nginx/sites-available/task.cybersupport.in /etc/nginx/sites-enabled/task.cybersupport.in
nano task.cybersupport.in
```

2. **paste the content into nano**

```bash
server {
	server_name task.cybersupport.in;


        location / {
                proxy_pass http://localhost:7070;
                proxy_set_header Host $host;
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                proxy_set_header X-Forwarded-Proto $scheme;
        }
        listen 80;
        listen [::]:80;
}
```

3. **Point your applied FQDN to the server IP with A record(IPv4 Address) in your DNS Records**
4. **Run the below commands**

```bash
nginx -t
certbot --nginx -d task.cybersupport.in
nginx -s reload
```

## API Endpoints

### Request

`POST /api/v1/todo/create`

| Body          | Type     | Description                                             |
| :------------ | :------- | :------------------------------------------------------ |
| `title`       | `string` | **Required**. Title of Todo                             |
| `description` | `string` | **Required**. Description of Todo                       |
| `due_date`    | `string` | Due date to complete Todo                               |
| `tags`        | `string` | Tags to attach with Todo                                |
| `status`      | `string` | Status of Todo. Default "O". Accepts "O", "W", "D", "V" |

### Response

```JSON
{
    {
    "id": number,
    "due_date": string,
    "tags": [
        {
            "id": number,
            "title": string
        },
        {
            "id": number,
            "title": string
        }
    ],
    "timestamp": string,
    "title": string,
    "description": string,
    "status": string
}
}
```

`GET /api/v1/todo/fetch`

### Response

```JSON
[
    {
    "id": number,
    "due_date": string,
    "tags": [
        {
            "id": number,
            "title": string
        },
        {
            "id": number,
            "title": string
        }
    ],
    "timestamp": string,
    "title": string,
    "description": string,
    "status": string
}
]
```

`GET /api/v1/todo/fetch/<int:id>`

### Response

```JSON
{
    {
    "id": number,
    "due_date": string,
    "tags": [
        {
            "id": number,
            "title": string
        },
        {
            "id": number,
            "title": string
        }
    ],
    "timestamp": string,
    "title": string,
    "description": string,
    "status": string
}
}
```

`PATCH /api/v1/todo/update`

| Body          | Type     | Description                                                           |
| :------------ | :------- | :-------------------------------------------------------------------- |
| `id`          | `number` | **Required**. ID of Todo                                              |
| `title`       | `string` | **Required**. Title of Todo                                           |
| `description` | `string` | **Required**. Description of Todo                                     |
| `due_date`    | `string` | **Required**. Due date to complete Todo                               |
| `tags`        | `string` | Tags to attach with Todo                                              |
| `status`      | `string` | **Required**. Status of Todo. Default "O". Accepts "O", "W", "D", "V" |

### Response

```JSON
{
    "due_date": string,
    "title": string,
    "description": string,
    "status": string
}
```

`DELETE /api/v1/todo/delete/<int:id>`

### Response

```JSON
{
    "message": string
}
```
