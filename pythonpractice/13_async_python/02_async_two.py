import asyncio

async def brew(name):
    print(f"Starting to brew {name}...")
    await asyncio.sleep(3)
    print(f"{name} is ready")

async def main():
    await asyncio.gather(
        brew('Masala chai'),
        brew('Ginger chai'),
        brew('Lemon tea'),
    )

asyncio.run(main())