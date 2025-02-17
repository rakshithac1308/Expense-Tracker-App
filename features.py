#Fetching input from the user
def add_data(transactions):
  date = input("Enter the date:")
  amount = int(input("Enter the amount:"))
  description = input("Enter the description:")
  transaction = {"date":date,"amount":amount,"description":description}
  transactions.append(transaction)
  return transactions

#Using Linear Search to find transactions based on dates
def search_by_date_linear(transactions):
  date=input("Enter search date:")
  for transaction in transactions:
    if transaction["date"] == date:
      return transaction
  return "Transaction not found."

#Sorting Transaction based on amount with bubble sort
def sort_amount(transactions):
  for i in range(len(transactions)):
    for j in range(0,len(transactions)-1):
      if transactions[j]['amount']> transactions[j+1]["amount"]:
        transactions[j],transactions[j+1] = transactions[j+1],transactions[j]
  return transactions

#Delete data from list
def delete_data(transactions):
  date=input("Enter serach date: ")
  for transaction in transactions:
    if transaction["date"]==date:
      transactions.remove(transaction)
  return transactions

def sum_amount(transactions):
  s=0
  year=input("Enter the year:")
  for dict in transactions:
    if dict['date'][0:4] == year:
      s+=dict['amount']
  return s


