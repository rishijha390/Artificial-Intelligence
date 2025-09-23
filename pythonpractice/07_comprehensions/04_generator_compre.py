daily_sales = [3 , 5 ,7,8,44,55,33]

total_cups = sum(sale for sale in daily_sales if sale > 5)

print(total_cups)