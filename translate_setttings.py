import aiohttp
import constants

async def translate(text: str, source: str, target: str) -> str:

    params = {
        'q': text,
        'source': source,
        'target': target,
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(constants.URL, params=params) as response:

            if response.status != 200:
                print(f'Error translating: {response.status}')
                return ''

            result = await response.json()

            return result['translatedText']