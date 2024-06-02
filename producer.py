import pandas as pd
from kafka import KafkaProducer
import time
import json

producer = KafkaProducer(bootstrap_servers=['18.232.136.147:9092'],
                        value_serializer=lambda x: json.dumps(x).encode('utf-8'))

producer.send('demo_test',value="{'hello':'world'}")
print("Sent")
time.sleep(2)