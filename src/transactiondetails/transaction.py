class transaction:
    def __init__(self,transaction_id,source_account,destination_account,amount: float):
        self.transaction_id=transaction_id
        self.source_account=source_account
        self.destination_account=destination_account
        self.amount=amount
        import datetime
        self.timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
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
    transaction_history=[]
    for transactions in transaction:
        if transactions.source_account == account_number or transactions.destination_account == account:
            transaction_history.append(transactions.get_transaction_details())
    return transaction_history