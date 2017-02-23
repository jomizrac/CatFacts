# CatFacts
Exercise for BW DX internship

This program sends a random cat fact to a list of numbers given in a JSON file, waiting 3 seconds between messages
Example JSON files for numbers and cat facts have been included in this Git Repo

To run:

1. Ensure a file named "numbers.json" exists in the current directory, and contains a list of phone numbers

2. Ensure your Catapult credentials are placed in the /home/\<user>/ directory in a file named ".bndsdkrc"

3. If wanted, place a JSON file created on http://catfacts-api.appspot.com/ into the current directory.  Use the following URL to get the list: "http://catfacts-api.appspot.com/api/facts?=5" and replace 5 with the desired number of cat facts to choose from, up to 100.

4. On the command line, run the following: python catfacts.py \<filename>

filename above can be left blank to use the default cat fact list, or can be the filename of the cat fact list in the current directory
