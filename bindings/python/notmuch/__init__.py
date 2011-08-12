"""The :mod:`notmuch` module provides most of the functionality that a user is
likely to need.

.. note:: The underlying notmuch library is build on a hierarchical
    memory allocator called talloc. All objects derive from a
    top-level :class:`Database` object.

    This means that as soon as an object is deleted, all underlying
    derived objects such as Queries, Messages, Message, and Tags will
    be freed by the underlying library as well. Accessing these
    objects will then lead to segfaults and other unexpected behavior.

    We implement reference counting, so that parent objects can be
    automatically freed when they are not needed anymore. For
    example::

            db = Database('path',create=True)
            msgs = Query(db,'from:myself').search_messages()

    This returns a :class:`Messages` which internally contains a
    reference to its parent :class:`Query` object. Otherwise the
    Query() would be immediately freed, taking our *msgs* down with
    it.

    In this case, the above Query() object will be automatically freed
    whenever we delete all derived objects, ie in our case:
    `del(msgs)` would also delete the parent Query. It would not
    delete the parent Database() though, as that is still referenced
    from the variable *db* in which it is stored.

    Pretty much the same is valid for all other objects in the
    hierarchy, such as :class:`Query`, :class:`Messages`,
    :class:`Message`, and :class:`Tags`.

"""

"""
This file is part of notmuch.

Notmuch is free software: you can redistribute it and/or modify it
under the terms of the GNU General Public License as published by the
Free Software Foundation, either version 3 of the License, or (at your
option) any later version.

Notmuch is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
for more details.

You should have received a copy of the GNU General Public License
along with notmuch.  If not, see <http://www.gnu.org/licenses/>.

Copyright 2010 Sebastian Spaeth <Sebastian@SSpaeth.de>'
"""
from notmuch.database import Database, Query
from notmuch.message import Messages, Message
from notmuch.thread import Threads, Thread
from notmuch.tag import Tags
from notmuch.globals import nmlib, STATUS, NotmuchError
__LICENSE__ = "GPL v3+"
__VERSION__ = '0.6'
__AUTHOR__ = 'Sebastian Spaeth <Sebastian@SSpaeth.de>'
