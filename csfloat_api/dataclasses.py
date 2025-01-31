from dataclasses import dataclass
from datetime import datetime
from typing import Dict, Any, List


@dataclass
class Sticker:
    name: str
    market_hash_name: str
    price: float


@dataclass
class Listing:
    id: str
    created_at: datetime
    price: int
    min_offer_price: int
    type: str
    market_hash_name: str
    float_value: float
    stickers: List[Sticker]
    paint_seed: int
    pattern_index: int

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Listing":
        stickers = []
        stickers_data = data.get('stickers', [])
        for sticker_data in stickers_data:
            sticker = Sticker(
                name=sticker_data.get("name", "Unknown"),
                market_hash_name=sticker_data.get("market_hash_name"),
                price=sticker_data.get("price", 0)
            )
            stickers.append(sticker)

        return cls(
            id=data["id"],
            created_at=datetime.fromisoformat(data["created_at"].replace("Z", "+00:00")),
            price=data["price"],
            min_offer_price=data.get("min_offer_price", 0),
            type=data["type"],
            market_hash_name=data["item"]["market_hash_name"],
            float_value=data["item"].get("float_value", 0),
            stickers=stickers,
            paint_seed=data["item"].get("paint_seed", 0),
            pattern_index=data["item"].get("pattern_index", 0)
        )
