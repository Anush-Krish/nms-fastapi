from kafka import KafkaConsumer
import json
import time
import random
from app.api.endpoints.users import notifications_store

consumer = KafkaConsumer(
    'notifications',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

MAX_RETRIES = 3

def process_notification(data):
    success = random.choice([True, False])
    return success

for message in consumer:
    data = message.value
    retries = 0
    while retries < MAX_RETRIES:
        if process_notification(data):
            user_id = data["user_id"]
            notifications_store.setdefault(user_id, []).append({
                "type": data["type"],
                "message": data["message"]
            })
            break
        retries += 1
        time.sleep(2 ** retries)  # exponential backoff
