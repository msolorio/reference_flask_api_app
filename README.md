## Flask Demo
A demo implementation of
- Flask
- SQLAlchemy
- Marshmallow
- PostgreSQL
- Flask Migrate
- Swagger

To be used as a reference for new Flask projects.

---

### Steps to Run

Create a postgres database<br>
`$ createdb flask_postgres`

Create Tables in PostgreSQL<br>
`$ ./migrate 'Initial migration'`

Run the Bootsrap<br>
`$ ./bootstrap.sh`

This will
- set necessary environment variables
- start virtual environment
- create app
- run app at http://localhost:5000

---

### Test using Swagger UI
visit `localhost:5000/api/docs`

### Test in browser or HTTP client

returns all automobiles<br>
`GET /api/automobiles/`

returns an single automobiles<br>
`GET /api/automobiles/<int:automobile_id>`

creates an automobiles<br>
`POST /api/automobiles/ { "make": "Aptera", "model": "Paradigm", "year": 2022, "color": "black" }`

deletes an automobiles<br>
`DELETE /api/automobiles/<int:automobile_id>`

updates an automobile<br>
`PATCH /api/automobiles/<int:automobile_id> { "color": "storm trooper" }`
