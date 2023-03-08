
# user-service

This is user-service of library project and has connection with [communication-lyer](https://github.com/Zahra-Nasiri/communication-layer)
 and [book-service](https://github.com/Zahra-Nasiri/book-service)
 projects.


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`MONGO_DB_URL`

`DB`

`user_collection`

`token_collection`


## Tech Stack

* python
* fastapi
* mongodb




## Installation

Install my-project with pip

```bash
  python -m venv venv
  venv\scripts\activate
  pip install -r requirements.txt
```

## Running Tests

To run tests, run the following command

```bash
  pytest
```


## Run Locally

Clone the project

```bash
  git clone https://github.com/Zahra-Nasiri/user-service
```

Go to the project directory

```bash
  cd user-service
```

Install dependencies

```bash
  python -m venv venv
  venv\scripts\activate
  pip install -r requirements.txt
```

Start the server

```bash
  uvicorn main:app --reload
```

## API Reference

#### Register a user

```http
  POST /register
```

#### login a user

```http
  POST /login
```

#### update a user

```http
  PATCH /{uid}
```

```http
  GET /
```


| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `token` | `string` | **Required**. Your token |

## Authors

- [Zahra-Nasiri](https://github.com/Zahra-Nasiri)


## 🚀 About Me
I'm a  back-end developer...

you can read more about me on my [linkedin account](https://www.linkedin.com/in/zahra-nasirmohammadi-73584b241/)
