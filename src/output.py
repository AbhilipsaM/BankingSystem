from CustomerDetails.customer import customer
from AccountDetails.Account import Account
from transactiondetails.transaction import transaction


    
if __name__=='__main__':
    # Create customers
    customer1 =customer("C001", "John Doe", "123 Main St", "555-1234")
    customer2 =customer("C002", "Jane Smith", "456 Elm St", "555-5678")
    customer1.get_customer_info()
    customer2.get_customer_info()


    # Create accounts for customers
    john_savings =Account("S001", customer1)
    john_checking =Account("C001", customer1)
    jane_savings =Account("S002", customer2)
    jane_checking =Account("C002", customer2)

    # Deposit $1000 into John Doe's Savings Account
    john_savings.deposit(1000.0)

    # Withdraw $200 from Jane Smith's Checking Account
    jane_checking.withdraw(200.0)

    # Perform a transfer of $300 from John Doe's Checking Account to Jane Smith's Savings Account
    if john_checking.withdraw(300)==True:
        jane_savings.deposit(300)
    else:
        print("Insufficient balance!!The Transfer cannot be done")


   
    # # Retrieve and display the balance of all four accounts
    # print(f"John Doe's Savings Account Balance: ${john_savings.balance}")
    # print(f"John Doe's Checking Account Balance: ${john_checking.balance}")
    # print(f"Jane Smith's Savings Account Balance: ${jane_savings.balance}")
    # print(f"Jane Smith's Checking Account Balance: ${jane_checking.balance}")

    # Retrieve and display balances
    print("------------Balances------------")
    print(f"John Doe's Savings Account Balance: ${john_savings.get_balance()}")
    print(f"John Doe's Checking Account Balance: ${john_checking.get_balance()}")
    print(f"Jane Smith's Savings Account Balance: ${jane_savings.get_balance()}")
    print(f"Jane Smith's Checking Account Balance: ${jane_checking.get_balance()}")

    # Retrieve and display the balance of all four accounts
    print("Balance in John Doe's Savings Account $",john_savings.balance)
    print("Balance in John Doe's Checking Account $",john_checking.balance)
    print("Balance in Jane Smith's Savings Account $",jane_savings.balance)
    print("Balance in Jane Smith's Checking Account $",jane_checking.balance)

    # Create transaction objects
    transactions1= [
    transaction("T001", john_savings, None, 1000),
    transaction("T002", None, jane_checking, 200),
    transaction("T003", john_checking, jane_savings, 300)]


    # Display transaction details
    print("\nTransaction Details:")
    for transactions in transactions1:
        print(transactions.get_transaction_details())
        print("details")
        

    # Display transaction history for Jane Smith's Savings Account
    print("\nTransaction History for Jane Smith's Savings Account:")
    jane_savings_history= transactions.get_transaction_history(jane_savings_account)
    for transaction_details in jane_savings_history:
        print(transaction_details)





