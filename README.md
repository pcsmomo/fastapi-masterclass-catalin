# Complete FastAPI masterclass from scratch 2022

Complete FastAPI masterclass from scratch 2022 by Catalin Stefan

## Folder structure

-

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
poetry add jose

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

</details>
