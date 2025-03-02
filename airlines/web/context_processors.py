import logging
from django.http import HttpRequest
from django.utils import timezone

logger = logging.getLogger(__name__)


def common_context(request: HttpRequest) -> dict:

    context = dict(
        current_year=timezone.now().year,
    )

    logger.info(f"Common context: {context}")
    return context
