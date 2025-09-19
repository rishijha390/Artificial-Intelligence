def fetch_sales():
    return [
        {"id":1 , "status":"delivered"},
        {"id":2 , "status":"fake"},
        {"id":3 , "status":"delivered"}
    ]

def filter_valid_orders(sales):
    return [order for order in sales if order["status"] == "delivered"]

def summarize_data(valid_orders):
    return{
        "total orders": len(valid_orders),
        "delivered": len(valid_orders)
    }

def generate_report():
    sales = fetch_sales()
    valid_orders = filter_valid_orders(sales)
    summary = summarize_data(valid_orders)
    print("Monthly Report:",summary)

generate_report()