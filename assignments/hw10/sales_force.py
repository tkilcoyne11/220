"""
Tucker Kilcoyne
sales_force.py
"""

from sales_person import SalesPerson


class SalesForce:
    """
    This class creates a group of sales people
    """

    def __init__(self):
        self.sales_people = []

    def add_data(self, file_name):
        file = open(file_name, "r")
        for i in file.readline():
            variables = i.split(",")
            employee = SalesPerson(int(variables[0]), variables[1])
            for j in variables[2].split():
                employee.enter_sale(float(j))
            self.sales_people.append(employee)

    def quota_report(self, quota):
        report = []
        for employee in self.sales_people:
            data = [employee.get_id(), employee.get_name(),
                    employee.total_sales, employee.met_quota(quota)]
            report.append(data)
        return report

    def top_seller(self):
        top_seller = []
        for i in range(len(self.sales_people)):
            for j in range(i+1, len(self.sales_people)):
                if self.sales_people[j].compare_to(self.sales_people[i]) > 0:
                    self.sales_people[i], self.sales_people[j] = \
                        self.sales_people[j], self.sales_people[i]
        top_seller.append(self.sales_people[0])
        for i in range(1, len(self.sales_people)):
            if self.sales_people[i] >= top_seller[0].total_sales():
                top_seller.append(self.sales_people[i])
            else:
                break
        return top_seller

    def individual_sales(self, employee_id):
        for i in range(len(self.sales_people)):
            if self.sales_people[i] == employee_id:
                return self.sales_people[i]
        return None
