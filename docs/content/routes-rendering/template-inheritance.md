---
title: "Template Inheritance"
date: 2021-09-05T13:18:38-04:00
weight: 4
draft: false
---

In the previous section, we saw how we can render a template with variables and even use loops, and if statements.
One thing that makes templating more powerful is the ability to inherit from other templates. This is done by using the `{% extends 'base.html' %}` tag. This tag tells the template engine to use the template `base.html` as a base template, and then render the current template with the variables and loops from the base template.

Lets see an example:

__base.html__

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}{% endblock %}</title>
</head>
<body>
    {% block content %}{% endblock %}
</body>
</html>
```

You can see that instead of defining the title, and the content, we have defined a block called `title` and `content`. In a temaplate like `index.html` we can now use the `{% block title %}` and `{% block content %}` tags to define the title and the content.

__index.html__

```html
{% extends 'base.html' %}
{% block title %}My Blog{% endblock %}
{% block content %}
    <h1>My Blog</h1>
    <ul>
        {% for post in posts %}
        <li>
            <a href="/blog/{{ post.id }}">{{ post.title }}</a>
        </li>
        {% endfor %}
    </ul>
{% endblock %}
```

This didn't look like much, but it's actually quite powerful, if we had a bootstrap nabar, we just saved ourselves a lot of work. We can now use the `{% block title %}` and `{% block content %}` tags to define the title and the content. We can also use the `{% for post in posts %}` tag to loop over all the posts and render them.
