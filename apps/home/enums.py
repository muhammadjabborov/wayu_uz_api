from django.db.models import TextChoices


class PaymentTypeChoose(TextChoices):
    PAYME = ('payme', 'Payme')
    CLICK = ('click', 'Click')
    OSON = ('oson', 'Oson')
