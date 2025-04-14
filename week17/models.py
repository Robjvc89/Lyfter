# models.py

class Category:
    def __init__(self, name: str):
        self.name = name.strip()

    def is_valid(self):
        return bool(self.name)


class Transaction:
    def __init__(self, trans_type: str, title: str, amount: float, category: str):
        self.type = trans_type
        self.title = title.strip()
        self.amount = amount
        self.category = category.strip()

    def is_valid(self):
        return (
            self.type in ['income', 'expense']
            and self.title
            and self.category
            and isinstance(self.amount, (int, float))
            and self.amount > 0
        )

    def to_dict(self):
        return {
            "type": self.type,
            "title": self.title,
            "amount": self.amount,
            "category": self.category
        }

    @staticmethod
    def from_dict(data):
        return Transaction(
            data["type"],
            data["title"],
            data["amount"],
            data["category"]
        )

