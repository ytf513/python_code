class Car(object):
    """
    Car class define.
    """

    wheel = 4

    def __init__(self, wheels, miles, make, model, year, sold_on):
        """Return a new Car object."""
        self.wheels = wheels
        self.miles = miles
        self.make = make
        self.model = model
        self.year = year
        self.sold_on = sold_on
        
    def sale_price(self):
        """Return the sale price for this car as a float amount."""
        if self.sold_on is not None:
            return 0.0  # Already sold
        return 5000.0 * self.wheels

    def purchase_price(self):
        """Return the price for which we would pay to purchase the car."""
        if self.sold_on is None:
            return 0.0  # Not yet sold
        return 8000 - (.10 * self.miles)

mustang = Car(4,5,6,7,8,8)
print mustang.wheels
# 4
print Car.wheel
# 4

print mustang.sale_price()
print mustang.purchase_price()
print Car.__doc__
print list.__doc__
