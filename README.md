# Magicweb

Magicweb is a simple web framework that is still under developement. It currently supports route parameters but no html templating.

## Usage
### Installation

To install Magicweb you can run
`pip install Magicweb` or `pip3 install Magicweb`

To install Magicweb from source run

```
git clone https://github.com/mordy-python/magicweb
cd magicweb
python setup.py install
```
### Run a basic app
To create a simple app we need to import Magicweb and create an app instance

```python
import magicweb
app = magicweb.App()
```
Once our app is instantiated we can add routes

```python
```python
import magicweb
app = magicweb.App()

@app.route('/')
def index(request, response):
  response.text = "Hello"
@app.route('/rendered')
def rendered(request, response):
  app.render('index.html')
```

We created two routes, one that returns hello world, and one that renders an html page. All html pages should be in a directory named html, although this can be overrdden when instantiting the App class.

To run our app we need to use the `app.run()` function

```python
...
app.run(app)
# to run with a different host/port just add those arguments
# app.run(app, host='0.0.0.0', port=5000)
```
