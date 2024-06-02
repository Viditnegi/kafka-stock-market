# kafka-stock-market

ssh -i "kafka-stock-market-2.pem" ec2-user@ec2-3-90-250-35.compute-1.amazonaws.com

## Installations
wget https://downloads.apache.org/kafka/3.7.0/kafka-3.7.0-src.tgz
tar -xvf kafka-3.7.0-src.tgz

sudo yum install java-1.8.0-openjdk

## Change public ip
Allow all traffic from all on aws ec2 instance.

sudo nano config/server.properties 
(change ADVERTISED_LISTENERS to public ip of the EC2 instance)

## Zookeeper
bin/zookeeper-server-start.sh config/zookeeper.properties

## Kafka Server
export KAFKA_HEAP_OPTS="-Xmx256M -Xms128M"
bin/kafka-server-start.sh config/server.properties

## producer-comsumer
bin/kafka-console-producer.sh --topic demo_test --bootstrap-server 3.90.250.35:9092
<br>
bin/kafka-console-consumer.sh --topic demo_test --bootstrap-server 3.90.250.35:9092
