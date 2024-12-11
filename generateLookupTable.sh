#!/bin/bash

{ echo "path, size"; ls /datasets/**/* -l | awk -F' ' '{ print $9","$5}'; } > fileLookup.csv

{ 
  echo "{";
  ls /datasets/**/* -l | awk -F' ' '{ print "\"" $9 "\": " $5 ","}';
  echo "\"fin\":123";
  echo "}";
} > fileLookup.json
