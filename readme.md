# Product Rating System
#### Using Text Based Sentiment Analysis
<hr>

## About
__This product generates rating of a product in an e-commerce website by analyzing the text based review provided by the users.__ <br>
The system uses sentiment analysis methodology in order to achieve desired functionality. The reviews provided by the users about a product on an e-commerce website is analyzed and rating of that product is generated based on the review. This system completely eradicates the trouble of giving rating as well as writing review and helps to generate accurate rating based on user reviews. <br><br>
<a href="https://google.com" > Learn More </a>

## Installation
The application runs on Python's __Flask__ micro  web framework. The following packages are required to be installed in order to run this application.
> __Packages for Sentiment Analysis__
  - numpy
  - pandas
  - tqdm
  - tensorflow
  - sklearn
  - matplotlib
  - keras
  - nltk
  
  <br>
  <br>
  
  > __Packages for Web Application__
  - flask
  - SQLAlchemy
  - Flask-MySQL
  - mysqlclient
  
Install these packages using <code>pip</code> (i.e. <code> pip install numpy</code>)

If problems arises during installing <code>mysqlclient</code> (eg: Microsoft Visual C++ 14.0 is required), visit <a href="https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient">this </a> link and download .whl file for your system and python version and run <br>
<code>pip install c:\location_to_whl_file\mysqlclient‑1.3.13‑cp36‑cp36m‑win_amd64.whl</code>

Download __LSTM Model__ and __Text Data__ frome <a href="https://drive.google.com/drive/folders/1M5-5ITbUmj2BA8fUfMDkBG7OiSJLTMKq?usp=sharing"> here </a>and place them inside the folder containing above files.

The folder should look as follows:


## Usage
Open __Command Prompt (CMD)__ and navigate to the folder containing the files. Then run
<code>flask run</code>
OR
<code>python app.py</code>
