# Turgle

Sometimes you have questions that only other humans can answer. What if asking them was as easy as using Google?

## RESTful API Methods

### Ask a Question

URL: https://www.turgleapi.appspot.com/api/question  
Format: JSON  
Method: POST  
Parameters:

+ **accessKey** - (required) Your Amazon Web Services access key.
+ **secretKey** - (required) Your Amazon Web Services secret key.
+ **answersLimit** - (required) The number of answers you require (not guaranteed to be unique).
+ **image** - (optional) An image related to the question you're asking (bmp, gif, ico, jpeg, png, tiff, and webp image data formats are accepted).
+ **text** - (required) The question you're asking.

Response:  
```
{"questionId": 12345}
```

### Get Answers

URL: https://www.turgleapi.appspot.com/api/answers  
Format: JSON  
Method: GET  
Parameters:

+ **accessKey** - (required) Your Amazon Web Services access key.
+ **secretKey** - (required) Your Amazon Web Services secret key.
+ **questionId** - (required) The questionId associated with the question you're interested in.

Response:  
```
{"answers": ["Red", "Green", "Blue"]}
```
