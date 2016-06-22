#!/bin/sh
cd "$(dirname "$0")"/apache-solr-3.5.0/example
nohup java -jar start.jar &
