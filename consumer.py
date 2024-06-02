import pandas as pd
from kafka import KafkaConsumer
import time
import json

consumer = KafkaConsumer(bootstrap_servers=['18.232.136.147:9092'],
                        value_deserializer=lambda x: json.loads(x.decode('utf-8')))

for c in consumer:
    print(c.value)