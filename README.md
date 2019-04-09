# Rutul dictionary
This is a repository for the Rutul dictionary. 

Link to the site: https://linghub.ru/rutuldict

Technical solution: Anastasia Panova & Elena Sokur (HSE Linguistic Convergence Laboratory)

Principal investigators: Michael Daniel & Konstantin Filatov

Date of creation: March 2019

The last version of the script can be found here: https://github.com/LingConLab/Rutul_dictionary


## Structure of the repository:
`/css`: contains standard bootstrap stylesheets and a special css for the DataTables library.

`/images`: technical pictures for the site.

`/js`: 
* standard bootstrap and jquery functions;
* `jquery.dataTables.min.js` contains general settings for the table;
* `dataTables.extraSettings.js` contains individual settings for uploading data to a web-page from a json-file, column searching, and opening and closing additinal rows.

`index.html`: main page of the site.

`make_json.py`: python file which creates a json-file from the original data. 


## Instruction
If you want to use this platform to create your own dictionary:
- in `index.html` change the name and the description of the project, and column names if necessary;
- create a json-file with your data and call it `data.json`;
- in `dataTables.extraSettings.js` change the name of the json-keys;
- create an `/audio` directory and put your audio files there.
