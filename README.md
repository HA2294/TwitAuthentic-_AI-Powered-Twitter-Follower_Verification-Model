# Twitter Fake Follwer Detection Model
This Python script can discover whether someone has purchased fake followers for that account. 

This script enables you to analyze any Twitter account and generate a similar scatter plot visualization of their followers. You can typically tell when someone purchased fake followers for an account when there are solid lines of followers that were created around the same time, as shown in the New York Times article.

This is done by frist filling out the required variables 

USER_TO_ANALYZE = 

OAUTH_TOKEN = ''

OAUTH_SECRET = ''

CONSUMER_KEY = ''

CONSUMER_SECRET = ''

Once you have created a twitter account you should be able to find the OAUTH and CONSUMER keys on the "Key and Access Tokens" section and find the consumer key and SECRET on the Application setting. Lastly Userto analyze is just the account you want to run throught the program

Once you have provided values for the five variables, the following script will take care of the remaining tasks.

If you are analyzing an account with a large number of followers, such as hundreds of thousands or more, please note that running the script may require some time due to adherence to the Twitter API's usage limitations. A progress bar will keep you informed about the analysis progress.

Upon completion, the script will save an image in the directory where you executed it. This image will contain the scatter plot visualization for the specified Twitter account.

