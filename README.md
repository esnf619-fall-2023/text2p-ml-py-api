# My API

This is a simple Python API built with Flask.

## Setup

1. Make sure you have Python 3 installed. You can check this by running `python --version` or `python3 --version` in your terminal.

2. Install pip, which is a package manager for Python. You can do this by running `sudo apt install python3-pip` on Ubuntu, or `sudo easy_install pip` on MacOS.

3. Clone this repository and navigate into the project directory:

```bash
git clone git@github.com:esnf619-fall-2023/text2p-ml-py-api.git
cd text2p-ml-py-api
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

## Deployment

This guide assumes that you have SSH access to an Ubuntu server.

1. SSH into your Ubuntu server.

2. Update the package lists for upgrades and new package installations:

```bash
sudo apt-get update
```

3. Install Python, pip, and venv:
```bash
sudo apt-get install python3 python3-pip python3-venv
```
4. Clone your repository and navigate into the project directory:
```bash
git clone git@github.com:esnf619-fall-2023/text2p-ml-py-api.git
cd text2p-ml-py-api
```
5. Create a virtual environment and activate it:
```bash
python3 -m venv venv
source venv/bin/activate
```
6. Install your project's dependencies:
```bash
pip install -r requirements.txt
```

7. Install Gunicorn:

```bash
pip install gunicorn
```

8. Test your application with Gunicorn:
```bash
gunicorn -w 4 -b 0.0.0.0:5000 "ml:create_app()"
```
If everything is working correctly, press CTRL+C to stop Gunicorn.

9. Install `screen`:
```bash
sudo apt-get install screen
```
10. Start a new screen session:
```bash
screen -S ml
```
11. Run your application with Gunicorn:
```bash
gunicorn -w 4 -b 0.0.0.0:5000 "ml:create_app()"
```
12. Press `CTRL+A` and then `D` to detach from the screen session.
