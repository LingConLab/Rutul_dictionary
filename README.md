# Rutul dictionary
This is a repository for Rutul dictionary. 

Link to the site: https://linghub.ru/rutuldict

Technical solution: Anastasia Panova & Elena Sokur (HSE Linguistic Convergence Laboratory)

Principal investigators: Michael Daniel & Konstantin Filatov

Date of creation: March 2019

The last vertion of this script is here: https://github.com/LingConLab/Rutul_dictionary


## Structure of the repository:
`/css`: contains standard bootstrap stylesheets and a special css for DataTables library.

`/images`: technical pictures for the site.

`/js`: 
* standard bootstrap and jquery functions;
* `jquery.dataTables.min.js` contains general settings for the table;
* `dataTables.extraSettings.js` contains individual settings for uploading data to a web-page from a json-file, column searching, and opening and closing additinal rows.

`index.html`: main page of the site.

`make_json.py`: python file which creates json-file from original data. 


# Instruction
If you want to use this platform to create your own dictionary:
- in `index.html` change a name and discription of the project, and column names if necessary;
- create a json-file with your data and call it `data.json`;
- in `dataTables.extraSettings.js` change name of json-keys;
- create `/audio` directory and put your audio files there.