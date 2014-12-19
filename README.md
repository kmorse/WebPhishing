WebPhishing
===========
Using this tool, it is possible to recreate, change, or analyze date about web phishing.

For the purpose of web phishing analysis, this project is a series of scripts that is run on a database of valid phish in order to grab additional data, and put that data in a WARC.

This project provides the following scripts:

datadump.py: This file pulls data from phishtank and puts it into a database.

intoWARC.py: This file takes each url in the database and find the http response and reason, image number, and source code of that url. It then adds these values into the WARC.

in order to run these, initialize a database called test.db.

IMPORTANT: in order to run the files which call import warc, it is necessary to clone this repository: git clone git://github.com/anandology/warc.git

Put the files in WebPhishing under the warc folder that comes with that clone.
