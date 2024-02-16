import os
import sys
import threading

from confluent_kafka import KafkaError, KafkaException, Consumer
from dotenv import load_dotenv

load_dotenv()
running = True


def basic_consume_loop(consumer):
    try:
        # consumer.subscribe(topics)

        while running:
            msg = consumer.poll(timeout=1.0)
            if msg is None: continue

            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    # End of partition event
                    sys.stderr.write('%% %s [%d] reached end at offset %d\n' %
                                     (msg.topic(), msg.partition(), msg.offset()))
                elif msg.error():
                    raise KafkaException(msg.error())
            else:
                print(msg.value().decode('utf8'))
    finally:
        # Close down consumer to commit final offsets.
        consumer.close()


def shutdown():
    running = False


def commit_completed(err, partitions):
    if err:
        print(str(err))
    else:
        print("Committed partition offsets: " + str(partitions))


class TransactionListener(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        # Create consumer
        # kafka:9092 - > kafka is advertised host name
        conf = {'bootstrap.servers': 'kafka:9092',
                'group.id': 'transaction',
                'default.topic.config': {'auto.offset.reset': 'smallest'},
                'on_commit': commit_completed}
        self.consumer = Consumer(conf)

    def run(self):
        print('Inside Service :  Created Listener ')
        try:
            # Subcribe to topic
            topic = os.getenv("topic")
            print(topic)
            self.consumer.subscribe([topic])
            basic_consume_loop(self.consumer)

        finally:
            # Close down consumer to commit final offsets.
            self.consumer.close()