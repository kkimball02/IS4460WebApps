import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
django.setup()

##Names were created in terminal
from customer.models import Customer, Order

customer_name= "Kyler Rae Kimball"
customer = Customer.objects.get(name=customer_name)
new_email = "kyler.kimball02@gmail.com"
customer.email = new_email
customer.save()

customer_name = "Johnson"
customer = Customer.objects.get(name=customer_name)
new_email = "johnsontheman@gmail.com"
customer.email = new_email
customer.save()

customer_name = "Bob"
customer = Customer.objects.get(name=customer_name)
new_email = "bobthebuilder@gmail.com"
customer.email = new_email
customer.save()

#Retrieving two customers
customers = Customer.objects.all()[:2]
orders_data = [
    {"total_price": 100.00, "total_items": 3, "order_date": "2024-02-26"},
    {"total_price": 75.50, "total_items": 2, "order_date": "2024-02-25"}
]

#populating orders
for customer in customers:
  for data in orders_data:
    Customer = customers[0]
    order = Order.objects.create(
    customer=customer,
    total_price=data["total_price"],
    total_items=data["total_items"],
    order_date=data["order_date"]
  )

