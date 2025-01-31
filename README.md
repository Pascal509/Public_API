PROJECT DESCRIPTION

This is a Flask-based REST API that provides a publicly accessible endpoint to retrieve basic information, including the developer's name, email, GitHub repository link, and the current UTC timestamp.

Additionally, the API includes CRUD (Create, Read, Update, Delete) functionality for managing an "About" section, allowing users to:

Retrieve stored personal entries (GET /about)
Add new entries (POST /about)
Update existing entries (PUT /about/<id>)
Delete entries (DELETE /about/<id>)


HOW TO RUN LOCALLY

git clone https://github.com/Pascal509/Public_API.git
cd Public_API
#Install necessary packages and dependencies; 
pip install flask flask-cors
python app.py
#API would run on default; http://127.0.0.1:5000/ in browser

Use ✅ cURL (Command Line):
# Test the GET request
curl -X GET http://127.0.0.1:5000/

# Test the POST request (Create a new entry)
curl -X POST http://127.0.0.1:5000/about -H "Content-Type: application/json" -d '{"name": "Ezenagu Chinemerem"}'

# Test the PUT request (Update an entry with id 1)
curl -X PUT http://127.0.0.1:5000/about/1 -H "Content-Type: application/json" -d '{"name": "Updated Name"}'

# Test the DELETE request (Delete entry with id 1)
curl -X DELETE http://127.0.0.1:5000/about/1


DEPLOYED END POINT


GET REQUEST
curl -X GET http://127.0.0.1:5000/

RESPONSE(200 OK)
{
  "current_datetime": "2025-01-31T14:24:21.951041Z",
  "email": "chinemeremezenagu@gmail.com",
  "github_url": "https://github.com/Pascal509/Public_API",
  "id": 1,
  "name": "Ezenagu Chinemerem"
}

LINK TO GITHUB REPOSITORY
https://github.com/Pascal509/Public_API

BACKLINK (Python Developers)
https://hng.tech/hire/python-developers