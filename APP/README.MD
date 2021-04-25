
## Domain Modeling

![image](https://user-images.githubusercontent.com/66631333/116009168-aafd1400-a5dd-11eb-8d61-fd7db6f58954.png)


### Running tests with Pytest

Perhaps because the book's focus is on architecture, and because [the authors offer the book for free](https://www.cosmicpython.com/book/preface.html), the book doesn't discuss much detail about actually running the tests beyond a few assumptions:

* You are using Docker containers (I'd rather not)
* You are using a virtual environment (Yes, we are) and will run the tests manually (Yes, we will)

Or, it is assumed that you have read Harry Percival's first book, [which is also free](https://www.obeythetestinggoat.com/pages/book.html#toc), and focuses more on the mechanics of testing.

Regardless, you'll want to ensure that you include [`pytest`](https://pypi.org/project/pytest/) in your virtual environment.

Then, test dicsovery is [pretty automagic](https://docs.pytest.org/en/stable/contents.html), and essentially requires that you run:

`python -m pytest` 

in your project directory.  Of course, [there's much more to using pytest](https://docs.pytest.org/en/stable/contents.html), but that is a good basic start.

Key files at this stage:

* tests for allocate and batches
* domain model classes/functions

##  Repository Pattern

This chapter introduces the use of SQLAlchemy and the basics of a [Repository Pattern](https://codewithshadman.com/repository-pattern-csharp/) using Python.

Things to install:
* [sqlalchemy](https://docs.sqlalchemy.org/en/13/): `pip install sqlalchemy`

In this chapter, these modules provide a persistence mechanic and an abstraction layer in the form of an [O/RM](https://en.wikipedia.org/wiki/Object%E2%80%93relational_mapping):
* orm
* repository

### Test Orientation

Everything is tested, so there are two new test modules:
* test_orm
* test_repository

#  Refactor

By the end of the book, the code reflects the following diagram:

![image](https://user-images.githubusercontent.com/66631333/116009250-08916080-a5de-11eb-9de1-792564ee0a97.png)

This involves a transition towards the following:

* a full set of tests:
    * end-to-end (e2e)
    * integration 
    * unit
* Domain Layer
    * entities and models
    * aggregates
    * events
    * commands
* Service Layer
    * Event and Command Handlers
    * Unit Of Work
    * internal message bus
* Adapters (concrete implementations of interfaces/ABCs)
    * Repository (for CRUD)
    * Event Publisher
* API
    * Entry Points (Flask)
    * Event consumer
    * External Message Bus (Redis)

