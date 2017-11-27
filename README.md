# CelebrityMatch
CelebrityMatch is a small Python application that allows you to compare two Twitter feeds and spits out the top five personality traits that those feeds share in common, along with the percentages of commonalities.

## Setup
On whatever directory you choose on your local machine clone this repository, execute the following commands in a terminal. **__(Note: The command below assumes you have pip installed.)__**
```sh
sudo pip install python-twitter
sudo pip install watson-developer-cloud
```
This makes use of the Twitter API and IBM Personality Insights API.
Afterward, create six local files in the same directory:
1) "twitter-consumer-key.txt"
2) "twitter-consumer-secret.txt"
3) "twitter-access-token.txt"
4) "twitter-access-secret.txt"
5) "ibm-username.txt"
6) "ibm-password.txt"
The first four should contain these appropriate Twitter credentials that you obtain when you make a Twitter application. The last two should be the credentials you obtain when you set up an IBM Bluemix account.

## Execution
To run the program, just execute the following command in a terminal in the directory where you cloned the Git repository. **__(Note: The command below assumes you have Python installed.)__**
```sh
python ./CelebrityMatch.py
```
Then, just follow the prompts.