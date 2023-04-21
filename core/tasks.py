import random
from config.celery import app
from core.models import Supplier


@app.task
def add_or_subtract_random_numbers_from_debt(start, stop):
    """Adds and subtracts random numbers from supplier debts"""
    for supplier in Supplier.objects.all():
        if supplier.provider is not None:
            add_random_number_to_the_debt = supplier.debt_to_the_supplier + random.randint(start, stop)
            supplier.debt_to_the_supplier = add_random_number_to_the_debt
            supplier.save()