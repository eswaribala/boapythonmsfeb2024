from django.core.management import BaseCommand

from account.kafkaconsumerconfiguration import TransactionListener


class Command(BaseCommand):
    help = 'Launches Listener for user_created message : Kafka'

    def handle(self, *args, **options):
        td = TransactionListener()
        td.start()
        self.stdout.write("Started Consumer Thread")
