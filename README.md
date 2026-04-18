# Flask Front-end Template

## Folder structure:

    ├───.vscode
    ├───app
    │   ├───forms
    │   ├───static
    │   │   └───uploads
    │   ├───templates
    │   │   ├───admin
    │   │   ├───auth
    │   │   └───components
    │   ├───utils
    │   ├───views
    │   └───
    ├───logs
    ├───tests
    │   └───
    ├───venv
    ├───.env
    ├───.flaskenv
    ├───.gitignore
    ├───requirements.txt
    ├───README.md
    ├───config.py
    ├───run.py / wsgi.py

## Define your environment:

    $ pip install virtualenv
    $ virtualenv venv
    $ source venv/Scripts/activate

## Install it:

    (venv) $ pip install -r requirements-dev.txt
    (venv) $ pip freeze

## Define environment variables:

    (venv) $ touch .env
        API_PATH = ""
        SECRET_KEY = ""

## Run it:

    (venv) $ flask run --reload --with-threads

## Parepare your Editor:

Git Extensions:
<br>
https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens

https://marketplace.visualstudio.com/items?itemName=donjayamanne.githistory

https://marketplace.visualstudio.com/items?itemName=mhutchie.git-graph

<br>
Python Extensions:
<br>

https://marketplace.visualstudio.com/items?itemName=ms-python.python

https://marketplace.visualstudio.com/items?itemName=LittleFoxTeam.vscode-python-test-adapter

https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring

https://marketplace.visualstudio.com/items?itemName=mgesbert.python-path

<br>
Flask Extensions:
<br>

https://marketplace.visualstudio.com/items?itemName=cstrap.flask-snippets

https://marketplace.visualstudio.com/items?itemName=wholroyd.jinja

https://marketplace.visualstudio.com/items?itemName=samuelcolvin.jinjahtml

<br>
Linters Extensions:
<br>

https://marketplace.visualstudio.com/items?itemName=usernamehw.errorlens

https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker-spanish

<br>
HTML Templates Extensions:
<br>

https://marketplace.visualstudio.com/items?itemName=formulahendry.auto-close-tag

https://marketplace.visualstudio.com/items?itemName=formulahendry.auto-rename-tag

https://marketplace.visualstudio.com/items?itemName=vincaslt.highlight-matching-tag

<br>
Extras:
<br>

https://marketplace.visualstudio.com/items?itemName=vscode-icons-team.vscode-icons

https://marketplace.visualstudio.com/items?itemName=TabNine.tabnine-vscode

https://marketplace.visualstudio.com/items?itemName=Gruntfuggly.todo-tree

https://marketplace.visualstudio.com/items?itemName=mikestead.dotenv

https://marketplace.visualstudio.com/items?itemName=CoenraadS.bracket-pair-colorizer


<br>

## DocString template 

For Python Docstring Generator VSCode extension

Function

    '''
    [Summary].

    :param   [name]<type>:  [description].

    :returns [name]<type>:  [description].
    '''

Class

    '''
    [Summary].
    '''

## That's it!!
