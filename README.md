# Real-Time stock-market data pipeline using kafka and ASW(EC2, s3, Athena, Glue)

ssh -i "kafka-stock-market-2.pem" ec2-user@ec2-3-90-250-35.compute-1.amazonaws.com

## Installations
wget https://downloads.apache.org/kafka/3.7.0/kafka-3.7.0-src.tgz
<br>
tar -xvf kafka-3.7.0-src.tgz

sudo yum install java-1.8.0-openjdk

## Change public ip
Allow all traffic from all on aws ec2 instance.

sudo nano config/server.properties 
<br>
(change ADVERTISED_LISTENERS to public ip of the EC2 instance)

## Zookeeper
bin/zookeeper-server-start.sh config/zookeeper.properties

## Kafka Server
export KAFKA_HEAP_OPTS="-Xmx256M -Xms128M"
<br>
bin/kafka-server-start.sh config/server.properties

## Create Topic
cd kafka_2.12-3.3.1
<br>
bin/kafka-topics.sh --create --topic demo_testing2 --bootstrap-server {Put the Public IP of your EC2 Instance:9092} --replication-factor 1 --partitions 1
<br>
**Check topic:-**
<br>
bin/kafka-topics.sh --bootstrap-server <broker-ip>:9092 --list

## producer-comsumer
bin/kafka-console-producer.sh --topic demo_test --bootstrap-server 3.90.250.35:9092
<br>
bin/kafka-console-consumer.sh --topic demo_test --bootstrap-server 3.90.250.35:9092

## Images

![image](https://github.com/Viditnegi/kafka-stock-market/assets/106267998/bc89c2d9-e8e2-4324-99eb-fced8df154d2)

![image](https://github.com/Viditnegi/kafka-stock-market/assets/106267998/04893fe2-a2d6-4e63-ab7c-18902aa4f900)

![image](https://github.com/Viditnegi/kafka-stock-market/assets/106267998/768e349b-82a8-4896-a8e8-b3070f35dd1c)





