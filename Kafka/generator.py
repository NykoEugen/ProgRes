import uuid
from datetime import datetime
import random


import pytz


class Generator:

    @staticmethod
    def topic_name():
        return 'Topic'

    @staticmethod
    def generate_unit() -> dict:
        batch_id = uuid.uuid1()
        dt = datetime.now(pytz.timezone('Europe/Kyiv'))
        n = random.randint(100, 1000)
        m = random.randint(0, 100)
        return {
            "schema_ver": "0.1",
            "timestamp": str(dt),
            "batch_id": str(batch_id),
            "batch_size": n,
            "sequence_num": m,
            "source_name": "TIS_PORTAL",
            "message_type": "upsert",
            "payload": {
                "entity_type": "Unit",
                "company_name": None,
                "attributes": {
                    "unit_id": m * 2 - 1,
                    "parent_unit_id": 2,
                    "name": "TowerST",
                    "ordern": 455,
                    "short_name": "TowerST",
                    "unit_type": "COMPANY"
                }
            }
        }
