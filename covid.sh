#!/bin/bash
# This script downloads covid data and displays it

POSITIVE=$(curl https://api.covidtracking.com/v1/us/current.json | jq '.[0].positive')
TODAY=$(date)

echo "On $TODAY, there were $POSITIVE positive COVID cases"

DATA=$(curl -s https://api.covidtracking.com/v1/us/current.json)

POSITIVE=$(echo "$DATA" | jq '.[0].positive')
NEGATIVE=$(echo "$DATA" | jq '.[0].negative')
DEATHS=$(echo "$DATA" | jq '.[0].death')
HOSPITALIZED=$(echo "$DATA" | jq '.[0].hospitalizedCurrently')
LAST_UPDATED=$(echo "$DATA" | jq '.[0].lastModified')

TODAY=$(date)

echo "Covid data as of $TODAY:"
echo "Total positive cases: $POSITIVE"
echo "Total negative cases: $NEGATIVE"
echo "Total deaths: $DEATHS"
echo "Currently hospitalized: $HOSPITALIZED"
echo "Last updated: $LAST_UPDATED"
