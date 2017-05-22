#!/usr/bin/env bash
set -e

UPSTREAM_BRANCH='unicode.org'

git checkout $UPSTREAM_BRANCH
rm -rf _download/
./tools/download_and_unzip.py
git add data/
git commit -m 'Update data from unicode.org/udhr'
git checkout master
git merge --no-ff --no-edit $UPSTREAM_BRANCH
