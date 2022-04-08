
# Hi, I'm Ayush Shresth! 👋


# Micro-Services ( Django )


An Application by Breaking the Monolithic Architecture to MicroService Architecture to acquire more scalability.

Technologies used were Python Script, **Django framework**, **Django Rest FrameWork**.

## Introduction
This application contains three services,

**Check this link to understanding the  Model/Architecture diagram and Workflow.**
https://whimsical.com/Vojg5KGTovsX2TkUczpVEf/

## Installation
Install services with pip

```bash
  bin/virtualenv testing 
  source bin/activate
  pip install -r /path/to/requirements.txt
```

## Services
## User Service**
  - Service description : Contains user details like name, email etc
  - Apis required :
      - Fetch users
      - Create a new user

**Run Locally**

Go to the project directory

```bash
  cd user_service
```

Start the server in the new bash

```bash
  py manage.py runserver 8000
```
## 🔗 APIs Details
- Admin Panel 
  - localhost/admin/
  - UserName -> **user** & Password -> **user**
- Fetch a user using user_id (GET)
   - localhost/api/user/**$user_id**/ 
- Fetch all user (GET)
   - localhost/api/user/ 
- Create a new user (POST)
   - localhost/api/user/ 


## Content Service**
   - Service description : Contains meta of readable content that we serve to the users
   - Each content is structured as a series which can contain multiple chapters.
   - Example: consider a series called “Harry Potter” which has 7 chapters
- Apis required :
  - Fetch content for a user
       - Input : userid , multiple series ids
       - Output : content meta with only unlocked chapters per series
  - Api for bulk upload of the content

**Run Locally**

Go to the project directory

```bash
  cd content_service
```

Start the server in the new bash

```bash
  py manage.py runserver 8001
```
## 🔗 APIs Details
- Admin Panel ( To see the Model Table )
  - localhost/admin/
  - UserName -> **user** & Password -> **user**
- Fetch content for a user using user_id and series_id (GET)
   - localhost/api/content/**$ user_id**/**$ series_id**/
- Api for bulk upload of the content (POST)
   - localhost/api/content/load/  


## Daily Pass**
- Service description : Contains the details of how many chapters per series is unlocked for a
particular user.
- Rest of the chapters are released on a daily basis; that is one chapter per day
- Any new content that is uploaded, again by default has 4 unlocked chapters for all the
users

- One should consider the scenario that there may be newly uploaded content. Not all the
content will be fed to the system on a single day
- So if a series is uploaded after user creation then the existing users should also see that
series with only 4 chapters unlocked

- Apis required
   - Api to unlock one chapters for the given user and series
       - For testing purpose : this api should not be idempotent, if I hit the api twice, it
should unlock two episodes for the requested user and series
        - Number of unlocked chapters = 4 + no. of times unlock api is hit
    - Fetch daily pass data by user

**Run Locally**

Go to the project directory

```bash
  cd daily_pass
```

Start the server in new bash

```bash
  py manage.py runserver 8002
```

## 🔗 APIs Details
- Admin Panel ( To see the Model Table )
  - localhost/admin/
  - UserName -> **user** & Password -> **user**
- Api to unlock one chapters for the given user and series (GET)
   - localhost/api/daily_pass/unlock_chapter/**$ user_id**/**$ series_id**/
- Api to Fetch daily pass data by user (GET)
   - localhost/api/daily_pass/chapter_detail/**$ user_id**/**$ series_id**/

## 🚀 About Me

I'm a very enthusiastic coder who desires to learn and a solution-oriented individual with a variety of technical skills.

 - Proficiency in java & Python.

 - Strong Problem-Solving Skills.

 - Good Knowledge of Data Structures & Algorithms.

- Command over both Frontend & Backend Web Development(django+react).


## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ayush-514875198/)
## 🛠 Skills
Django, React.js, Redux, Python, Javascript, Java, HTML, CSS...


## Feedback

If you have any feedback, please reach out to us at ayushshresth97@gmail.com
