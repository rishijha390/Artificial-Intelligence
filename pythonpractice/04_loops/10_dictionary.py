users  = [
    {"id":1 , "total":100 , "coupon": "P10"},
    {"id":2 , "total":150 , "coupon": "R30"},
    {"id":3 , "total":250 , "coupon": "T30"},
]

discounts = {
    "P10": (0.2,0),
    "R30": (0.5,0),
    "T30": (0,10),
}

for user in users:
    percent , fixed = discounts.get(user["coupon"],(0,0))
    discount = user["total"] * percent + fixed
    print(f"{user["id"]} paid {user["total"]} and got discount for next visit of rupees {discount}")