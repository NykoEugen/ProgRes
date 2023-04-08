import psycopg
def sent_msg_to_sql(self):
    with psycopg.connect("host=localhost port=5432 dbname=testdb user=postgres password=Astroraph1995") as conn:
        with conn.cursor() as cur:
            # cur.execute("DROP TABLE messages ")
            # cur.execute("""CREATE TABLE messages (id SERIAL PRIMARY KEY, message TEXT)""")
            message = self.msg
            cur.execute("INSERT INTO messages (message) VALUES (%s)", (message,))
            conn.commit()
            conn.close()
{
  "schema_ver": "0.1",
  "timestamp": "2023-03-20 14:24:22.916956+02:00",
  "batch_id": "256a884e-c71a-11ed-b587-0242ac120004",
  "batch_size": 823,
  "sequence_num": 65,
  "source_name": "TIS_PORTAL",
  "message_type": "upsert",
  "payload": {
    "entity_type": "Unit",
    "company_name": null,
    "attributes": {
      "unit_id": 129,
      "parent_unit_id": 2,
      "name": "TowerST",
      "ordern": 455,
      "short_name": "TowerST",
      "unit_type": "COMPANY"
    }
  }
}