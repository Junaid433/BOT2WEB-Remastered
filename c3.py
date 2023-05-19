from api import client3 as client
import asyncio
from colorama import Fore

async def main():
    try:
        await client.start()
        print(Fore.GREEN + 'Client 3 Has Been Configured')
        await client.stop()
    except Exception:
        print(Fore.GREEN + 'Client 3 Has Been Configured')

asyncio.run(main())