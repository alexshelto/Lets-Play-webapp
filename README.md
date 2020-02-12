# Lets Play Web Application

## Table of contents
- [Developers](#developers)
  * [Roles](#roles)
- [Project Description](#project-description)
  * [Tools](#tools)
  * [Project Plans](#plans-for-final-project)
- [Installing](#installing-dependencies)
- [Running Locally](#running-locally)




### Developers
* Alexander Shelton @alexshelto
* Ben Bauer @benjaminxbauer
* AJ Stein @AJStein51
* Hunter Burden @HunterBurden

### Roles
Alex: Team Lead (float)
Ben and Hunter: Back End
AJ: Front End

### Project Description
This is a webapp that allows users to find group members for different games.
Games can be pickup basketball, videogames, and dungeons and dragons.

### Tools
* Flask
	* Backend Routing using Python
* Github
	* Code repository
* Jinja
	* Frontend templating
* sqlite
	* Database
	
### Plans for final project
We are planning on hosting this web app on a website to allow people to access it via smartphone / computer


### Installing dependencies
> It is highlt recomended to use a virtual machine for python
(put links for virtual env)

> Make sure you are using python 3.x
> Activate virtual machine
```shell
cd Lets-Play-webapp
pip install -r requirements.txt
```

### Running Locally
> The application itself is built in the run.py file. This line will set your run.py file up as the main file
```shell
export FLASK_APP=run.py
```
> When running your app locally it is recomended to be in debugger mode. To put your app in debugger mode and run the web app this line can be used.
```shell
FLASK_DEBUG=True flask run
```


