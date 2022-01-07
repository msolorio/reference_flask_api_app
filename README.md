## Flask Demo
A demo implementation of
- Flask
- SQLAlchemy
- Marshmallow
- PostgreSQL
- Flask Migrate

To be used as a reference for new Flask projects.

---

### Steps to Run

Create a postgres database
`$ createdb flask_postgres`

Run the Bootsrap
`$ ./bootstrap.sh`

This will
- set necessary environment variables
- start virtual environment
- create app
- run app at http://localhost:5000

Create Tables in PostgreSQL
`$ ./migrate 'Initial migration'`

---

### Test in browser or HTTP client

returns all cats<br>
`GET /cats`

returns a single cat<br>
`GET /cats/<int:cat_id>`

creates a cat<br>
`POST /cats { "name": "cat name", "age": 1, "color": "speckled" }`

deletes a cat<br>
`DELETE /cats/<int:cat_id>`
```
