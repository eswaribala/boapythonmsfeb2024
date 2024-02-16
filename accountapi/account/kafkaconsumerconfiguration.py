import sys

from confluent_kafka import KafkaError, KafkaException
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
