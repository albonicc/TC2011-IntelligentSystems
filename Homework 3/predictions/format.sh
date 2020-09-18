#!/bin/bash

cat $1 | tr "," ":" | cut -d: -f1,5 | tr ":" "," > output.csv
