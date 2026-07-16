from core.infra.database.models.item import Item


def create_item_models(
    import_id: int,
    valid_records: list[dict],
) -> list[Item]:

    items = []

    for record in valid_records:

        items.append(
            Item(
                import_id=import_id,
                product_data=record,
                enrich_data=None,
                status="PENDING",
                review_status=False,
                comment=None,
            )
        )

    return items