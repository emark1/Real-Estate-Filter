
class Purchase:
    def __init__(self, price, baths, beds, city, home_type):
        self.price = price
        self.baths = baths
        self.beds = beds
        self.city = city
        self.type = home_type

    @staticmethod
    def create_dict(lookup):
        return Purchase(
            float(lookup['price']),
            int(lookup['baths']),
            int(lookup['beds']),
            lookup['city'],
            lookup['type'],
        )