# Complete FastAPI masterclass from scratch 2022

Complete FastAPI masterclass from scratch 2022 by Catalin Stefan

## Folder structure

- 03-get-method to 13-dependencies
  - keep adding features and concepts
- 14-ocr: Optical character recognition
- 15-prg-blog
- 17-prg-instagram
- 20-prj-warehouse
  - microservices
  - redis

## Details

<details open>
  <summary>Click to Contract/Expend</summary>

## Section 2: Getting started

### 8. FastAPI features

- Automatic documentation
  - Swagger: http://localhost:8000/docs
  - ReDoc: http://localhost:8000/redoc
- Standard python3
- Security and authentication
- Dependency injection
- Testing - 100% coverage

## Section 3: GET method

### 10. Section overview

- Path parameter
- Predefined values
- Query parameters

## Section 4: Operation description

### 14. Section overview

- Status code
- Tags
- Summary and description
- Response description

## Section 6: Parameters

### 23. Section overview

- Request body
- Path and Query parameters
- Parameter metadata
- Validators
- Multiple values
- Number validators
- Complex subtypes

### 27. Validators

required: `Body(...)` or `Body(Ellipsis)`

## Section 7: Database with SQLAlchemy

### 31. Section overview

- Dependencies quick intro
- Databases in FastAPI
- Create database and tables
- Write data
- Create and read
- Update and delete
- Relationships

### 35. Create database and table

```sh
poetry add sqlalchemy
```

### 37. Create database and table continued

[TablePlus - database tool](https://tableplus.com/)

### 38. Write data in database

```sh
poetry add passlib
poetry add bcrypt
```

```py
# app/schemas.py
# it automates the process from orm to our schema
class Config():
    orm_mode = True

# app/router/user.py
# response model doesn't have id, password, so they will be hidden
@router.post('/', response_model=UserDisplay)
```

## Section 8: Concepts

### 43. Section overview

- Error handling
- Custom responses
- Headers
- Cookies
- Form data
- CORS

### 45. Custom Response

- Standard response is a model, list, database model, dict, etc.
- We can customize the Response object
- No data conversion

#### Why?

- add parameters: Headers, Cookies
- different types of response
  - plain text
  - xml
  - html
  - files
  - streaming
- complex decisional logic
- better docs

[htmlg - online WYSIWYG html editor](https://htmlg.com/html-editor/)

### 46. Headers

- HTTP Headers don't allow `_` (underscore)
  - automatic conversion between `_` and `-`
    - `custom_header` -> `custom-header`

### 48. Form data

```sh
# to use Form, we need this library
poetry add python-multipart
```

### 49. CORS

CORS: Cross Origin Resource Sharing

## Section 9: Authentication

### 50. Section overview

- Authentication
- Securing an endpoint
- Generating access token
- User authentication

### 51. Authentication

- Complex topic
- OAuth2 with username and password

### 54. Generating access token

```sh
# jwt
poetry add python-jose

# generate secret key on terminal
openssl rand -hex 32
# a4fbc3a090deb4ee6da272a666faed145568b95b06fe485a4c007e5641083a55
```

```py
# it must be the same as token url in `auth2.py`, OAuth2PasswordBearer(tokenUrl="token")
@router.post('/token')
```

## Section 10: Working with files

### 59. Making files statically available

```sh
poetry add aiofiles
```

## Section 11: Tasks

### 62. Deployment

- [Deta - free python hosting](https://www.deta.sh/)
- [Deta doc - Getting started](https://docs.deta.sh/docs/micros/getting_started)

```sh
curl -fsSL https://get.deta.dev/cli.sh | sh
deta login
deta new
```

### 63. Debugging

1. Open the folder, `11-tasks`
2. Before debug, set the breakpoint
3. View -> Command Palette (Shift + Command + P)
   - Debug: Restart
     - FastAPI
     - `app.main.py`
   - (or) Debug: Add Configuration
     - FastAPI
     - `app.main.py`
4. the app will run on the vscode terminal and it be able to debug!!!

[FastAPI doc: Debugging](https://fastapi.tiangolo.com/tutorial/debugging/)

### 64. Testing

```sh
poetry add --dev pytest httpx
```

```sh
pytest
# =============================== test session starts ================================
# platform darwin -- Python 3.10.8, pytest-7.2.0, pluggy-1.0.0
# rootdir: /Users/noah/Documents/study/study_codes/udemy/fastapi-masterclass-catalin/fastapi-masterclass-catalin-git/11-tasks
# plugins: anyio-3.6.2
# collected 4 items

# tests/test_main.py ....                                                       [100%]

# ================================ 4 passed in 0.72s =================================
```

> this file, `tests/__init__.py` is necessary for testing. \
> without the init file, testing will be failed.

### 65. Logging

```sh
docker exec -it 11-tasks-app-1 bash
/usr/src# ls
/usr/src# cat log.txt
```

## Section 12: More concepts

### 66. Section overview

- Async await
- Templates
- Middleware
- Background tasks
- WebSockets

### 68. Templates

```sh
poetry add jinja2
poetry add aiofiles
```

Check the response on the [Real time HTML Editor](`https://htmledit.squarefree.com/`)

### 72. Web sockets

```sh
poetry add websockets
```

## Section 13: Dependencies

### 73. Section overview

- Dependencies
- Class dependencies
- Multi level dependencies
- Global dependencies

## Section 14: OCR application

### 78. Intro

OCR: Optical Character Recognition

- Very simple
- Why?
  - confidence
  - bragging rights
  - Frontend - API - Backend
- `Tesseract` and `pytesseract`

### 79. OCR API functionality

[Tesseract by Google](https://github.com/tesseract-ocr/tesseract#about)

```sh
brew install tesseract
poetry add fastapi uvicorn python-multipart aiofiles pytesseract
```

Attach any image file with text. The library will read the text. Awesome!!

> but tesseract should be installed on the server\
> so with the current setting with docker-compose, it won't read the image. \
> run it on the local, it works!!!! it's amazing
>
> - `poetry shell`
> - `uvicorn app.main:app --host=0.0.0.0 --timeout-keep-alive=0 --port=8000 --reload`

## Section 15: Blog site - FastAPI

### 81. Project setup

```sh
poetry add fastapi \
  uvicorn \
  sqlalchemy \
  python-multipart \
  aiofiles
```

## Section 17: Instagram - FastAPI

### 98. FastAPI requirements

- Signup, Login, Logout
- Upload an image with a caption
- Retrieve and display all posts
- Delete a post
  - only available to its creator
- Comment on a post

### 99. Project setup

```sh
poetry install
poetry shell
uvicorn app.main:app --port=8000 --reload
```

## Section 17: Instagram - FastAPI

### 101. Database setup

```sh
poetry add sqlalchemy
```

### 103. Password encryption

```sh
poetry add passlib bcrypt
```

### 106. Upload image

```sh
poetry add python-multipart aiofiles
```

### 108. Authentication

```sh
# jwt
poetry add python-jose

# generate secret key on terminal
openssl rand -hex 32
# e49b4b8d9831aefe01760969131242bbe173d684ef0c3832c53fb3250b045541
```

### 118. Post header

```sh
# npm install @material-ui/core // v4

# v5
npm install @mui/material @emotion/react @emotion/styled
```

### 121. Signup dialog

```sh
npm install tss-react
```

## Section 20: Warehouse app with Microservices and Redis

### 168. Initialize project and Redis database

```sh
poetry init
poetry add fastapi uvicorn autopep8
poetry add redis-om
```

### 170. Store microservice

```sh
# Copy `pyproject.toml` file from api-warehouse
poetry install
poetry add requests
```

### 172. Update product

```sh
poetry shell
python fullfillment.py
# BUSYGROUP Consumer Group name already exists
# []
# []
# []
```

### 174. Create web project

```sh
npx create-react-app web
npm install react-router-dom
```

### 176. Products UI

[CSS Scan Buttons](https://getcssscan.com/css-buttons-examples)

</details>
