# kafka-stock-market

ssh -i "kafka-stock-market-2.pem" ec2-user@ec2-3-90-250-35.compute-1.amazonaws.com

bin/zookeeper-server-start.sh config/zookeeper.properties

export KAFKA_HEAP_OPTS="-Xmx256M -Xms128M"
bin/kafka-server-start.sh config/server.properties


bin/kafka-console-producer.sh --topic demo_test --bootstrap-server 3.90.250.35:9092
bin/kafka-console-consumer.sh --topic demo_test --bootstrap-server 3.90.250.35:9092
