# Covid-19-BE

## Project: Covid-19-BE

### Author: Amani M AL-Zoubi

### Links and Resources

- [Django REST framework](https://www.django-rest-framework.org/)

### Setup

- use python version 3.10.7

### description
- The goal of this API is so that the user can communicate with the database and view/add/update/delete records of the COVID-19 statistics retrieved from the user. 


### Authentication and Permission for models


| API end-points        | HTTP Method   | Authentication  | Permission  | Result                                       |
|---------------------- |-------------  |------------   |------------  |------------------------------------------     |
| /record                 | GET           | AnyOne          | AnyOne        |  view all the records that are retrieved                  |
| /record                 | POST          | AnyOne          | AnyOne         | Create new record                                |
| /record/{record_pk}       | GET           | AnyOne          | AnyOne         | Retrieve details of a particular record         |
| /record/{record_pk}       | PUT           | AnyOne          | AnyOne         | Update a particular record's info               |
| /record/{record_pk}       | DELETE        | AnyOne          | AnyOne         | Delete a particular record's details from DB    |
