---
title: "Creating a Magicweb application"
date: 2021-09-03T11:57:09-04:00
weight: 2
pre: "<b>2. </b>"
---

### Create a virtualenv and install Magicweb

Before installing, create a python vitual environment with the following command: `python -m venv venv`.

Activate the virtual environment with `source venv/bin/activate` on Mac and Linux, or `venv\Scripts\activate` on Windows.

Now let's install the magicweb package with the following command: `pip install magicweb` (See [here](getting-started/installation) for more details).

### Create a new Magicweb application

Now lets import App from magicweb and create a new application.

```python
from magicweb import App
app = App(__file__)
```

What we did here is create a new App object. The first argument is the path to the current file. This is used to find the templates and static files.

`App` also has an optional `template_folder` argument. If you want to use a different template folder, you can set it here. By default, it is set to `templates`.

```python
...
app = App(__file__, template_folder='templates2')
```

### Run the application

To run the application, we need to call the `run` method and supply the app name as a parameter.

```python
...
app.run(app)
```

{{< panel title="Note" style="info" >}}
We have not created any routes yet, so the application will not do anything.
{{< /panel >}}
