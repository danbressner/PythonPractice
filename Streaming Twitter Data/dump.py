import settings
import dataset
from datafreeze import freeze


db = dataset.connect(settings.CONNECTION_STRING)

result = db[settings.OUTPUT_TABLE].all()
freeze(result, format='csv', filename=settings.OUTPUT_FILE)
