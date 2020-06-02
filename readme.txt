

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

STEP 3 : Fore each episode in STEP 2, fetch the transcript

Prototype : saveeachepisodetotextfile.py
Output: episodecompletetext.txt



Code : Work in Progress(WIP)

STEP 4 : Get the  list of movies seperately

Code: listofmovies.py
Output : list-of-all-movies.json in the Movies folder

STEP 5 : For each move in Step 4 , get the movie transcript

Code: 
Output : in the Movies folder

***

POST SCRAPING :

	Clean the data. ( Online store, COVID, Transcript Index links in each file)

