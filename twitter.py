import support
import tweepy
import json
from transformers import pipeline
from kafka import KafkaProducer
from kafka.admin import KafkaAdminClient, NewTopic

producer = KafkaProducer(bootstrap_servers=support.kafka_path)

def find_sentiment(tweet):
	classification = classifier(tweet.text)
	polarity = classification[0]["label"]
	return polarity

class KafkaListener(tweepy.StreamingClient):
	def on_tweet(self, tweet):
		polarity = find_sentiment(tweet)
		my_hashmap = {"id":tweet.id,"sentiment":polarity}
		producer.send(support.topic, bytes(json.dumps(my_hashmap), 'utf-8'))
		print("Connection successful. Tweet Sentiment: ", polarity)
		producer.flush()
		

if __name__ == "__main__":
	classifier = pipeline('text-classification')
	listner = KafkaListener(support.bearer_token)
	listner.add_rules(tweepy.StreamRule(support.search_term1))
	listner.add_rules(tweepy.StreamRule(support.search_term2))
	listner.add_rules(tweepy.StreamRule(support.search_term3))
	listner.filter()
