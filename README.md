# Backend with Flask

This is a backend application built with Flask with some of the typical
situations encountered during the development.

https://www.youtube.com/playlist?list=PLab_if3UBk98jBTmyxShFVirMbgfFYu8W

## Chapter 1

In this first video, I've created a Flask project, I've added the necessary
dependencies and structured the folders.

For this, I've used the Poetry to create the project and add the dependencies.
Then, I've created some simple endpoints to test my application.

To structure the endpoints, I've also used the Blueprints.


## Chapter 2

In this second video, I show different methods to authenticate a request into
a Flask application.

I start using a Basic Authentication and then JWT. Both authentication are
validated with the library flask-httpauth using decorators.

To protect endpoints with any kind of authentication, I only need to add the
adequate decorator to the endpoint signature.


## Chapter 3

In this third video, I will configure the database connection with SQLAlchemy.
Flask and SQLAlchemy work very well together. The database connection can direclty
be injected in the Flask application and SQLAlchemy will read it.

I will also create some entities to show the most common relationships: one-to-one,
one-to-many, many-to-one and many-to-many.

Here is the command I've used to create the database in the video:
```
docker run -d -e POSTGRES_HOST_AUTH_METHOD=trust -e POSTGRES_USER=sergio -e POSTGRES_PASSWORD=my-password -e POSTGRES_DB=backenddb -p 5432:5432 postgres:13
```


## Chapter 4

In this fourth video, I show how to use Marshmallow to serialize and deserialize
JSON document to and from objects. I will also show how to use Marshmallow to
validate JSON documents.

With Marshmallow, I must create to be used against JSON documents. Those schemas
define the rules for each field, required or not, type and some custom
validation rules.

I also have a Marshmallow / SQLAlchemy dependency which allows me to create the
schemas directly from the SQLAlchemy models.


## Chapter 5

In this fifth video, I've added the unit tests unit Pytest. I've used the parametrized
tests to run a single test with multiple inputs. I've also created some tests
using two different ways of mock. If also created a conftest file with the initialization
of the application, the database and the data.

Here is the command I've used to create the database in the video:
```
docker run -d -e POSTGRES_HOST_AUTH_METHOD=trust -e POSTGRES_USER=sergio -e POSTGRES_PASSWORD=my-password -e POSTGRES_DB=backenddb -p 5432:5432 postgres:13
```


## Chapter 6

In this video, I've configured pre-commit and added 4 tools to be run at each commit: isort, 
black, mypy and flake8.

isort will organize the imports. It will group them by line. It will also group the import of 
the current project in a separated block, leaving the installed dependencies in another block.
When the line is too long, it will split it.

Black is a tool which will format the code upon the rules of PEP8. Using double quotes for
strings, no space before a colon and space after a colon. And a lot more rules.

Mypy is a type checker. It will check if the variables are used expecting the same type as
they were created.

Flake8 is a code style checker. It will just check what was done after all the previous tools
modified the code.

All of those tools can be configured into the pyproject.toml except for flake8.


## Chapter 7

In this video, I show the usage of Jinja to generate HTML templating to create an HTML file
used for emails. I will use several blocks of Jinja. I start showing how to return a Jinja
template from a Flask application. I will inject some variables inside the Jinja template
while returning it from the controller.

Inside the Jinja template, I show the usage of the for-loops, the blocks for modularity, the
includes for inheritance and the macros for code reusability.

