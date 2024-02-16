import socket

from confluent_kafka import Producer


def kafka_configure():
    #KAFKA_ADVERTISED_HOST_NAME: kafka
    conf = {'bootstrap.servers': 'kafka:9092',
            'client.id': socket.gethostname()}

    return Producer(conf)


def acked(err, msg):
    if err is not None:
        print("Failed to deliver message: %s: %s" % (str(msg), str(err)))
    else:
        print("Message produced: %s" % (str(msg)))
