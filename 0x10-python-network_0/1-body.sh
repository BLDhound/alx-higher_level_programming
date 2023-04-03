#!/bin/bash
# sends GET reqeust to URL and display response body
curl -sfL "$1" -X GET
