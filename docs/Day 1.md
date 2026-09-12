# Day 1: Project Setup and First FastAPI Endpoint

## 1. What we achieved

We established the project structure, created a Python virtual environment, installed FastAPI and Uvicorn, built a working GET endpoint, and made our first Git commit.

The browser successfully displayed:

```json
{"message": "Personal Finance API is running"}
```

The application currently returns a fixed message. We have not added a frontend, database, or authentication yet.

## 2. Tools and their roles

| Tool | Purpose |
|---|---|
| Python | Runs our backend code |
| FastAPI | Defines API endpoints and handles requests and responses |
| Uvicorn | Runs the web server that serves our FastAPI application |
| VS Code | Editor for writing code |
| Git | Tracks changes and saves local code history |
| GitHub | Hosts Git repositories online; publishing was not part of this setup |
| Node.js and npm | Will support React and Vite development later |

Git and GitHub are different: Git works locally; GitHub is a service where we can publish and collaborate on Git repositories.

## 3. Initial project structure

```text
personal-finance-app/
├── .git/
├── .gitignore
├── README.md
├── Day 1.md
├── personal-finance-app-documentation.md
├── backend/
│   ├── .venv/
│   ├── __pycache__/
│   ├── main.py
│   └── requirements.txt
└── frontend/
```

| File or folder | Purpose |
|---|---|
| `.git/` | Git's internal repository data and history |
| `.gitignore` | Rules identifying files Git should leave untracked |
| `README.md` | Project overview and instructions for running it |
| `Day 1.md` | This setup guide and study notes |
| `personal-finance-app-documentation.md` | Personal project notes |
| `backend/` | Python API code |
| `backend/.venv/` | Local Python environment and installed packages |
| `backend/__pycache__/` | Automatically generated Python bytecode cache |
| `backend/main.py` | Our FastAPI application and first route |
| `backend/requirements.txt` | Snapshot of installed Python dependencies |
| `frontend/` | Reserved for our future React application |

Git does not track empty directories, so an empty `frontend/` folder will not appear in commits.

## 4. Creating the folders and initializing Git

These are reference commands for the setup already performed. They do not need to be repeated.

First, we selected the project directory:

```powershell
Set-Location "C:\Users\shahz\Desktop\personal-finance-app"
```

We created separate backend and frontend directories:

```powershell
New-Item -ItemType Directory -Path backend, frontend
```

We initialized a local Git repository with a branch named `main`:

```powershell
git init -b main
```

We checked the repository state:

```powershell
git status
```

At that point, `No commits yet` meant Git was initialized but no snapshots had been saved.

## 5. Creating a Python virtual environment

A virtual environment gives a project its own Python packages. One project can use one FastAPI version while another uses a different version without their installations interfering.

We created the environment using Python 3.13:

```powershell
py -3.13 -m venv backend\.venv
```

| Part | Meaning |
|---|---|
| `py -3.13` | Select Python 3.13 |
| `-m venv` | Run Python's built-in virtual environment module |
| `backend\.venv` | Create the environment at this location |

We explicitly selected Python 3.13 because the machine's `python` and `py` commands initially selected different Python versions.

### Activating the environment

Activation adjusts the current terminal's environment so commands such as `python` use our project's interpreter:

```powershell
.\backend\.venv\Scripts\Activate.ps1
```

The prompt then displayed:

```text
(.venv) PS C:\Users\shahz\Desktop\personal-finance-app>
```

We verified the interpreter with:

```powershell
python -c "import sys; print(sys.executable)"
```

Expected path:

```text
C:\Users\shahz\Desktop\personal-finance-app\backend\.venv\Scripts\python.exe
```

Creating and activating are different: create the environment once; activate it again when opening a new terminal for backend work. Use single backslashes in these PowerShell paths; the doubled backslashes used during setup were accepted on Windows but were unnecessary.

## 6. Installing FastAPI and Uvicorn

With the environment active, we installed both packages:

```powershell
python -m pip install fastapi uvicorn
```

`pip` installs Python packages. Using `python -m pip` ensures we run the installer associated with the selected Python interpreter.

The packages have different responsibilities:

- Uvicorn listens for incoming HTTP requests.
- FastAPI matches requests to routes and prepares responses.

We checked their installed versions:

```powershell
python -c "import fastapi, uvicorn; print('FastAPI:', fastapi.__version__); print('Uvicorn:', uvicorn.__version__)"
```

The output during our setup was:

```text
FastAPI: 0.141.1
Uvicorn: 0.52.4
```

The pip upgrade notice was informational, not an installation failure.

## 7. Recording dependencies

We recorded installed packages and their exact versions:

```powershell
python -m pip freeze | Out-File -Encoding utf8 backend\requirements.txt
```

- `pip freeze` lists installed packages in requirements-file format.
- `|` passes that output to the next command.
- `Out-File` writes it into `backend\requirements.txt`.
- `-Encoding utf8` specifies the text encoding.

The file includes FastAPI, Uvicorn, and packages they depend on.

Someone recreating the project can install the recorded dependencies with:

```powershell
python -m pip install -r backend\requirements.txt
```

Here, `-r` means to read package requirements from this file.

We commit `requirements.txt`, not `.venv/`. The environment can be recreated locally.

## 8. Writing our first endpoint

We created `backend/main.py`:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Personal Finance API is running"}
```

### Importing FastAPI

```python
from fastapi import FastAPI
```

This imports the `FastAPI` class from the installed `fastapi` package.

### Creating the application

```python
app = FastAPI()
```

This creates an application object and stores it in `app`. Our routes are registered on this object.

### Registering a route

```python
@app.get("/")
```

This is a decorator: syntax that attaches behavior to the function directly below it. Here, it registers that function to handle HTTP method `GET` at URL path `/`.

A GET request asks to retrieve information. `/` is the root path.

### Defining the function

```python
def read_root():
```

- `def` defines a Python function.
- `read_root` is its name.
- `()` means it has no declared parameters.
- `:` begins its body.

The function name does not determine the URL. The decorator does. Ordinary `def` is sufficient for this endpoint.

### Returning a response

```python
    return {"message": "Personal Finance API is running"}
```

The four-space indentation makes this line part of the function.

The returned value is a Python dictionary with a key named `message`. FastAPI converts it into a JSON response.

Python dictionaries and JSON look similar here, but they are different: the dictionary exists in Python; JSON is the data format sent to the browser.

## 9. Starting the development server

From the project root, we ran:

```powershell
python -m uvicorn main:app --app-dir backend --reload
```

| Part | Meaning |
|---|---|
| `python -m uvicorn` | Run Uvicorn using the selected Python environment |
| `main:app` | Import the object `app` from the module `main` |
| `--app-dir backend` | Look inside `backend` when importing the application |
| `--reload` | Restart the server when source files change during development |

We opened:

```text
http://127.0.0.1:8000/
```

- `127.0.0.1` refers to our own computer.
- `8000` is the server's port.
- `/` matches the path registered with `@app.get("/")`.

The request flow was:

```text
Browser sends GET /
        ↓
Uvicorn receives the request
        ↓
FastAPI finds the matching route
        ↓
read_root() returns a dictionary
        ↓
FastAPI prepares a JSON response
        ↓
Uvicorn sends the response to the browser
```

The browser displayed the JSON as a table. That was just its presentation of the response.

To stop the server, press Ctrl+C in its terminal.

## 10. Interactive API documentation

FastAPI provides interactive documentation at:

```text
http://127.0.0.1:8000/docs
```

With the server running:

1. Expand GET /.
2. Click Try it out.
3. Click Execute.
4. Inspect the response body and status code.

The expected response status is 200 OK, meaning the request succeeded.

At the time these notes were saved, the `/docs` result had not yet been confirmed.

## 11. Saving work with Git

Git's basic workflow is:

```text
Edit files → Stage selected changes → Commit a snapshot
```

We discussed staging everything eligible under the current directory:

```powershell
git add .
```

The `.` means the current directory. At the project root, this stages changes throughout the project, subject to ignore rules for untracked files. The active Python virtual environment does not affect Git.

Alternatively, select files explicitly:

```powershell
git add .gitignore README.md backend/main.py backend/requirements.txt
```

To review staged changes:

```powershell
git diff --cached --stat
```

Then we created the first commit:

```powershell
git commit -m "Set up FastAPI backend with initial GET endpoint"
```

Git reported commit `16ef1a4`.

Finally, this command reported a clean working tree:

```powershell
git status
```

A clean working tree means there are no pending changes; it does not guarantee that every committed file belongs in the repository. A commit is local and does not upload anything to GitHub.

## 12. The Git mistake we discovered

The first commit included:

```text
backend/__pycache__/main.cpython-313.pyc
```

Inspection showed that `.gitignore` was empty. Therefore, it had no rule excluding Python's generated cache.

The intended `.gitignore` contents are:

```gitignore
# Python
.venv/
__pycache__/
*.pyc

# Local environment configuration
.env
.env.*
!.env.example

# Frontend
node_modules/
dist/
```

The `!` rule allows a future `.env.example` file to be tracked. That file should contain placeholders, not actual secrets.

### Why adding the rule alone is not enough

`.gitignore` applies to untracked files. The cache file was already committed, so we also need to stop tracking it.

After saving the ignore rules, this command removes the cache directory from Git's index while keeping the files on disk:

```powershell
git rm -r --cached backend/__pycache__
```

Stage the ignore rules:

```powershell
git add .gitignore
```

Review the pending changes. Expect the ignore rules to change and the cache file to appear as deleted from Git:

```powershell
git diff --cached --stat
```

Commit the cleanup and check the repository state:

```powershell
git commit -m "Ignore generated Python files and local dependencies"
git status
```

This records the cleanup in a new commit. It does not erase the file from the earlier commit's history.

At the time these notes were saved, this cleanup had been explained but had not been confirmed as completed.

## 13. README documentation

The README explains what the project does, distinguishes current progress from planned features, and tells someone how to run the backend.

Its setup instructions should include Python 3.13 as a prerequisite, creating and activating the environment, installing `backend/requirements.txt`, and starting Uvicorn. It should also link to the local endpoint and `/docs`.

Documenting these commands does not mean running the entire setup again each day.

## 14. Starting the project next time

There is no need to recreate the environment or reinstall packages every time.

Navigate to the project:

```powershell
Set-Location "C:\Users\shahz\Desktop\personal-finance-app"
```

Activate the existing environment:

```powershell
.\backend\.venv\Scripts\Activate.ps1
```

Start the server:

```powershell
python -m uvicorn main:app --app-dir backend --reload
```

Open the endpoint or documentation in the browser. Stop the server with Ctrl+C when finished.

## 15. Day 1 review questions

Try answering these without looking above:

1. Why do we use a virtual environment?
2. How do FastAPI and Uvicorn differ?
3. What does `@app.get("/")` do?
4. What does `main:app` mean?
5. What is the difference between a Python dictionary and JSON?
6. How does staging differ from committing?
7. Why does `.gitignore` not automatically remove an already tracked file?

## 16. Completion checklist

- [x] Inspect the project folder and installed tools.
- [x] Initialize a local Git repository on `main`.
- [x] Create and activate a Python virtual environment.
- [x] Install FastAPI and Uvicorn.
- [x] Record installed dependencies in `requirements.txt`.
- [x] Create a GET / endpoint and see its JSON response in the browser.
- [x] Make the initial Git commit.
- [ ] Confirm that the Python cache cleanup is committed.
- [ ] Confirm a 200 response through `/docs`.

These checkboxes reflect confirmed progress when the notes were written. Update them after completing the remaining checks.

## 17. Terminology glossary

### Web and API concepts

| Term | Meaning | Example in our project |
|---|---|---|
| Application | A program that performs tasks for its users. | Our personal finance application will help users manage income and expenses. |
| Frontend | The part of an application users see and interact with. | Our future React pages will contain forms, buttons, and charts. |
| Backend | Code that handles requests, business rules, and access to stored data. | Our Python backend currently returns a welcome message. |
| Client | Software that sends a request to a server. | The browser was the client when we opened the endpoint. |
| Server | Software that listens for requests and sends responses; the word can also mean the computer running that software. | Uvicorn runs our local web server. |
| API (Application Programming Interface) | A defined way for one piece of software to interact with another. A web API exposes operations through HTTP requests and responses. | Our future React frontend can request transaction data from our FastAPI backend. |
| HTTP (Hypertext Transfer Protocol) | The rules clients and servers use to exchange web requests and responses. | The browser used HTTP to request our welcome message. |
| Request | A message a client sends asking a server to do something. It includes a method and a target, and may include headers and a body. | The browser sent a GET request for `/`. |
| Response | The server's reply to a request. It includes a status code and can include data in a body. | Our backend returned a JSON welcome message. |
| HTTP method | The part of a request that describes the kind of operation being requested. | GET retrieves information; POST commonly submits data to create something. |
| GET | An HTTP method used to retrieve information. A GET endpoint should not be designed to change application data. | `GET /` retrieves our welcome message. |
| Endpoint | An operation exposed by a web API, identified in our examples by an HTTP method and URL path. | `GET /` is our first endpoint. A future `GET /transactions` could list transactions. |
| GET endpoint | An endpoint that accepts GET requests to retrieve information. | `@app.get("/")` registers our GET endpoint. |
| Route | A mapping that connects a request's method and path to the code that handles it. | FastAPI maps `GET /` to `read_root()`. |
| URL (Uniform Resource Locator) | An address identifying a resource and how to reach it. | `http://127.0.0.1:8000/` is the URL we opened. |
| Path | The part of a URL that identifies a resource within the server. | `/` is our root path; `/docs` is the documentation path. |
| Root path | The path `/`, at the base of a website or API. It is different from the project root folder on disk. | Our welcome endpoint uses `/`. |
| Localhost / loopback address | A way to refer to the same computer that is making the request. `localhost` is a hostname; `127.0.0.1` is an IPv4 loopback address. | Opening `127.0.0.1` accesses a server on our own computer. |
| Port | A number that helps direct network traffic to a particular listening service on a computer. | Our development server listens on port `8000`. |
| Status code | A number in an HTTP response indicating its result. | `200` means OK; `404` means Not Found. |
| Response body | The content returned with a response, separate from its status code and headers. | `{"message": "Personal Finance API is running"}` is our response body. |
| JSON (JavaScript Object Notation) | A text format for exchanging structured data. It is used by many languages, not only JavaScript. | FastAPI sends our message as a JSON object. |
| Serialization | Converting data from a program into a format that can be sent or stored. | FastAPI converts our Python dictionary into a JSON response. |
| API documentation | A description of the operations an API provides and how to call them. | `/docs` lets us inspect and try our endpoint in a browser. |

### Python and backend tools

| Term | Meaning | Example in our project |
|---|---|---|
| FastAPI | A Python framework for building web APIs. A framework provides structure and reusable tools for common development tasks. | We use FastAPI to register routes and create responses. |
| Uvicorn | A web server that runs compatible Python web applications and handles network communication. | We start it with `python -m uvicorn`. |
| Interpreter | The program that executes Python code. | `backend\.venv\Scripts\python.exe` is our environment's interpreter. |
| Module | A unit of Python code that can be imported; a `.py` file can be a module. | `main.py` is imported as the module `main`. |
| Package | A way to organize and distribute reusable Python code. | We installed the `fastapi` package. |
| Dependency | A package or tool that other software needs to work. | FastAPI is one of our backend's dependencies. |
| pip | Python's package installer. | `python -m pip install fastapi uvicorn` installs packages. |
| Virtual environment | A project-specific Python environment with its own installed packages. It does not isolate the whole operating system like a virtual machine. | We created ours at `backend\.venv`. |
| Activation | Adjusting a terminal session so commands use the virtual environment's tools by default. | Running `Activate.ps1` makes `python` select our environment's interpreter. |
| requirements.txt | A conventional file listing Python packages to install, optionally with version constraints. | Our file records exact versions produced by `pip freeze`. |
| Import | Making code from another module or package available in the current file. | `from fastapi import FastAPI` makes the class available to us. |
| Class | A definition used to create objects with particular behavior and data. | `FastAPI` is a class. |
| Object / instance | A concrete value created from a class. | `FastAPI()` creates an application instance. |
| Variable | A name that refers to a value or object. | `app` refers to our FastAPI application object. |
| Function | A named block of code that runs when called and can return a result. | `read_root()` returns our welcome dictionary. |
| Parameter / argument | A parameter is a named input in a function definition; an argument is a value supplied when calling it. | `read_root()` has no declared parameters. In `app.get("/")`, `"/"` is an argument. |
| Decorator | Python syntax that applies another callable to a function or class when it is defined. Frameworks can use decorators to register behavior. | `@app.get("/")` registers the function below it as a route handler. |
| Route handler | The function called to handle a request matched to a route. | `read_root` handles GET requests to `/`. |
| Dictionary | A Python data structure containing key-value pairs. | `{"message": "Personal Finance API is running"}` contains one key-value pair. |
| String | A text value, written inside quotes in our examples. | `"message"` and `"Personal Finance API is running"` are strings. |
| Return | A statement that ends a function call and gives a value back to its caller. | `return {...}` gives our dictionary to FastAPI. |
| Indentation | Leading spaces that define blocks of Python code. | Four spaces place `return` inside `read_root`. |
| Bytecode cache | Generated files that help Python avoid recompiling unchanged imported source code. | `__pycache__/main.cpython-313.pyc` is generated from `main.py`. |
| Development server | A server run while developing and checking an application locally. | Our Uvicorn command starts the development server. |
| Reload | Restarting the application when watched source files change. | `--reload` lets us see saved code changes without manually restarting each time. |

### Terminal and command terminology

| Term | Meaning | Example in our project |
|---|---|---|
| Terminal | The interface where we enter commands and read their output. | VS Code's integrated terminal. |
| Shell | The program that interprets commands entered in a terminal. | We use PowerShell. |
| Current working directory | The folder from which a command runs. Relative paths are interpreted from this location. | Our commands usually run from the project root. |
| Project root | The top-level folder containing the project. | `C:\Users\shahz\Desktop\personal-finance-app`. |
| Relative path | A path expressed relative to the current location. | `backend\main.py` starts from our project root. |
| Absolute path | A complete filesystem path identifying a location. | `C:\Users\shahz\Desktop\personal-finance-app\backend\main.py`. |
| Command option / flag | An argument that changes a command's behavior. | `--reload` enables automatic reload in Uvicorn. |
| Pipe | The `|` operator, which passes output from one command to another. | We passed the output of `pip freeze` to `Out-File`. |
| UTF-8 | A character encoding used to represent text as bytes in a file. | We selected UTF-8 when saving `requirements.txt`. |

### Git terminology

| Term | Meaning | Example in our project |
|---|---|---|
| Version control | Recording changes over time so we can inspect history and recover earlier versions. | We use Git for version control. |
| Repository / repo | A project managed by Git, including its recorded history. | `git init` created our local repository. |
| Working tree | The checked-out project files we edit on disk. | Editing `main.py` changes our working tree. |
| Untracked file | A file Git has not added to its index yet. | A newly created study-notes file is initially untracked. |
| Tracked file | A file Git knows about through its index, commonly because it was staged or committed. | `main.py` became tracked after we added it. |
| Staging area / index | The prepared contents of the next commit. | `git add` places selected changes in the staging area. |
| Stage | Select file contents or changes for the next commit. | `git add .` stages eligible changes under the current directory. |
| Commit | A recorded snapshot of staged project content with metadata such as a message and author. | Our first commit saved the Day 1 backend setup. |
| Commit ID | The identifier Git assigns to a commit; a shortened form is often displayed. | `16ef1a4` identifies our initial commit in abbreviated form. |
| Branch | A named reference to a line of commits, allowing work to develop separately. | Our initial branch is named `main`. |
| Diff | A comparison showing changes between versions or states of files. | `git diff --cached --stat` summarizes changes staged for the next commit. |
| Clean working tree | Git reports no pending changes to commit. Ignored local files may still exist. | This does not prove that the committed code is correct. |
| .gitignore | A file of patterns telling Git which untracked files to ignore. | `.venv/` excludes the local Python environment. |
| --cached in git rm | Remove a path from Git's index while keeping the working copy on disk. | We use it to stop tracking `backend/__pycache__/`. |
| Remote | A named reference to another repository, often hosted online. | A future GitHub repository can be configured as a remote. |
| Push | Send local commits to a remote repository. | We have not needed to push to complete the local Day 1 setup. |

### Putting the terms together

For our first endpoint:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Personal Finance API is running"}
```

Read it as: "Create a FastAPI application. Register a GET endpoint at the root path. When a matching request arrives, call the route handler `read_root` and convert its returned dictionary into a JSON response."

An API can contain many endpoints. FastAPI is the framework we use to build the API, and Uvicorn is the server that runs it. The API is not the same thing as FastAPI, and an endpoint is not the entire API.

## References

- [FastAPI: First Steps](https://fastapi.tiangolo.com/tutorial/first-steps/)
- [FastAPI: Virtual Environments](https://fastapi.tiangolo.com/virtual-environments/)

