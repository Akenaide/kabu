from typing import Optional
from django_countries.fields import Country

from shops import models


def make_shop(
    name: str = "Test Shop",
    address: str = "Test Address",
    country: Optional[Country] = None,
    is_active: bool = True,
) -> models.Shop:
    """
    Factory for creating Shop instances with sensible defaults.

    Args:
        name: Shop name (default: "Test Shop")
        address: Shop address (default: "Test Address")
        country: Country as Country object or code (default: France/"FR")
        is_active: Whether shop is active (default: True)

    Returns:
        Created Shop instance
    """
    if country is None:
        country = Country("FR")  # Default to France

    return models.Shop.objects.create(
        name=name,
        address=address,
        country=country,
        is_active=is_active,
    )
