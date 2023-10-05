class customer:
    def __init__(self, customer_id, name,address,phone_number):
        self.customer_id=customer_id
        self.name=name
        self.address=address
        self.phone_number=phone_number
    
    def get_customer_info(self) -> str:
        customer_info = f"Customer ID: {self.customer_id}\nName: {self.name}\nAddress: {self.address}\nPhone Number: {self.phone_number}"
        print(customer_info)
        
# if __name__=='__main__':
#     obj=Customer('CZ07','Abhilipsa','Bbsr','7896430134')
#     obj.get_customer_info()