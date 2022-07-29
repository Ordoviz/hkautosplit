import logging

log = logging.getLogger('hkautosplit')
log.setLevel(logging.INFO)
ch = logging.StreamHandler()
formatter = logging.Formatter('[%(levelname)s] %(message)s')
ch.setFormatter(formatter)
log.addHandler(ch)
