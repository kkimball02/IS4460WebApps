import requests
import json

id = 1

api_url = f'http://localhost:8000/api/customer/{id}/'

customer_data = {'name': 'Wells Fargo',
                 'email': 'wellsfarg0@gmail.com',
                 'phone_number': '8019998897'}

response = requests.put(api_url, data=json.dumps(customer_data), headers={'Content-Type':'application/json'})

if response.status_code==200:
    print('Customers updated successfully')
else:
    print('Error updating customers')
    


