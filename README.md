# Flip Test

Using django framework to solve the flip test

for detailed version see on requirements.txt

demo on heroku:

[get token] (https://test-flip.herokuapp.com/api/token/)
[disburse api] (https://test-flip.herokuapp.com/disbursement/disburse)


## Installation

### use docker

start:
```bash
docker-compose up web
```

running the test:
```bash
docker-compose up test
```

### use direct python
```bash
pip install -r requirements.txt
```

start:
```bash
python manage.py runserver 0.0.0.0:{PORT}
```

running the test:
```bash
python manage.py test
```


## Usage

### get token

username: hend

password: 123
```bash
curl -H "Content-Type: application/json" -X POST --data '{"username":"hend","password":"123"}' http://{base_url}/api/token/
```

response
```json
{"refresh":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYwNzEzMTUyOSwianRpIjoiZGI0YzdiOTM1YjgwNDY0ZmI5NTkwMzU0NmVhMTIzZWYiLCJ1c2VyX2lkIjoxfQ._xsVeom8bAzgnYw58IW3gzCa9wutu_Sbgg6L1bMIY8E","access":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjA3MDQ1NDI5LCJqdGkiOiI4MTg5ZDVhYmEwOWQ0MDYxODc0OTQ3MTg5OWE3NTdjZSIsInVzZXJfaWQiOjF9.zPPNdVSW7gQZKGXkSt24J3rbXsLfuDuG1Sa6DZbeAeo"}
```

### create disbursement

request POST /disbursement/disburse

content-type "application/json"

Authorization Bearer {token}

body:
```json
{
    "bank_code":"3214",
    "account_number":"123123123213",
    "remark":"test123",
    "amount":200000
}
```

response 200:
```json
{
    "status_code": 200,
    "message": {
        "id": 7873843548,
        "amount": 200000,
        "status": "PENDING",
        "timestamp": "2020-12-03 14:20:44",
        "bank_code": "3214",
        "account_number": "123123123213",
        "beneficiary_name": "PT FLIP",
        "remark": "test123",
        "receipt": null,
        "time_served": "0000-00-00 00:00:00",
        "fee": 4000
    }
}
```

### update disbursement

request PUT /disbursement/disburse/<id>

content-type "application/json"

Authorization Bearer {token}

response 200:
```json
{
    "id": 787384354,
    "amount": 10000,
    "status": "PENDING",
    "timestamp": "2020-12-04 12:10:25",
    "bank_code": "bni",
    "account_number": "1234567890",
    "beneficiary_name": "PT FLIP",
    "remark": "sample remark",
    "receipt": "https://flip-receipt.oss-ap-southeast-5.aliyuncs.com/debit_receipt/126316_3d07f9fef9612c7275b3c36f7e1e5762.jpg",
    "time_served": "2020-12-04 12:19:25",
    "fee": 4000
}
```

## Demo

already up on heroku

[get token] (https://test-flip.herokuapp.com/api/token/)
[disburse api] (https://test-flip.herokuapp.com/disbursement/disburse)