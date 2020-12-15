import logging

log = logging.getLogger('debug')
log.setLevel(logging.DEBUG)

fh = logging.FileHandler('debug.log')
fh.setLevel(logging.DEBUG)
fh.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(message)s'))

sh = logging.StreamHandler()
sh.setLevel(logging.DEBUG)
sh.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(message)s'))

log.addHandler(sh)
log.addHandler(fh)