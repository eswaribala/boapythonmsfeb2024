from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

from transaction.models import Transaction


@registry.register_document()
class TransactionDocument(Document):

    class Index:
        name = "boa_transactions_2024"
        settings = {
            "number_of_shards": 1,
            "number_of_replicas": 0,
        }

    class Django:
        model = Transaction
        fields = [
            "transactionId",
            "amount",
            "dot"
        ]


