"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""


class Employee:
    def __init__(self, name, contract_type, contract_value, commission_type=None, commission_value=None):
        self.name = name
        self.contract_type = contract_type
        self.contract_value = contract_value
        self.commission_type = commission_type
        self.commission_value = commission_value

    def get_pay(self):
        if self.contract_type == 'hourly':
            pay = self.contract_value[0] * self.contract_value[1]
        else:
            pay = self.contract_value

        if self.commission_type == 'bonus':
            pay += self.commission_value
        elif self.commission_type == 'contract':
            pay += self.commission_value[0] * self.commission_value[1]

        return pay

    def __str__(self):
        if self.contract_type == 'hourly':
            contract_str = f"{self.name} works on a contract of {self.contract_value[1]} hours at {self.contract_value[0]}/hour"
        else:
            contract_str = f"{self.name} works on a monthly salary of {self.contract_value}"

        if self.commission_type == 'bonus':
            commission_str = f" and receives a bonus commission of {self.commission_value}"
        elif self.commission_type == 'contract':
            commission_str = f" and receives a commission for {self.commission_value[1]} contract(s) at {self.commission_value[0]}/contract"
        else:
            commission_str = ""

        return f"{contract_str}{commission_str}. Their total pay is {self.get_pay()}."


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', 'salary', 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', 'hourly', (25, 100))

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', 'salary', 3000, 'contract', (200, 4))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', 'hourly', (25, 150), 'contract', (220, 3))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', 'salary', 2000, 'bonus', 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', 'hourly', (30, 120), 'bonus', 600)
