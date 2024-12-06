
class Camera:
    def __init__(self, resolution):
        self.resolution = resolution
    
    def take_photo(self):
        """Simulate taking a photo."""
        print(f"Taking a photo with {self.resolution} MP resolution.")


class Phone:
    def __init__(self, brand):
        self.brand = brand
    
    def make_call(self, number):
        """Simulate making a phone call."""
        print(f"Calling {number} from a {self.brand} phone.")


class Smartphone(Camera, Phone):
    def __init__(self, brand, resolution):
        Camera.__init__(self, resolution)
        Phone.__init__(self, brand)
    
    def browse_internet(self):
        """Simulate browsing the internet."""
        print("Browsing the internet.")


smartphone = Smartphone(brand="XYZ", resolution=12)


smartphone.take_photo()        
smartphone.make_call("123456789")  
smartphone.browse_internet()   
