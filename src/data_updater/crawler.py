"""Market crawler stub. Replace with real HTTP/WebSocket code."""
import logging, asyncio

async def fetch_market_list():
    logger = logging.getLogger('data_updater')
    logger.debug('fetch_market_list (stub)')
    await asyncio.sleep(0.1)
    return []
