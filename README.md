
<h1 align="center">:memo::chart_with_upwards_trend: CoronaXiv :cricket::bar_chart:</h1>

<div align="center">

<img src="./screenshots/logo.png" width=400px height=125px/>

<br>

[![](https://img.shields.io/badge/Made_with-Flask-red?style=for-the-badge&logo=flask)](https://flask.palletsprojects.com/en/1.1.x/)
[![](https://img.shields.io/badge/Made_with-Python3-red?style=for-the-badge&logo=python)](https://www.python.org/ "Python3")
[![](https://img.shields.io/badge/Made_with-ElasticSearch-red?style=for-the-badge)](https://www.elastic.co/)
[![](https://img.shields.io/badge/Deployed_on-Heroku-red?style=for-the-badge&logo=heroku)](https://www.heroku.com/  "Heroku")

<br>

</div>

---

<b>Submission for HackJaipur Hackathon 2020.</b> 

<h2>About:</h2>

CoronaXiv is an ElasticSearch-powered AI Search Engine that indexes the thousands of research papers that have piled up in response to the Corona Virus pandemic and illustrates various visualizations.

### Features:

* [x] Dashboard for team coaches consisting of various statistics about the game in general.
* [x] Provide predictions about performance of a player based on numerous parameters like country, ground, time, ball faced, etc. 
* [x] Squad (Playing XI) Prediction feature for a team using K-means clustering. 
* [x] Player vs Player head-on statistics. 
* [x] Team vs Team performance in recent years. 
* [x] Mobile-view support.

<h2>Problem it solves:</h2>

A lot of researchers are working remotely across the globe, where lockdown restrictions are varying. Some researchers are working in labs, while some are working from home. In order to assist them in their endeavor to help defeat the Corona Virus pandemic, it would be really handy for any researcher to have a dedicated search-engine for Covid-19 papers, and also get links to other similar papers which are AI-recommended, so that it saves their time. Every second is precious in this battle against this global pandemic and hence, we have built CoronaXiv, an ElasticSearch-powered AI Search Engine for research papers related to the Corona Virus. 
In the current scenario, one would perform Google search in order to look for some research papers. However, more often than not, certain keywords will yield results not related to the Corona Virus pandemic, and also lack UX since the user has to switch from one paper to another every time by going back to the home screen. With CoronaXiv, one can directly access the papers easily, with different visualizations to assist the user in understanding relations of different papers and identify papers based on keywords, or access papers clustered on basis of similar domains. 



---

<h3 align="center">CoronaXiv as a webapp:</h3>

<div align="center">
<h4 align="center">Landing Page</h4>
<img src="./screenshots/ss1.png" width=900px/>
<br>
</div>

---


### Future scope of this project:

* [ ] Provide more comprehensive data analysis for each team. 
* [ ] Provide partial prediction for squad, building the team around the few players selected by coach. 
* [ ] Provide insights based on graphs. (For eg: the AI system saying that player X is slow in pitch Y against team Z.)
* [ ] With availability of more datasets, convert this project into a full-fledged software. 
* [ ] Used advanced machine learning algorithms ffor squad predictions on a large number of parameters and extracting insights. 

### Tech Stack of this Project:

* Frontend: Vue.js
* Backend: Python3
* Framework: Flask
* Machine Learning Model: K-means Clustering (sklearn)  (elasticsearch?)
* Libraries: Available in [requirements.txt](https://github.com/nachiketbhuta/exsports-analytics/blob/master/requirements.txt). //TODO: update this

### To run the project:

* [Fork](https://github.com/nachiketbhuta/exsports-analytics) this Repository.
* Change into he directory in the terminal and run as:
  -`pip3 install -r requirements.txt`
  -`python3 manage.py runserver`
* Open your web browser and enter the following URL:
`localhost:8000`


#### This project still has scope of development, so you can also contribute to this Project as follows:
* [Fork](https://github.com/nachiketbhuta/exsports-analytics) this Repository.
* Clone your Fork on a different branch:
	* `git clone -b <name-of-branch> https://github.com/nachiketbhuta/exports-analytics.git`
* After adding any feature:
	* Goto your fork and create a pull request.
	* We will test your modifications and merge changes.

This project was done as a part of HackJaipur Hackathon 2020 `with no pre-preparation in less than 24 hours.`

---
<h3 align="center"><b>Developed with :heart: by Team Stochastic.</b></h1>
