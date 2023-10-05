import datetime

class transaction:
    transaction_history=[]
    def __init__(self,transaction_id,source_account,destination_account,amount: float):
        self.transaction_id=transaction_id
        self.source_account=source_account
        self.destination_account=destination_account
        self.amount=amount
    
        self.timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        transaction.transaction_history.append((self.amount,self.timestamp,self.source_account.account_number,self.destination_account.account_number))

    
    def get_transaction_details(self) -> str:
        transaction_details = f"Transaction ID: {self.transaction_id}\n"
        transaction_details += "Source Account:{self.source_account}\n"
        # transaction_details += f"  #Account Number: {self.source_account.Account.account_number}\n"
        # transaction_details += f"  #Customer Name: {self.source_account.customer.name}\n"
        transaction_details += f"Destination Account:{self.destination_account}\n"
        # transaction_details += f"  #Account Number: {self.destination_account.Account.account_number}\n"
        # transaction_details += f"  #Customer Name: {self.destination_account.customer.name}\n"
        transaction_details += f"Amount: ${self.amount:.2f}\n"
        transaction_details += f"Timestamp: {self.timestamp}"
        
    def get_transaction_history(account):
        t_history=[]
        for transactions in transaction.transaction_history:
            if account.account_number in transactions:
                t_history.append(transactions)
        return t_history