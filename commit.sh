#!/bin/bash
if [ -z "$(git status | grep nothing)" ]
then
	echo "Commit files first"
	exit 1
fi
python make.py
git checkout gh-pages
cp -r target/* .
git add --all
git commit -m "Auto-commit to gh-pages" --author="Auto Script <null@null.com>"
git push origin
git checkout master
