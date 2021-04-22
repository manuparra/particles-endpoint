


# Particles EndPoint (API RESTFUL)

  * [Installing](#installing)
  * [Run the webservice for the EndPoint](#run-the-webservice-for-the-endpoint)
  * [EndPoint information](#endpoint-information)
    + [Parameters](#parameters)
    + [Output](#output)
  * [Code configuration](#code-configuration)
    + [EndPoint](#endpoint)
    + [Database](#database)
    + [Output data](#output-data)
  * [How to improve](#how-to-improve)
    + [API Documentation](#api-documentation)
    + [Architecture design to performance](#architecture-design-to-performance)
    + [Test Driven Development (TDD)](#test-driven-development--tdd-)
  * [Running in containers (Kubernetes/Docker)](#running-in-containers--kubernetes-docker-)



- Nektarios Benekos (nektarios.benekos@cern.ch)


## Installing

- Clone this repository ``git clone ...``
- Go to the folder created (``particles_endpoint``) and run inside: ``pip install -r requirements.txt``. It will install ``Python flask`` and ``Python PyMySQL``.

Requeriments are, ```Flask==1.0.2``` and ```pymysql==0.7.11```.


## Run the webservice for the EndPoint

Firstly, check if datastore and the database config is the correct for you in the setup file. Edit ``setup`` file and customize the parameters. By default the  parameters are just for testing (syntetic) and works for testing purposes.

Then, go to the ``code`` folder and run:

```
python app.py 0.0.0.0 8098
```

where: 
- ``app.py`` is the main web application containing the EndPoint functions.
- ``0.0.0.0`` is the IP to bind the EndPoint webservice.
- ``port`` is the port for the EndPoint

Go to your WEB BROWSER (Chrome, FireFox, ...) and paste: 

```
http://localhost:8098/particles/?lookup=BRC
```

You will see the query results to the EndPoint with the string ``BRC``

*Example*:

```
python app.py 192.168.0.1 8080
```

It will run the end point on the Physical ethernet IP ``192.168.0.1`` and port ``8080``.


## EndPoint information

The EndPoint is enabled in the URL: 

```
http://_______/particles/
```

### Parameters

It receives 2 parameters with the operation ``GET`` (POST, PUT, etc, are not allowed):

- ``lookup``: String of more than 3 characters - **Mandatory**
- ``species``: String of more than 3 characters - **Optional**

Examples:

```
http://_______/particles/?lookup=BRC
```

or

```
http://_______/particles/?lookup=BRC&species=S1
```
or  

```
http://_______/particles/?lookup=BRMC&species=S1
```




### Output

**Return**:

JSON object (list of dicts) like this example: 

```
[
    {
        "astrolake_id": 1,
        "gene_name": "BRCA1",
        "location": "L1",
        "species": "S1"
    },
    ...
    ]
```


Where ``astrolake_id`` id the ID of the particle in the AstroLake System, ``gene_name`` is the name of the particle, ``location`` is the location of the particle, and the last ``species`` is the specie of the particle related.


## Code configuration

Some code configuration to have into account.

### EndPoint 

The EndPoint is inside the main file of the web service at app.py.  To modify the EndPoint URI, change the line 

```
@app.route('/particles/', methods=['GET'])
``` 

to the corresponding URI, for instance:

```
@app.route('/astrolake/particles/', methods=['GET'])
``` 



### Database

The database used for this example is MySQL. The configuration data can be found in the setup file ``setup``. By default is included some  data to a test server with synthetic data.

### Output data

To modify the output data of the query, it is necessary to modify the configuration in the file ``db/dbstore.py`` .


## How to improve

### API Documentation

For the documentation of a RESTful API, one of the best options is to use the OpenAPI proposal, through which you can model a series of functionalities. A tool to generate the API documentation code is https://editor.swagger.io/, through which all the API parameterization is configured.

The OpenAPI documentation for the Particles EndPoint is the next: 

- [OpenAPI Particles HTML Doc](./extras/particles_openapi.html)
- [OpenAPI Particles Def](./extras/particles_openapi.yml)
- [OpenAPI Particles Example server](./extras/particles_openapi_server.zip)

About the code in python: 

- Documentation tool like ``Sphinx`` is highly recommended.




### Architecture design: focus in the performance

In order to improve the performance of the API EndPoint, taking into account a possible massive increase in requests per second, several architectures are proposed:

- Model based on HAProxy and computation nodes (or VM-Containers) to serve the requests.
- Model based on Kubernetes, to adjust the request demand to the number of working containers (pods) in a elastic way.
- NoSQL Database Model, which allows distributing data in multiple nodes in an elastic way. This would eliminate a bottleneck, with access to them more directly. 
- Data caching: Partially load particle data into nodes / computing units for faster access. Implement different levels of caching.



### Test Driven Development (TDD)

Test-driven development (TDD) is one of the  software engineering practice that involves two other practices: Writing the tests first (Test First Development) and Refactoring. Unit tests are generally used to write the tests, so, first, a test is written and it is verified that the tests fail.

![ImgTests](https://cdn-media-1.freecodecamp.org/images/1*FZGakHQbCUMAyDinf-KBiw.png)

Example: Test case, checking if our function Calculator (class) have value 0 when start (for instance):


```
import unittest  

# Test Class
class TestMyCalculator(unittest.TestCase):  

    # Testing function if
    def test_initial_value(self):
        calc = Calculator()
        self.assertEqual(0, calc.value)
    
```

Then run:

```
python -m unittest discover
```




