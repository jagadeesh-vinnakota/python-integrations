import logging

first = 5
second = 0

try:
    result = first/second
except Exception as e:
    logging.exception(f'Indicates exception logging, {e}')
