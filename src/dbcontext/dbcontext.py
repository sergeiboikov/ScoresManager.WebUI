import psycopg2


class DBcontext():
    def __init__(self, config):
        self.connectionstring = config.PG_DB_CONNECTION_STRING

    def run_query(self, query):
        conn = psycopg2.connect(self.connectionstring)
        cur = conn.cursor()
        cur.execute(query)
        res = cur.fetchone()
        conn.close()
        return (res)

    def run_procedure(self, query):
        conn = psycopg2.connect(self.connectionstring)
        cur = conn.cursor()
        cur.execute(query)
        cur.close()
        conn.commit()
        conn.close()
