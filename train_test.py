import drink_detect

# logger setting
from logging import getLogger, StreamHandler, Formatter, DEBUG, INFO
logger = getLogger()
formatter = Formatter('%(asctime)s %(name)s %(funcName)s [%(levelname)s]: %(message)s')
handler = StreamHandler()
handler.setFormatter(formatter)
logger.addHandler(handler)

dd = drink_detect.DrinkDetector(debug=True)
dd.train()

