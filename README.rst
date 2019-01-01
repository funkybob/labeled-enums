labeled-enums
=============

A Django-friendly iterable Enum type with labels.

Example
-------

.. code-block:: python

    >>> from lenum import LabeledEnum
    >>> class STATE_CHOICES(LabeledEnum):
    ...     NEW = 0
    ...     IN_PROGRESS = 1
    ...     REVIEW = 2, 'In Review'
    ...
    >>>
    >>> STATE_CHOICES.NEW
    0
    >>> STATE_CHOICES.IN_PROGRESS
    1
    >>> STATE_CHOICES[2]
    'In Review'
    >>> list(STATE_CHOICES)
    [(0, 'New'), (1, 'In Progress'), (2, 'In Review')]

    >>> STATE_CHOICES.for_label('In Progress')
    1
    ```

    >>> STATE_CHOICES.names
    ('NEW', 'IN_PROGRESS', 'REVIEW')

Usage in Django:

.. code-block:: python

    class STATUS(LabeledEnum):
        CLOSED = 0
        NEW = 1
        PENDING = 2, 'Process Pending'
        FAILED = -1, 'Processing Failed'

    class MyModel(models.Model):
        # django migrations can have trouble resolving imports if we define the
        # class within the class, so we bind this here for convenience.
        STATUS = STATUS

        status = models.IntegerField(choices=STATUS, default=STATUS.NEW)

Installation
------------

.. code-block::

    pip install labeled-enum
