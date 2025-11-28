"""Simple statistics utilities (stub)."""
import logging

def compute_pnl(trades):
    logging.getLogger('poly_stats').debug('compute_pnl called (stub)')
    return {'pnl': 0.0, 'trades': len(trades)}
