# WBD - Filharmonia 2

Before working on project activate the virtualenv:
`source env/bin/activate`

Running `run.py` runs Flask server on localhost, port 5000.

Content of `app_filharmonia` package:
- `static` folder: contains CSS file for whole application
- `templates` folder: contains HTML files for every webpage
- `__init__.py`: is responsible for the initial connection with the database and the import of other Python files in the package
- `routes.py`: defines behaviour for available webpages and sets their URL (`@app.route()`)
- `models.py`: defines models corresponding to tables from database
- `forms.py`: defines forms used in project (add/modify/delete records from database)

In order to insert data with polish characters into database, set environment variable `$NLS_LANG` to 
`.AL32UTF8`.
