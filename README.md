# Twitter Fake Followers Analyzer

This Python script can discover whether someone has purchased fake followers for their Twitter account.

## Description

This script enables you to analyze any Twitter account and generate a scatter plot visualization of their followers. By examining the scatter plot, you can identify solid lines of followers that were created around the same time, indicating the possibility of fake followers, as shown in the New York Times article.

## Usage
```python
1. Fill out the required variables in the script:

USER_TO_ANALYZE = ''
OAUTH_TOKEN = ''
OAUTH_SECRET = ''
CONSUMER_KEY = ''
CONSUMER_SECRET = ''

- **USER_TO_ANALYZE:** The Twitter account username you want to analyze.
- **OAUTH_TOKEN:**  The OAuth token obtained from Twitter for authentication.
- **OAUTH_SECRET:** The OAuth secret obtained from Twitter for authentication.
- **CONSUMER_KEY:** The consumer key obtained from Twitter for authentication.
- **CONSUMER_SECRET:** The consumer secret obtained from Twitter for authentication.

1. Fill out the required variables in the script: 

2. Once you have created a Twitter account and obtained the OAuth and consumer keys, replace the empty strings with the corresponding values.

Run the script, and it will take care of the remaining tasks.

```

### Note: 

  If you are analyzing an account with a large number of followers (e.g., hundreds of thousands or more), please be aware that running the script may require some time due to adherence to the Twitter API's usage limitations. A progress bar will  keep you informed about the analysis progress.

  Upon completion, the script will save an image in the directory where you executed it. This image will contain the scatter plot visualization for the specified Twitter account.

## Requirements
Python
Python libraries: tweepy, matplotlib, numpy

## License
This project is licensed under the MIT License. You are free to use, modify, and distribute the codebase for personal or commercial purposes.

## Contact
If you have any questions or suggestions regarding the Twitter Fake Followers Analyzer, please feel free to contact us at your-email@example.com. We appreciate your interest and look forward to hearing from you.
