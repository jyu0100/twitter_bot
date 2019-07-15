import tweepy 
import time

print('this is my twitter bot')

CONSUMER_KEY = 'STI8m0HL4oAUPQnhvjLWxtxgj'
CONSUMER_SECRET = 'aWIOclR1aAlxQ9kM0uAalV0462JbzTcc3Y3EbfhUalp5MadkfN'
ACCESS_KEY = '1149354407768801282-j9T77S8nLc1zYC7r5mShC2oEO0V2nN'
ACCESS_SECRET = 'CIBCKa9Exk9dfkxIFdwbf313bZNNLPcmm7rHPNICOkSoz'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

FILE_NAME = 'last_seen_id.txt'

#these id functions are to stop the bot from constantly looking over the old tweets that 
#have been responded to

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def reply_to_tweets(): 
    print('retrieving and replying to tweets...')
    # use 1150850522901045249 for testing
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    mentions = api.mentions_timeline(last_seen_id, tweet_mode = 'extended')
    # api.mentions_timeline() is part of tweepy.ResultSet which is a subclass of Python's list

    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text)
        last_seen_id = mention.id 
        store_last_seen_id(last_seen_id, FILE_NAME)
        if '#hello' in mention.full_text.lower():
            print('found #hello')
            print('responding back...')
            api.update_status('@' + mention.user.screen_name + '#HelloWorld Why are you talking to a bot?', mention.id)

while True:
    reply_to_tweets()
    time.sleep(15)