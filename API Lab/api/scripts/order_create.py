import requests
import json



api_url = 'http://localhost:8000/api/order/'

customer_id = '2'
order_data = {'id': 1, 'customer': customer_id,
                 'total_amount': '124.96',
                 'date_created': '2024-03-20'
                 }
try:
    response = requests.post(api_url, data=json.dumps(order_data), headers={'Content-Type':'application/json'})
    response.raise_for_status()
    if response.status_code==201:
        print('Order created successfully.')
    else:
        print(f'Error creating Order')

except Exception as e:
    print('An error occured:', e)