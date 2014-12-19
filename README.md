Using this tool, it is possible to recreate, change, or analyze data about web phishing.

For the purpose of web phishing analysis, this project is a series of scripts that is run on a database of valid phish in order to grab additional data, and put that data in a WARC.

This project provides the following scripts:

datadump.py: This file pulls data from phishtank and puts it into a database.

intoWARC.py: This file takes each url in the database and find the http response and reason, image number, and source code of that url. It then adds these values into the WARC.

process2.py is a file that takes the downloaded database and goes through each entry, takes a screenshot and shows the response.

in order to run these, initialize a database called test.db.

IMPORTANT: in order to run the files which call import warc, it is necessary to clone this repository: git clone git://github.com/anandology/warc.git

Put the files in WebPhishing under the warc folder that comes with that clone.

Be careful when running these scripts. Because you are opening urls to phishing sites, your computer may be at risk. Try using a Virtual Box for development instead.

In order to pull the data hourly, run a cron job on this script and give the job one hour time limit.

For click through analysis, a script was modified for each of 50 PayPal-like sites and then process2.py was run on them and also a modification of intoWARC that grabbed a photo so that I could analyze results. Click through does not have a script that works for every phish, so it is necessary in next steps to create an automated click through. Not just automatic script analysis by manually inputting each url.
