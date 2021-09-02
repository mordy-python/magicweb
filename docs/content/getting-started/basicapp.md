---
title: "Create a basic app"
weight: 2
date: 2021-09-02T12:26:18-04:00
draft: false
---

Once we have Magicweb installed, we can create an app.

```python
from magicweb import App

app = App(__file__)
```

We need to put the `__file__` argument in the constructor so that Magicweb knows where to look for templates. Once we have an app, we can add routes.

```python
@app.route("/")
def index(request, response):
    response.text = "Hello World!"
```

We created a route that returns the text "Hello World!". It is important to note that the `request` and `response` arguments are required. The `request` argument is the request object that is passed to the route. The `response` argument is the response object that is returned by the route.

We can also create a route that returns a template. The templates are stored in the `templates` directory.

```python
@app.route("/template")
def template(request, response):
    app.render('template.html', response)
```

{{% notice note %}}
Find more about template rendering in the [Template Guide](/templates).
{{% /notice %}}

Once we have our routes, we can start the server.

```python
run(app)
```

We can also specify the host and port that the server run on with the keyword arguments `host` and `port`.

```python
run(app, host='0.0.0.0', port=8080)
```
