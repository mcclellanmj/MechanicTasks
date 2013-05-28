#!/bin/bash
python make.py
git checkout gh-pages
cp -r target/* .
