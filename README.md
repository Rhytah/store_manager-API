# store_manager-API
API endpoints to manage store data

[![Maintainability](https://api.codeclimate.com/v1/badges/c12a0e5277a846a7a1aa/maintainability)](https://codeclimate.com/github/Rhytah/store_manager-API/maintainability)

[![Build Status](https://travis-ci.org/Rhytah/store_manager-API.svg?branch=ft-161237635--admin-fetch-all-sale-records)](https://travis-ci.org/Rhytah/store_manager-API)

[![Coverage Status](https://coveralls.io/repos/github/Rhytah/store_manager-API/badge.svg?branch=ch-161341127-route-protection-and-validations)](https://coveralls.io/github/Rhytah/store_manager-API?branch=ch-161341127-route-protection-and-validations)


[![codecov](https://codecov.io/gh/Rhytah/store_manager-API/branch/master/graph/badge.svg)](https://codecov.io/gh/Rhytah/store_manager-API)



### Tools

* Text editor where we write our project files. (VScode)
* Flask Python Framework -Server-side framework
* Pytest - a Python Testing Framework
* Pylint - a Python linting library 
* Postman -Application to test and consume endpoints
* PEP8 - Style guide

**Getting Started**
clone the github repo to your computer:
* $git clone https://github.com/Rhytah/store_manager-API.git
* Extract the zip file to another file

**Create virtual environment and activate it**
```
$pip install virtualenv
$ virtualenv venv
$ venv\Scripts\activate
``` 
 **Install all the necessary tools by**
 ```
 $pip insatll -r requirements.txt
 ```
**Start app server in console/terminal/commandprompt**
```
$python app.py
```
**Test app in terminal**
```
$pytest
```
## Versioning
```
This is version one"v1" of the API
```
## End Points(Required Features)
|           End Point                                 |            Functionality                   |
|   -----------------------------------------------   | -----------------------------------------  |
|     POST api/v1/products                            |             Create a product               |
|     GET  api/v1/products                            |             Fetch all products             |
|     GET  api/v1/products/<int:productId>            |             Fetch a product                |
|     POST api/v1/sales                               |             Add a sale order               |
|     GET  api/v1/sales/<int:saleId>                  |             Fetch a specific sale order    |
|     GET  api/v1/sales                               |             Admin fetch all sale orders    |

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/fd78148dfa33db6ba32c)

## Author
- [Rhytah] https://github.com/Rhytah