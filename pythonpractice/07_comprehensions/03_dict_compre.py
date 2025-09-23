tea_price_inr = {
    "Masala chai" : 40,
    "Green chai" : 50,
    "Lemon chai" : 200
}

tea_prices_usd = {tea : price / 80 for tea , price in tea_price_inr.items()}
print(tea_prices_usd)