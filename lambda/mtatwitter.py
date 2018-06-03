import twitter
import json
import random

QUERY_TEMPLATE = "q={}%20%23mta%20OR%20%23MTA%20OR%20%23NYCTSubway%20since%3A2018-06-01"

with open('credentials.json') as f:
    credentials = json.loads(f.read())

api = twitter.Api(**credentials)

def lambda_handler(_event_json, _context):
    search_dict = json.loads(_event_json['body'])
    print(search_dict)
    search_term = search_dict['search_term']
    result = api.GetSearch(raw_query=QUERY_TEMPLATE.format(search_term))
    dict_result = map(lambda x: x.AsDict(),result)
    reduced_dict_result = map(lambda x: {'created_at':x['created_at'],'text':x['text']}, dict_result)
    return generate_response(json.dumps(list(reduced_dict_result)))
    
    
def generate_response(response_text):
    return {
    "isBase64Encoded": True,
    "statusCode": 200,
    "headers": {},
    "body": response_text
}