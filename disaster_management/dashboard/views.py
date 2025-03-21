from django.shortcuts import render

def index(request):
    context = {
        'user': request.user,
        'notifications': [
            {'user': 'Josephine Thompson', 'message': 'commented on admin panel'},
            {'user': 'Donoghue Susan', 'message': 'Hi, How are you?'},
        ],
        'total_orders': 13647,
        'order_change': 2.3,
        'recent_orders': [
            {'id': 'RB5625', 'date': '2024-04-29', 'product': {'image': '/static/images/products/product-1(1).png', 'name': 'Product 1'}, 'customer_name': 'Anna M. Hines', 'email': 'anna.hines@mail.com', 'phone': '(+1)-555-1564-261', 'address': 'Burr Ridge/Illinois', 'payment_type': 'Credit Card', 'status': 'Completed'},
        ],
    }
    return render(request, 'index.html', context)

#invoices view
def invoice(request):
    return render(request,'invoice.html')