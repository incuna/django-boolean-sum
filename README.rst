Django Boolean Sum
==================

This is a small Django utility module to allow you to correctly annotate or
aggregate based on the sum of a Boolean field. This answers the question "how
many objects do I have related to this object *where foo is True*.

Usage
-----

Usage is pretty simple::

    from django_boolean_sum import BooleanSum

    MyModel.objects.annotate(priority_related_count=BooleanSum('related__priority'))

This will return instances of ``MyModel`` with a ``related_count`` attribute, which
is the number of related instances which have ``priority=True``.

Installation
------------

From PyPI::

    $ pip install django-boolean-sum

Caveats
-------

This has been tested solely on PostgreSQL and Sqlite, using Django 1.4. It also
depends on internal Django components which are not documented, and therefore
are subject to possible breaking changes in future versions.

It is very naive about multi-databases, assuming that the query is being made
for the backend of the ``default`` database.

Contributing
------------

Pull Request it.
