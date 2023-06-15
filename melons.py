"""Classes for melon orders."""
import random
import datetime

class AbstractMelonOrder:
    """An abstract base class that the other Melon Orders inherit from"""

    def __init__(self, species, qty):
        """Initialize melon order attributes"""
       
        self.species = species
        self.qty = qty
        self.shipped = False


    def get_base_price(self):
        """Calculate the base price"""

        base_price = random.randrange(5,10)
        now = datetime.datetime.now()
        
        if now.weekday() in range(0, 5) and now.hour in range(8, 12):
            base_price += 4

        return base_price


    def get_total(self):
        """Calculate price, including tax."""

        base_price = self.get_base_price()

        if self.species == "christmas":
            base_price = base_price * 1.5

        total = (1 + self.tax) * self.qty * base_price
            
        if self.order_type == "international" and self.qty < 10: 
            total += 3


        return total
    
    ### Another way to write it: ###
        # def get_total(self):
        # """Calculate price, including tax."""

        # base_price = self.get_base_price()
        
        # if self.species == "christmas":
        #     base_price = base_price * 1.5
            
        # if self.order_type == "International" and self.qty < 10:
        #     total = (1 + self.tax) * self.qty * base_price + 3
        # else:
        #     total = (1 + self.tax) * self.qty * base_price

        # return total


    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    order_type = "domestic"
    tax = .08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"
    tax = 0.17

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super().__init__(species, qty)
        self.country_code = country_code


    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class GovernmentMelonOrder(AbstractMelonOrder):
    """A government melon order"""

    order_type = "government"
    tax = 0

    def __init__(self, species, qty):
        super().__init__(species, qty)
        self.passed_inspection = False
        
    
    def mark_inspection(self, passed):
        """Record whether a melon has passed inspection"""

        self.passed_inspection = passed 
