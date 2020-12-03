# ShipayTest 

### Lew Andrade's technical test for the role of Junior Backend Developer on Shipay.
This test consists of a RESTful API made in Python 3 representing the payment from a client to an establishment.  
---
## Building
The repo already has the Python Virtual Environment with the all the necessary dependencies to build the application, so to run it simply execute the `app.py` file:

`python app.py`

#### Dependencies
The application was made using: `Flask`, `Flask-SQLAlchemy`, `Flask-RESTful` and `flask-marshmallow`. `marshmallow-sqlalchemy` was also used to clear some conflicts;

## Testing the endpoints
Located in http://localhost:5000, the API endpoints are:

`/api/v1/transacao` with `GET` and `POST`; 

and

`/api/v1/transacao/<int:transaction_id>` with `GET`, `PUT` and `DELETE`

`<int:transaction_id>` being the Id of a single transaction created by the `POST` request.

---




### _Important note_
_This is **NOT** an official Shipay project, it is an employment test made by Lew Andrade, and thus has **NO** correlation with Shipay and it's Intellectual Properties whatsoever._
