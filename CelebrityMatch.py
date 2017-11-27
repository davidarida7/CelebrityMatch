import sys
import operator
import requests
import json
import twitter
from watson_developer_cloud import PersonalityInsightsV2 as PersonalityInsights
import sys

def analyze(handle):
  twitter_consumer_key_file = open("twitter-consumer-key.txt", "r")
  twitter_consumer_key = twitter_consumer_key_file.read()
  twitter_consumer_key_file.close()

  twitter_consumer_secret_file = open("twitter-consumer-secret.txt", "r")
  twitter_consumer_secret = twitter_consumer_secret_file.read()
  twitter_consumer_secret_file.close()

  twitter_access_token_file = open("twitter-access-token.txt", "r")
  twitter_access_token = twitter_access_token_file.read()
  twitter_access_token_file.close()

  twitter_access_secret_file = open("twitter-access-secret.txt", "r")
  twitter_access_secret = twitter_access_secret_file.read()
  twitter_access_secret_file.close()
  
  twitter_api = twitter.Api(consumer_key=twitter_consumer_key, consumer_secret=twitter_consumer_secret, access_token_key=twitter_access_token, access_token_secret=twitter_access_secret)
  
  statuses = twitter_api.GetUserTimeline(screen_name=handle, count=200, include_rts=False)
  
  text = ""
  
  for status in statuses:
    if (status.lang == 'en'): #English tweets
    #Adjusting for all types of Python  
      if sys.version_info < (3, 0, 0):
      	text += status.text.encode('utf-8')
      else:
      	text += status.text

     
  #The IBM Bluemix credentials for Personality Insights!

  pi_username_file = open("ibm-username.txt", "r")
  pi_username = pi_username_file.read()
  pi_username_file.close()  

  pi_password_file = open("ibm-password.txt", "r")
  pi_password = pi_password_file.read()
  pi_password_file.close()
  
  personality_insights = PersonalityInsights(username=pi_username, password=pi_password)
  pi_result = personality_insights.profile(text)
  return pi_result

def flatten(orig):
    data = {}
    for c in orig['tree']['children']:
        if 'children' in c:
            for c2 in c['children']:
                if 'children' in c2:
                    for c3 in c2['children']:
                        if 'children' in c3:
                            for c4 in c3['children']:
                                if (c4['category'] == 'personality'):
                                    data[c4['id']] = c4['percentage']
                                    if 'children' not in c3:
                                        if (c3['category'] == 'personality'):
                                                data[c3['id']] = c3['percentage']
    return data

def compare(dict1, dict2):
    compared_data = {}
    for keys in dict1:
        if dict1[keys] != dict2[keys]:
                compared_data[keys]=abs(dict1[keys] - dict2[keys])
    return compared_data

user_handle = "@dee_arida"
celebrity_handle = "@ADP"
user_result = analyze(user_handle)
celebrity_result = analyze(celebrity_handle)

#First, flattening the results from the Watson PI API
user = flatten(user_result)
celebrity = flatten(celebrity_result)

#Then, comparing the results of the Watson PI API by calculating the distance between traits
compared_results = compare(user,celebrity)

#Finally, sorting and displaying top 5 results
sorted_result = sorted(compared_results.items(), key=operator.itemgetter(1))

#The results are displayed in the following format:
#Matched Personality Trait -> Probability of your profile exhibiting given trait -> Probability of Celebrity's profile exhibiting given trait -> Difference between probabilities
for keys, value in sorted_result[:5]:
    print (keys),
    print ('->'),
    print (user[keys]),
    print ('->'),
    print (celebrity[keys]),
    print ('->'),
    print (compared_results[keys])