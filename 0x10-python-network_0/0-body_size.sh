#!/bin/bash

# Get the URL from the command line argument
url=$1

# Use curl to send a request to the URL and store the response body in a variable
response=$(curl -s $url)

# Get the size of the response body in bytes and display it
size=$(echo -n $response | wc -c)
echo "The size of the response body is $size bytes."
