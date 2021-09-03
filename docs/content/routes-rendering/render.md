---
title: "Render a Template"
date: 2021-09-03T12:27:54-04:00
weight: 2
draft: false
---

To render a template, you can use the `render` method of your app instance. Lets create a basic application and render a template.

```python
from magicweb import App, run

app = App(__file__)

@app.route('/')
def index(request, response):
    app.render('index.html', name='MagicWeb', the_answer=42)
    # app.render('index.html', {'name': 'MagicWeb', the_answer: 42})
    # You can also use a dictionary to pass variables to the template.
run(app)
```

Whats happening here?

* The `render` method is called on the app instance with the arguments `template_name` and `**kwargs`.
* The `template_name` argument is the name of the template to render.
* The `**kwargs` argument is either:
  * Keyword arguments, which are passed to the template as variables.
  * A dictionary of values to be passed to the template.

Magicweb looks for templates in the default location: `templates/` or the template location specified by you.
