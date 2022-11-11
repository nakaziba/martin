class ServiceProvider:
    email="photogenics@gmail.com"
    discount=0.20
    def __init__(self,name,phone):
        self.__name=name
        self.__phone=phone
    def get_name(self):
        return self.__name
    @classmethod
    def issuing_invoices(cls):
        return "here is the invoice"
serv_1=ServiceProvider("photogenics",750740057)
serv_2=ServiceProvider("claire",772309040)        
serv_1.discount=0.20
print(serv_1.discount)
print(serv_2.discount)

# updating email details.

ServiceProvider.email="claireanne@gmail.com"

print(serv_1.email)
        