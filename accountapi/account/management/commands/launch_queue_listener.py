from django.core.management import BaseCommand

from account.kafkaconsumerconfiguration import TransactionListener


class Command(BaseCommand):
    help = 'Launches Listener for transaction_created message : Kafka'

    def handle(self, *args, **options):
        # thread instantiation
        td = TransactionListener()
        td.start()
        self.stdout.write("Started Consumer Thread")
