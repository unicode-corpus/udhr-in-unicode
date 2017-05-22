#!/usr/bin/env python

import sys;
import os.path;

BASE_URL = 'http://unicode.org/udhr/assemblies/'

SOURCE_FILES = {
    'charcount': 'udhr_charcount.zip',
    'html': 'udhr_html.zip',
    'txt': 'udhr_txt.zip',
    'xml': 'udhr_xml.zip',
}

ROOT_DIR = os.path.join(os.path.dirname(__file__), '..')
DATA_DIR = os.path.join(ROOT_DIR, 'data')
DOWNLOAD_DIR = os.path.join(ROOT_DIR, '_download')


def error(message, exit_code = 1):
    sys.stderr.write("%s\n" % message)
    exit(exit_code)

def report(message):
    sys.stdout.write("%s\n" % message)


def fetch(zip_filename):
    dst = os.path.join(DOWNLOAD_DIR, zip_filename)
    if not os.path.exists(dst):
        report("downloading %s..." % zip_filename)
        os.system("curl '%s/%s' -o '%s'" % (BASE_URL, zip_filename, dst))
    else:
        report("found %s." % zip_filename)
    if not os.path.exists(dst):
        error("failed to fetch %s" % zip_filename)

def unzip(zip_filename, dst_dirname):
    src = os.path.join(DOWNLOAD_DIR, zip_filename)
    dst = os.path.join(DATA_DIR, dst_dirname)
    os.system("unzip -u '%s' -d '%s'" % (src, dst))
    if not os.path.exists(dst):
        error("failed to unzip %s" % zip_filename)


def main():
    if not os.path.exists(DOWNLOAD_DIR):
        os.mkdir(DOWNLOAD_DIR)
    if not os.path.exists(DATA_DIR):
        os.mkdir(DATA_DIR)

    for type, filename in SOURCE_FILES.items():
        fetch(filename)
        unzip(filename, type)

if __name__ == '__main__':
    main()
