---
title: "Render Variables in HTML"
date: 2021-09-03T13:09:39-04:00
weight: 3
draft: false
---

Now that we have our variables passed to the template, we can render them in the template.

Lets create `templates/index.html` and add the following code:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Magicweb</title>
</head>
<body>
    <h1>Hello {{ name }}</h1>
    <h3>The answer to Life, the Universe, and Everything {{ the_answer }}</h3>
</body>
</html>
```

For the most part, it's a normal html document. We can use the variables we created in the template by using the `{{ }}` syntax and placing th variable name inside the braces.

You can also use `{% %}` tags to do more complex things, such as if statements, and loops.

## With an if statement

Lets add an if statement to our template, if no name is passed, we will use the default name.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Magicweb</title>
</head>
<body>
    {% if name %}
        <h1>Hello {{ name }}</h1>
    {% else %}
        <h1>Hello World</h1>
    {% endif %}
    <h3>The answer to Life, the Universe, and Everything {{ the_answer }}</h3>
</body>
</html>
```

Don't forget to use the `{% endif %}` tag to close the if statement.

## With a loop

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Magicweb</title>
</head>
<body>
    <h1>Hello {{ name }}</h1>
    <h3>The answer to Life, the Universe, and Everything {{ the_answer }}</h3>
    {% for item in items %}
        <p>{{ item }}</p>
    {% endfor %}
</body>
</html>
```

Assuming we passed a list of items to the template, we can loop through them and render them in the template.
