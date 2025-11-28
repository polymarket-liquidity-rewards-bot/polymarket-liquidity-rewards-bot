"""Background market updater (stub)."""
import asyncio, logging

async def run_update_markets(cfg):
    logger = logging.getLogger('update_markets')
    path = cfg.get('DATA_PATH', './data')
    logger.info('Market updater started (stub). Writing to %s', path)
    while True:
        # TODO: implement real market crawling + DB persistence
        logger.debug('Refreshing market list... (stub)')
        await asyncio.sleep(60)
