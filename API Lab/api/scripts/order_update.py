import requests
import json


id = 1
api_url = f'http://localhost:8000/api/order/{id}/'

customer_id = '2'
order_data = {'id': 1, 'customer': customer_id,
                 'total_amount': '200.96',
                 'date_created': '2024-03-21'
                 }
try:
    response = requests.put(api_url, data=json.dumps(order_data), headers={'Content-Type':'application/json'})
    response.raise_for_status()
    if response.status_code==200:
        print('Order updated successfully.')
    else:
        print(f'Error updating Order')

except Exception as e:
    print('An error occured:', e)