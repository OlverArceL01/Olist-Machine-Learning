from pathlib import Path
from dataclasses import dataclass

@dataclass(frozen=True)
class OutputPaths:
    orders: Path
    order_items: Path
    products: Path
    customers: Path
    product_category_name_translation: Path
