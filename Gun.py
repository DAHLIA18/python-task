class Gun:
    def __init__(self):
        self.is_loaded = None
        self.ammo_count = None

    def _init_(self, model, caliber, capacity, is_loaded=False):
        self.model = model
        self.caliber = caliber
        self.capacity = capacity
        self.is_loaded = is_loaded
        self.ammo_count = 0

    def load(self, ammo_count):
        if ammo_count <= self.capacity:
            self.ammo_count = ammo_count
            self.is_loaded = True
            print(f"{self.model} loaded with {ammo_count} rounds.")
        else:
            print(f"Cannot load {ammo_count} rounds. Capacity exceeded.")

    def fire(self):
        if self.is_loaded and self.ammo_count > 0:
            print(f"{self.model} fires.")
            self.ammo_count -= 1
            if self.ammo_count == 0:
                self.is_loaded = False
                print("Gun is empty.")
        else:
            print("Gun is not loaded or out of ammo.")
