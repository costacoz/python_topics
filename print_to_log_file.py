"""
    This is another example on how to write log files.
    More correct approach would be in 11_std_logging.py file of this repo.

    This approach might be better for short scope specific logging.
"""

with open('test_example.log', mode='w') as f:
    print('I am testing logging feature.', file=f, flush=True)
