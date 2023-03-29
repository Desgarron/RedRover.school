# 5.1. Создайте любой класс с произвольным количеством подклассов, экземпляров, атрибутов и методов
#     - как минимум один атрибут должен быть с уровнем доступа private. Соответственно, для получания
#     значений этого атрибута нужно использовать методы get и set.


class Company:

    def __init__(self, name, qty_workers, revenue, office_location,
                 company_type, business):
        self._name = name
        self.qty_workers = qty_workers
        self.__revenue = revenue
        self._office_location = office_location
        self.company_type = company_type
        self.business = business

    def get_company_name(self):
        return f'Company name is {self._name}'

    def set_company_name(self, new_company_name):
        self._name = new_company_name

    def get_company_revenue(self):
        return f'Company {self._name} revenue is {self.__revenue}'

    def set_company_revenue(self, new_company_revenue):
        self.__revenue = new_company_revenue

    def get_company_location(self):
        return f'Company office location is {self._office_location}'

    def set_company_location(self, new_company_loction):
        self._office_location = new_company_loction


class Logistic(Company):

    def __init__(self, name, qty_workers, revenue, office_location,
                 company_type, business, qty_trucks, countries_of_working):

        super().__init__(name, qty_workers, revenue, office_location,
                         company_type, business)
        self.qty_trucks = qty_trucks
        self.countries_of_working = countries_of_working

    def get_qty_trucks(self):
        return f'In company {self._name} are {self.qty_trucks} trucks'

    def set_qty_trucks(self, new_qty):
        self.qty_trucks = new_qty
