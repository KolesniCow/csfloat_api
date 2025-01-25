from dataclasses import dataclass
from datetime import datetime
from typing import Dict, Any

@dataclass
class Listing:
    id: str
    created_at: datetime
    price: int
    min_offer_price: int
    type: str
    market_hash_name: str  # Новое поле для названия предмета

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Listing":
        return cls(
            id=data["id"],
            created_at=datetime.fromisoformat(data["created_at"].replace("Z", "+00:00")),
            price=data["price"],
            min_offer_price=data.get("min_offer_price", 0),
            type=data["type"],
            market_hash_name=data["item"]["market_hash_name"],  # Достаем название из item
        )
