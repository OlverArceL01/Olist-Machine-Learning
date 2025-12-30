from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class InputPaths:
    orders: Path
    order_items: Path
    products: Path
    customers: Path
    product_category_name_translation: Path