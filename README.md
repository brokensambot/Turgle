# Turgle

Sometimes you have questions that only other humans can answer. What if asking them was as easy as using Google?

## RESTful API Methods

### Ask a Question

URL: https://www.turgleapi.com/api/question  
Format: JSON  
Method: POST  
Parameters:

+ **accessKey** - (required) Your Amazon Web Services access key.
+ **secretKey** - (required) Your Amazon Web Services secret key.
+ **answers** - (required) The number of answers you require (not guaranteed to be unique).
+ **text** - (required) The question being asked.

Response:  
```
{"HITId": "GBHZVQX3EHXZ2AYDY2T0"}
```

### Get Answers

URL: https://www.turgleapi.com/api/answers  
Format: JSON  
Method: GET  
Parameters:

+ **accessKey** - (required) Your Amazon Web Services access key.
+ **secretKey** - (required) Your Amazon Web Services secret key.
+ **HITId** - (required) The HIT Id associated with the question that was asked (only valid for questions asked via the Turgle API).

Response:  
```
{"answers": ["Red", "Green", "Blue"]}
```
