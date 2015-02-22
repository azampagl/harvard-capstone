#!/bin/sh

# Reuse head from one of the files.
head -n1 ../../../data/weather/ncdc_snowfall/201401.csv > ../../../data/weather/ncdc_snowfall.csv

# Append all others, extracting head line first and replacing all (missing) -9999.000 values with zeros.
cat ../../../data/weather/ncdc_snowfall/*.csv | grep -v 'date,snowfall' | sed 's/,-9999.000/,0.000/g' >> ../../../data/weather/ncdc_snowfall.csv
