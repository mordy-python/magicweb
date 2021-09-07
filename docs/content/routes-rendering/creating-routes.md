---
title: "Creating Routes"
date: 2021-09-03T11:46:42-04:00
draft: false
weight: 1
---

Lets start by creating the same basic app as before.

```python
from magicweb import Magicweb, run

app = Magicweb(__file__)
```

Now we can create a route.

A route is composed of a decorator and a function.
The decorator is used to define the route's path and the function is used to define the route's behavior.

```python
...
@app.route("/")
def index(request, response):
    response.text = "Hello World!"
```

What this does is it defines the route's path as `/` and when the route is called, it will call the function `index`. The function will receive the request and response objects as arguments and it will return "Hello World" in the reponse.

{{< panel title="Note" style="info" >}}
All functions MUST accept at least two arguments: the `request` and the `response`.
{{< /panel >}}

### Routes with parameters

Magicweb supports routes with parameters. The syntax is the same as before, but now the path is defined as `/hello/{name}`. And the function will receive the `name` parameter as an argument.

```python
...
@app.route("/hello/{name}")
def hello(request, response, name):
    response.text = f"Hello {name}"
```
