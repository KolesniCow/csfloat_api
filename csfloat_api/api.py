import requests
from typing import List, Optional
from csfloat_api.dataclasses import Listing
from csfloat_api.enums import SortBy, Category


class CSFloatAPI:
    BASE_URL = "https://csfloat.com/api/v1"

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.headers = {"Authorization": api_key}

    def get_listings(
            self,
            page: int = 0,
            limit: int = 50,
            sort_by: SortBy = SortBy.BEST_DEAL,
            category: Category = Category.ANY,
            def_index: Optional[List[int]] = None,
            min_float: Optional[float] = None,
            max_float: Optional[float] = None,
            rarity: Optional[int] = None,
            paint_seed: Optional[int] = None,
            paint_index: Optional[int] = None,
            user_id: Optional[str] = None,
            collection: Optional[str] = None,
            min_price: Optional[int] = None,
            max_price: Optional[int] = None,
            market_hash_name: Optional[str] = None,
            item_type: Optional[str] = None,
            stickers: Optional[str] = None,
    ) -> List[Listing]:
        """
        Получение всех активных объявлений на CSFloat Market.

        :return: Список объектов Listing.
        """
        params = {
            "page": page,
            "limit": limit,
            "sort_by": sort_by.value,
            "category": category.value,
            "def_index": ",".join(map(str, def_index)) if def_index else None,
            "min_float": min_float,
            "max_float": max_float,
            "rarity": rarity,
            "paint_seed": paint_seed,
            "paint_index": paint_index,
            "user_id": user_id,
            "collection": collection,
            "min_price": min_price,
            "max_price": max_price,
            "market_hash_name": market_hash_name,
            "type": item_type,
            "stickers": stickers,
        }
        response = requests.get(
            f"{self.BASE_URL}/listings",
            headers=self.headers,
            params={k: v for k, v in params.items() if v is not None},
        )
        response.raise_for_status()
        data = response.json()['data']

        # Проверяем, что ответ является списком
        if not isinstance(data, list):
            raise ValueError(f"Unexpected response format: {data}")

        return [Listing.from_dict(item) for item in data]

