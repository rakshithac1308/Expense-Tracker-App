#Combining the features into Application
from features import search_by_date_linear,sort_amount,add_data,delete_data,sum_amount

#List of dictionary in variable transactions
transactions=[
    {"date":"2024-8-25","amount":500,"description":"Grapes"},
     {"date":"2024-8-22","amount":250,"description":"orange"},
     {"date":"2024-8-26","amount":60,"description":"apple"},
    {"date":"2024-8-28","amount":650,"description":"guva"},
    {"date":"2024-8-18","amount":2000,"description":"berry"},
]

falg = True
while falg:
  print("1.add")
  print("2.search")
  print("3.sort")
  print("4.remove")
  print("5.display")
  print("6.stop")
  print("7.Sum of Aomunt")
  choice=int(input("Enter the choice:"))
  if choice == 1:
    print("-"*50)
    print("Adding Data")
    print("-"*50)
    transactions=add_data(transations)
    print("-"*50)
  elif choice == 2:
    print("-"*50)
    print("Searching Data")
    print("-"*50)
    print(search_by_date_linear(transactions))
    print("-"*50)
  elif choice == 3:
    print("-"*50)
    print("Sorting Data")
    print("-"*50)
    transactions=sort_amount(transactions)
    print("-"*50)
  elif choice == 4:
    print("-"*50)
    print("Deleting Data")
    print("-"*50)
    transactions=delete_data(transactions)
    print("-"*50)
  elif choice == 5:
    print("-"*50)
    print("Displaying Transactions")
    print("-"*50)
    print(transactions)
    print("-"*50)
  elif choice == 6:
    print("-"*50)
    print("Exiting Application")
    flag=False
    print("-"*50)
  elif choice == 7:
    print("-"*50)
    print("Sum of amount of given year")
    print(sum_amount(transactions))
    print("-"*50)
  else:
    print("-"*50)
    print("Please enter the correct choice:")
    print("-"*50)
  
