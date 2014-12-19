import warc
import httplib
import urllib2
import sqlite3 as lite
import sys
import csv

con = None
h = warc.WARCHeader({
                        "WARC-Type" : "response"
                    }, defaults=True)
try:
    con = lite.connect('test.db')
    con.text_factory = str
    cur = con.cursor()
    cur.execute('SELECT SQLITE_VERSION()')
    data = cur.fetchone()
    print "SQLite version: %s" % data
except lite.Error, e:
    print "Error %s:" % e.args[0]
    sys.exit(1)


#for row in cur.execute("SELECT url from phish_valid"):
cur.execute("SELECT url,phish from phish_valid")
for c in cur.fetchall():
    print c[0]
    urls = str(c[0])
    id = c[1]
    print c[1]

    try:
        response3 = urllib2.urlopen(urls)
        page_source = response3.read()
        print page_source
        res = httplib.HTTPConnection("www.google.com")
        res.request("GET", "")
        r1 = res.getresponse()
        s = "Response_Status: "+str(r1.status) + " Response_Reason: "+str(r1.reason) + " Image: "+ str(id) +".png" + " Source_Code: " + page_source
        record = warc.WARCRecord(h, s)
        f = warc.open("crlf_at_1k_boundary.warc.gz", "w")
        f.write_record(record)
        f.close()
        print record
    except urllib2.HTTPError, err:
        if err.code == 404:
            print "Page not found!"
        elif err.code == 403:
            print "Access denied!"
        else:
            print "Something happened! Error code", err.code
    except urllib2.URLError, err:
        print "Some other error happened:", err.reason
        #page_source = response3.read()

h = warc.WARCHeader({
    "WARC-Type" : "response"
}, defaults=True)