"""Celery tasks."""

import celery


@celery.shared_task
def somar(a, b):
    """Soma 2 números de forma assíncrona."""
    return a + b
