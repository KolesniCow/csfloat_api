from enum import Enum

class SortBy(str, Enum):
    LOWEST_PRICE = "lowest_price"
    HIGHEST_PRICE = "highest_price"
    MOST_RECENT = "most_recent"
    EXPIRES_SOON = "expires_soon"
    LOWEST_FLOAT = "lowest_float"
    HIGHEST_FLOAT = "highest_float"
    BEST_DEAL = "best_deal"
    HIGHEST_DISCOUNT = "highest_discount"
    FLOAT_RANK = "float_rank"
    NUM_BIDS = "num_bids"


class Category(int, Enum):
    ANY = 0
    NORMAL = 1
    STATTRAK = 2
    SOUVENIR = 3
