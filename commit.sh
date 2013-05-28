#!/bin/bash
python make.py
git checkout gh-pages
cp -r target/* .
git add --all
git commit -m "Auto-commit to gh-pages"
git push origin
git checkout master
