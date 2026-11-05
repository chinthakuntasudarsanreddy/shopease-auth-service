\# ShopEase Authentication Microservice



\## Project Overview



ShopEase Authentication Microservice is an independent authentication service developed using FastAPI, MySQL, SQLAlchemy, Alembic, and JWT. It provides secure user registration, login, token verification, profile access, and password management.



\## Technology Stack



\- \*\*Backend:\*\* Python, FastAPI

\- \*\*Database:\*\* MySQL 8

\- \*\*ORM:\*\* SQLAlchemy

\- \*\*Migrations:\*\* Alembic

\- \*\*Authentication:\*\* JWT (JSON Web Tokens)

\- \*\*Password Security:\*\* Passlib and bcrypt

\- \*\*Validation:\*\* Pydantic

\- \*\*Containerization:\*\* Docker and Docker Compose

\- \*\*API Documentation:\*\* Swagger UI



\## Features



\- User registration with input validation

\- Unique email validation

\- Secure password hashing

\- JWT-based login authentication

\- Access token generation and expiration

\- Protected user profile endpoint

\- JWT token verification

\- Change password with current-password verification

\- Role-based information in JWT

\- MySQL database integration

\- Database migrations using Alembic

\- Dockerized FastAPI and MySQL services



\## Project Structure



```text

shopease-auth-service/

│

├── app/

│   ├── main.py

│   ├── routers/

│   │   └── auth\_routes.py

│   ├── models/

│   │   └── user\_model.py

│   ├── schemas/

│   │   └── auth\_schema.py

│   ├── services/

│   │   └── auth\_service.py

│   ├── core/

│   │   ├── config.py

│   │   └── security.py

│   └── database/

│       └── connection.py

│

├── alembic/

├── alembic.ini

├── Dockerfile

├── docker-compose.yml

├── requirements.txt

├── .dockerignore

├── .gitignore

├── .env

└── README.md

```



\## Authentication API Endpoints



| Method | Endpoint | Description |

|---|---|---|

| POST | `/api/auth/register` | Register a new user |

| POST | `/api/auth/login` | Authenticate user and generate JWT |

| GET | `/api/auth/me` | Retrieve authenticated user |

| POST | `/api/auth/verify-token` | Verify JWT token |

| POST | `/api/auth/change-password` | Change user password |



\## Installation and Setup



\### 1. Clone the repository



```bash

git clone YOUR\_GITHUB\_REPOSITORY\_URL

cd shopease-auth-service

```



\### 2. Create a virtual environment



```bash

python -m venv venv

```



Activate it on Windows:



```cmd

venv\\Scripts\\activate

```



\### 3. Install dependencies



```bash

pip install -r requirements.txt

```



\### 4. Configure environment variables



Create a `.env` file in the project root.



Configure the following values using your own credentials:



```dotenv

APP\_NAME=ShopEase Authentication Service

APP\_HOST=0.0.0.0

APP\_PORT=8004



DB\_HOST=localhost

DB\_PORT=3306

DB\_USER=your\_database\_user

DB\_PASSWORD=your\_database\_password

DB\_NAME=shopease\_auth\_db



MYSQL\_ROOT\_PASSWORD=your\_mysql\_root\_password



JWT\_SECRET=your\_generated\_secret

JWT\_ALGORITHM=HS256

ACCESS\_TOKEN\_EXPIRE\_MINUTES=30

```



Do not commit `.env` or share your secrets.



\### 5. Run database migrations



```bash

alembic upgrade head

```



\### 6. Start the application locally



```bash

uvicorn app.main:app --reload --port 8004

```



\## Docker Setup



Build the Docker image:



```bash

docker compose build

```



Start the services:



```bash

docker compose up -d

```



Apply database migrations:



```bash

docker compose exec auth-api alembic upgrade head

```



Check running containers:



```bash

docker compose ps

```



View application logs:



```bash

docker compose logs auth-api

```



Stop containers:



```bash

docker compose down

```



\## API Documentation



Once the application is running, access:



\- Swagger UI: `http://127.0.0.1:8004/docs`

\- ReDoc: `http://127.0.0.1:8004/redoc`

\- Health Check: `http://127.0.0.1:8004/health`



\## Database Design



\### Users Table



| Column | Description |

|---|---|

| id | Primary key |

| full\_name | User's full name |

| email | Unique email address |

| password\_hash | Hashed password |

| role | User role |

| is\_active | Account status |

| created\_at | Account creation timestamp |

| updated\_at | Last update timestamp |



\## Security Features



\- Passwords are stored as bcrypt hashes.

\- JWT tokens are signed using a secret key.

\- Token expiration is configured.

\- Protected endpoints validate bearer tokens.

\- Registration prevents duplicate email addresses.

\- Password changes require current-password verification.

\- Environment secrets are excluded from Git.



\## Testing



The following functionality has been tested:



\- User registration

\- User login

\- JWT token generation

\- Authenticated user profile

\- Token verification

\- Password change

\- Duplicate email rejection

\- Invalid login rejection

\- Docker API health check

\- Docker MySQL connectivity

\- Alembic database migration



\## Project Objective



To develop an independent, secure, and reusable authentication microservice that can be integrated with other ShopEase services, such as the Product Service and other e-commerce modules.



\## License



This project is developed for educational and demonstration purposes.



