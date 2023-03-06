# Covid-19-BE

## Project: Covid-19-BE

### Author: Amani M AL-Zoubi

### description
- The goal of this API is so that the user can communicate with the database and view/add/update/delete records of the COVID-19 statistics retrieved from the user. 

### Links and Resources

- [Django REST framework](https://www.django-rest-framework.org/)

### Setup

- use python version 3.10.7

#### `.env` requirements 
- create a .env file inside the Covid19 folder and copy everything in `.env.sample` inside it 

#### How to initialize/run your application (where applicable)
- I used docker , so you need to run it from docker container
    `docker-compose up` to run it from your machine 
- Use `http://127.0.0.1:<PORT>/api/v1/records/` to get records API 
- for specific Game add it's id to your path like `http://127.0.0.1:<PORT>/api/v1/records/1`

### Authentication and Permission for models


| API end-points        | HTTP Method   | Authentication  | Permission  | Result                                       |
|---------------------- |-------------  |------------   |------------  |------------------------------------------     |
| /record                 | GET           | AnyOne          | AnyOne        |  view all the records that are retrieved                  |
| /record                 | POST          | AnyOne          | AnyOne         | Create new record                                |
| /record/{record_pk}       | GET           | AnyOne          | AnyOne         | Retrieve details of a particular record         |
| /record/{record_pk}       | PUT           | AnyOne          | AnyOne         | Update a particular record's info               |
| /record/{record_pk}       | DELETE        | AnyOne          | AnyOne         | Delete a particular record's details from DB    |
