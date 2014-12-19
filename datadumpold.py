import sqlite3 as lite
import sys
import csv
import urllib2
url = "http://data.phishtank.com/data/7c5d7fe2f72e02528e13f8701439a271f9f77ea438a917e4f80335b468f6ea70/online-valid.csv"
response = urllib2.urlopen(url)
cr = csv.reader(response)
con = None

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

with open('verified_online.csv','rb') as fin:
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['phish_id'], i['url'],i['phish_detail_url'], i['submission_time'],i['verified'],i['verification_time'],i['online'], i['target']) for i in dr]

cur.executemany("INSERT INTO phish_valid (phish, url, phish_detail, stime, verified, vtime, online, target) VALUES (?, ?, ?, ?, ?,?, ?,?);", to_db)
con.commit()
con.close()