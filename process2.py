__author__ = 'kris'
#!/usr/bin/env python

import sys
import warc
import logging as log
import json

# https://github.com/mistermarco/screencapture
# selenium is not headless

#import urllib

import cPickle as pickle
import os.path
import bz2
import subprocess

import signal

def handler(signum, frame):
    log.info("Ctrl-C detected, dumping pickled processed file and \
      exiting")
    with open(dbfilename, 'wb') as g:
        pickle.dump(processed, g)
    sys.exit(0)

if __name__ == "__main__":

    log.basicConfig(stream=sys.stderr, level=log.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

    # TODO make these command line arguments
    # online-valid is a full dump of the DB in JSON fromat from phishtank
    #filename   = "/Users/developer/Desktop/phish/phishtank/online-valid.json.1410855057.bz2"
    #filename = "http://data.phishtank.com/data/7c5d7fe2f72e02528e13f8701439a271f9f77ea438a917e4f80335b468f6ea70/online-valid.json.bz2"
    # test file
    #filename   = "/Users/developer/Desktop/phish/phishtank/online-valid.2.json"
    #dbfilename = "/Users/developer/Desktop/phish/phishtank/phish_ids.db"
    #dbfilename = "/Users/developer/Desktop/phish/phishtank/previously_done.db"
    filename = "/Users/kris/Desktop/phish/verified_online.json.bz2"
    dbfilename = "/Users/kris/Desktop/phish/database.db"

    # check if bz2, then load initial file.
    if os.path.splitext(filename)[1] == ".bz2":
        with bz2.BZ2File(filename, 'rb') as f:
            data = json.load(f)
    else:
        with open(filename, 'r') as f:
            data = json.load(f)

    # load a pickled set of processed phish_ids
    if os.path.isfile(dbfilename):
        with open(dbfilename, 'rb') as g:
            processed = pickle.load(g)
            # TODO need to check on EOFError or some exception
        # make sure they're all ints
        processed = set([int(p) for p in processed])
    else:
        processed = set()

    signal.signal(signal.SIGINT, handler)



    # process each entry in the json file
    for entry in data:
        log.debug("valid keys: %s" % entry.keys())

        # assuming valid format
        phish_id = entry["phish_id"]
        with open("test.txt", "a") as myfile:
            url = entry["url"]
            target = entry["target"]
            s = "url :"+ str(url)
            s.encode('utf-8')
            myfile.write("things")


    log.info("processed: %s" % processed)

    with open(dbfilename, 'wb') as g:
        pickle.dump(processed, g)
