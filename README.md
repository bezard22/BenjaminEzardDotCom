# BenjaminEzardDotCom
Source code for BenjaminEzard.com

The site serves as a personal portfolio for projects as well as a host for informational or utility applications. The site is currently built in Django. Each article/application/project on the site (stored in the articles directory) has its own github repository and exists as a submodule in this project.

The site is currently a work in progress and has not yet been published.

---

## Structure

```
├── BenjaminEzardDotCom
│   ├── articles
│   │   └── <article>
│   │   │   |── static
│   │   │   │   │── index.html
│   │   │   │   │── index.js
│   │   │   │   └── style.css
│   │   │   │── src
│   │   │   └── README.md
|   ├── BenjaminEzardDotCom
|   |   ├── __init__.py
|   |   ├── asgi.py
|   |   ├── urls.py
|   |   └── wsgi.py
|   ├── portfolio
|   |   ├── static/portfolio
|   |   |   └── style.css
|   |   ├── templates/portfolio
|   |   |   ├── article.html
|   |   |   ├── footer.html
|   |   |   ├── header.html
|   |   |   └── index.html
|   |   |── __init__.py
|   |   |── admin.py
|   |   |── apps.py
|   |   |── models.py
|   |   |── tests.py
|   |   |── urls.py
|   |   └── views.py
├── manage.py
└── README.md
```
| Directory/File | Description |
| --- | --- |
| /articles | Directory containing article static files and src files for implementation. Each subdirectory is a its own repo and exists as a submodule in this project |
| /articles/\<article\> | Subdirectory for article |
| /articles/\<article\>/static | static files (html, css, js, assets) for article |
| /articles/\<article\>/static/index.html | html file for article |
| /articles/\<article\>/static/index.js | script file for article |
| /articles/\<article\>/static/style.css | stylesheet file for article |
| /articles/\<article\>/src | implementation of topic discussed in article |
| /articles/\<article\>/README | README for article |
| /BenjaminEzardDotCom | django directory for site (settings.py file excluded for security) |
| /portfolio | main django application hosted on site, serving article pages |
| /static/portfolio/style.css | main stylesheet for site |
| /templates/portfolio | portfolio templates directory | 
| /templates/portfolio/article.html | html article template |
| /templates/portfolio/footer.html | html template for footer across site |
| /templates/portfolio/header.html | html template for header across site |
| /templates/portfolio/index.html | html template for home page |

Site database excluded for security