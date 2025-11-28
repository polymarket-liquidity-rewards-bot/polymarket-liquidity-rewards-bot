"""Statistics updater (stub)."""
import asyncio, logging

async def run_update_stats(cfg):
    logger = logging.getLogger('update_stats')
    logger.info('Stats updater started (stub).')
    while True:
        # TODO: calculate PnL, exposures, and persist
        logger.debug('Updating stats... (stub)')
        await asyncio.sleep(30)
