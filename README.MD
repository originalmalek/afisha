# Interactive Map of Moscow

![](screenshots/mysite.png)

[Demo Site](https://originalmalek.pythonanywhere.com/).  
[Json file example](https://raw.githubusercontent.com/devmanorg/where-to-go-frontend/master/places/moscow_legends.json).

Python 3.11

## Running the Site

- Download the code
- Install the dependencies using the command `pip install -r requirements.txt`
- Create the database with the command `python3 manage.py migrate`
- Start the server using the command `python3 manage.py runserver`

## How to Add Data
(Data is stored in the *media/data* folder in *.json* format.)
- To add a file, run the command `python3 manage.py load_place "https://raw.githubusercontent.com/devmanorg/where-to-go-frontend/master/places/moscow_legends.json"`

## Environment Variables

Some of the project settings come from environment variables. 
To define them, create a file named `.env` in the same directory as `manage.py`, 
and write the data in this format: `VARIABLE=value`.

Variables include:
- `DEBUG` — debug mode. Set to `True` to enable debug information in case of errors.
- `SECRET_KEY` — project's secret key
- `SESSION_COOKIE_SECURE` - Determines whether to use a secure cookie for the session cookie. Set to `True`
- `CSRF_COOKIE_SECURE` - Determines whether to use a secure cookie for the CSRF cookie. Set to `True`
- `STATIC` - Static folder. Set 'static'
