# Avalara AvaTax Python SDK
[![Build Status](https://travis-ci.org/RJB888/Python_Final.svg?branch=master)](https://travis-ci.org/RJB888/Python_Final)

## Introduction
This GitHub repository is the Python SDK for Avalara's world-class tax service, AvaTax.  It uses the AvaTax REST v2 API, which is a fully REST implementation and provides a single client for all AvaTax functionality.  For more information about AvaTax REST v2, please visit [Avalara's Developer Network](http://developer.avalara.com/) or view the [online Swagger documentation](https://sandbox-rest.avatax.com/swagger/ui/index.html).


## Getting Started

**Setup**

``` bash
# Clone repository to your local machine
$ git clone https://github.com/RJB888/Python_Final.git

# cd into the Python_Final directory
$ cd Python_Final
```

**Environment**

``` bash
# Begin a new virtual environment with Python 3 
Python_Final $ python3 -m venv ENV

# Activate environment
Python_Final $ source ENV/bin/activate
```

**Installation**

Install [pip](https://pip.pypa.io/en/stable) if you don't have it already

``` bash
# pip install package  
(ENV) Python_Final $ pip install -e .

# pip install testing set of extras
(ENV) Python_Final $ pip install -e .[testing]
```

## SDK Development

### Environment

Avalara provides two different environments for AvaTax: **Sandbox** and **Production**.

The **Sandbox** environment is meant to help you test your software without the risk of accidentally affecting production data or reporting transactions. 

In **Production**, transactions that are marked Committed can be reported on a tax filing using the Avalara Managed Returns Service.

Each environment is completely separate, and each has its own credentials.

If you have a Sandbox account, you cannot use that account to log onto Production; and vice versa.


### Setup Test Credentials

For testing, your credentials are accessed as environment varibales through os.environ.

Add the following to the ```activate``` file in your environment:

``` bash
# Username and password
USERNAME='your_sandbox_username'
PASSWORD='your_sandbox_password'

# Or account id and license key
ACCOUNT_ID='your_sandbox_account_id'
LICENSE_KEY='your_sandbox_license_key'
```


### Meet the Team:

[Han Bao](https://github.com/han8909227)

[Philip Werner](https://github.com/philipwerner)

[Robert Bronson](https://github.com/RJB888)

[Adrienne Karnoski](https://github.com/adriennekarnoski)
=======
