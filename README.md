# My API

This is a simple Python API built with Flask.

## Setup

1. Make sure you have Python 3 installed. You can check this by running `python --version` or `python3 --version` in your terminal.

2. Install pip, which is a package manager for Python. You can do this by running `sudo apt install python3-pip` on Ubuntu, or `sudo easy_install pip` on MacOS.

3. Clone this repository and navigate into the project directory:

```bash
git clone git@github.com:esnf619-fall-2023/text2p-ml-py-api.git
cd myapi
```

4. Create a virtual environment and activate it:

```bash
python3 -m venv venv
source venv/bin/activate
```

5. Install the project's dependencies:

```bash
pip install -r requirements.txt
```

## Running the API

1. Set the `FLASK_APP` environment variable to your application:

```bash
export FLASK_APP=ml
```

2. Run the Flask application:

```bash
flask run
```

The API will be served at `http://127.0.0.1:5000`.

## Routes

- `/`: Returns a welcome message.
- `/api/data`: Returns some data.
