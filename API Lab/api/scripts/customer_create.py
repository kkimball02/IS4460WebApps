import requests
import json
api_url = 'http://localhost:8000/api/customer/'

customer_data = {'name': 'Wells Fargo',
                 'email': 'wfarg0@gmail.com',
                 'phone_number': '8019998888'}

response = requests.post(api_url, data=json.dumps(customer_data), headers={'Content-Type':'application/json'})

if response.status_code==201:
    print('Customers created successfully.')
else:
    print(f'Error creating customers')