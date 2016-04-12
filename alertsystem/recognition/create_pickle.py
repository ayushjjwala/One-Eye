#!/usr/bin/env python

import sys
import os.path
import pickle

if __name__=="__main__":
    if len(sys.argv) !=2:
        print "usage:"
        sys.exit(1)

    pickle_file = open('mug.pck', 'w')
    BASE_PATH = sys.argv[1]

    label = 0
    for dirname, dirnames, filenames in os.walk(BASE_PATH):
        for subdirname in dirnames:
            subject_path = os.path.join(dirname, subdirname)
            for filename in os.listdir(subject_path):
                abs_path = "%s/%s" %(subject_path, filename)
                pickle.dump([abs_path,label], pickle_file)
            label = label + 1

    pickle_file.close()


