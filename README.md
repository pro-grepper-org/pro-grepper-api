## Api

### The model used for api is LabelPowerset Transformation with Random Forest Classifier

### Route Information :
Api route : apiforprogrepper.herokuapp.com/api/companies

Rquest Type : POST

Params : 
- problem-statement: ' ' // problem statement text
- tags : [ ] //list of tags default empty
- num-companies: 5 //top n most probabilistic companies  

### Flow : 

1) Data received by the api is passed through the following functions :
- HTML tags are removed if any
- Punctuation symbols are removed if any
- Other than alphabets, other symbols are removed
- Stop words are removed
- Stemming is done to convert the tokens into their base form

2) The preprocessed data is then fit into the vectorizer (vectorizer_new.sav)

3) Finally,the data is passed through the model(company_tags_lbps_lg_new.sav) and the probabilities are calculated.

4) The top n probabilistic companies are returned.