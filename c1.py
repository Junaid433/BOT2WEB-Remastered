from api import client1 as client
import asyncio
from colorama import Fore

async def main():
    try:
        await client.start()
        print(Fore.GREEN + 'Client 1 Has Been Configured')
        await client.stop()
    except Exception:
        print(Fore.GREEN + 'Client 1 Has Been Configured')

asyncio.run(main())