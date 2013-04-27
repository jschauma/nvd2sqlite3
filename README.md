NIST Vulnerability Database to Sqlite3
======================================
Many organizations have a need to map public CVEs to internal tickets,
packages, or otherwise keep track of the known vulnerabilities.  For this,
it is useful to have a local database to process CVEs easily in bulk.

The 'nvd2sqlite3' utility will populate and sync NIST's Vulnerability
Database into a local sqlite3 database for this purpose.

FAQ
===

What are the dependencies?
--------------------------
'nvd2sqlite3' is written in python, using only modules included in the
base distribution.  In particular, it uses the 'xml.etree.ElementTree'
module for XML parsing and the 'sqlite3' module to populate the local
database.

python < 2.6 probably isn't going to be sufficient, though.

How do I install 'nvd2sqlite3'?
-------------------------------
'nvd2sqlite3' comes with a standard python 'setup.py' file, so you should
be able to just run 'python setup.py install'.

How do I use it?
----------------
Simply run:

    curl https://nvd.nist.gov/static/feeds/xml/cve/nvdcve-2.0-recent.xml | \
            nvd2sqlite3 -d /wherever/you/like/to/keep/the/dbfile

By default, 'nvd2sqlite3' will use '/var/db/cvedb' as the database file,
so make sure that the user invoking the command has write access to that
file.

Please see the manual page for details.

Who wrote this tool?
--------------------
'nvd2sqlite3' was originally written by Jan Schaumann
(jschauma@netmeister.org) in April 2013.
