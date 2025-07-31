import os
import asyncio
from fastmcp import Client
from dotenv import load_dotenv

load_dotenv()

port = os.getenv('PORT')
url = f'http://127.0.0.1:{port}/mcp'

async def main():
    async with Client(url) as client:
        if 0:
            tools = (await client.list_tools())
            for tool in tools:
                print(tool.name)
            

        # call get_sheet_data of A8
        res = await client.call_tool('list_sheets')
        print(res)

if __name__ == '__main__':
    asyncio.run(main())