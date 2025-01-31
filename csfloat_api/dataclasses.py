from dataclasses import dataclass
from datetime import datetime
from typing import Dict, Any, List, Optional

@dataclass
class Sticker:
    sticker_id: int
    slot: int
    icon_url: str
    name: str
    scm_price: Optional[int]
    scm_volume: Optional[int]

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Sticker":
        return cls(
            sticker_id=data.get("stickerId"),
            slot=data.get("slot"),
            icon_url=data.get("icon_url"),
            name=data.get("name"),
            scm_price=data.get("scm", {}).get("price"),
            scm_volume=data.get("scm", {}).get("volume")
        )

@dataclass
class Seller:
    avatar: str
    flags: int
    online: bool
    stall_public: bool
    steam_id: str
    username: str
    median_trade_time: Optional[int]
    total_failed_trades: Optional[int]
    total_trades: Optional[int]
    total_verified_trades: Optional[int]

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Seller":
        stats = data.get("statistics", {})
        return cls(
            avatar=data.get("avatar"),
            flags=data.get("flags"),
            online=data.get("online"),
            stall_public=data.get("stall_public"),
            steam_id=data.get("steam_id"),
            username=data.get("username"),
            median_trade_time=stats.get("median_trade_time"),
            total_failed_trades=stats.get("total_failed_trades"),
            total_trades=stats.get("total_trades"),
            total_verified_trades=stats.get("total_verified_trades")
        )

@dataclass
class Item:
    asset_id: str
    def_index: int
    paint_index: int
    paint_seed: int
    float_value: float
    icon_url: str
    d_param: str
    is_stattrak: bool
    is_souvenir: bool
    rarity: int
    quality: int
    market_hash_name: str
    stickers: List[Sticker]
    tradable: int
    inspect_link: str
    has_screenshot: bool
    scm_price: Optional[int]
    scm_volume: Optional[int]
    item_name: str
    wear_name: str
    description: str
    collection: str
    badges: List[str]

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Item":
        scm = data.get("scm", {})
        return cls(
            asset_id=data.get("asset_id"),
            def_index=data.get("def_index"),
            paint_index=data.get("paint_index"),
            paint_seed=data.get("paint_seed"),
            float_value=data.get("float_value"),
            icon_url=data.get("icon_url"),
            d_param=data.get("d_param"),
            is_stattrak=data.get("is_stattrak"),
            is_souvenir=data.get("is_souvenir"),
            rarity=data.get("rarity"),
            quality=data.get("quality"),
            market_hash_name=data.get("market_hash_name"),
            stickers=[Sticker.from_dict(s) for s in data.get("stickers", [])],
            tradable=data.get("tradable"),
            inspect_link=data.get("inspect_link"),
            has_screenshot=data.get("has_screenshot"),
            scm_price=scm.get("price"),
            scm_volume=scm.get("volume"),
            item_name=data.get("item_name"),
            wear_name=data.get("wear_name"),
            description=data.get("description"),
            collection=data.get("collection"),
            badges=data.get("badges", [])
        )

@dataclass
class Listing:
    id: str
    created_at: datetime
    type: str
    price: int
    state: str
    seller: Seller
    item: Item
    is_seller: bool
    min_offer_price: int
    max_offer_discount: int
    is_watchlisted: bool
    watchers: int

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Listing":
        return cls(
            id=data.get("id"),
            created_at=datetime.fromisoformat(data.get("created_at").replace("Z", "+00:00")),
            type=data.get("type"),
            price=data.get("price"),
            state=data.get("state"),
            seller=Seller.from_dict(data.get("seller", {})),
            item=Item.from_dict(data.get("item", {})),
            is_seller=data.get("is_seller"),
            min_offer_price=data.get("min_offer_price"),
            max_offer_discount=data.get("max_offer_discount"),
            is_watchlisted=data.get("is_watchlisted"),
            watchers=data.get("watchers")
        )
