# Goals

- Figure out the Django authentication module.
- Practice without looking doc.

## TODO

- [x] Create views.py in mysite
  - [x] a "Hello world" http response
- [ ] Create home page template
  - [x] create "template" folder for project and change "settings.py"
  - [ ] create "static" folder for "js" and "css" file
  - [x] create "base.html"
  - [x] create "index.html" inherit "base.html"
  - [x] create `index()` in view and change "urls.py"
- [ ] Setup SQL server to django
  - [x] install `mssql-django`
  - [x] run django migration command
  - [ ] go to SQL server to check if default user model has been created
  - [x] create superuser for project
- [x] use django admin to create some test user
- [ ] Create user profile page to show user message
  - [x] create `profile.html` template
  - [x] `profile(username)` in view
  - [ ] add permission control to `profile(username)` function
- [ ] Create user login page
  - [ ] view
  - [ ] template
- [ ] Create user logout page
  - [ ] view
  - [ ] template