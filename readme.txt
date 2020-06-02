

Scraping 

git clone 
python3 -m venv transcripts-scraping
source ./transcripts-scraping/bin/activate
cd transcripts-scraping
pip install -r requirements.txt

STEP 1 : Get list of tv serials from https://transcripts.foreverdreaming.org/index.php

Code : listoftvserials.py
Output : listoftvserials.json ( PRETTY PRINT JSON SHELL COMMAND- `cat listoftvserials.json | jq` )

STEP 2 : Get list of episodes for each tv serial from STEP 1


Code : listofepisodesforeachtvserial.py
Output: listofepisodesforeachtvserial.json

***
WORK IN PROGRESS

