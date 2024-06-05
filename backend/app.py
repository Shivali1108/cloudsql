import logging
import psycopg2

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

def connect_db():
    try:
        conn = psycopg2.connect(
            dbname="your_database_name",
            user="your_username",
            password="your_password",
            host="your_host",
            port="your_port"
        )
        return conn
    except psycopg2.Error as e:
        logging.error('Unable to connect to the database: %s', e)
        raise

def init_db():
    try:
        conn = connect_db()
        with conn.cursor() as cur:
            cur.execute('''
                CREATE TABLE IF NOT EXISTS data (
                    id SERIAL PRIMARY KEY,
                    value1 TEXT NOT NULL,
                    value2 TEXT NOT NULL
                )
            ''')
        conn.commit()
        logging.info('Database initialization successful')
    except psycopg2.Error as e:
        logging.error('Error initializing the database: %s', e)
        raise
    finally:
        conn.close()

def insert_data(value1, value2):
    try:
        conn = connect_db()
        with conn.cursor() as cur:
            cur.execute('INSERT INTO data (value1, value2) VALUES (%s, %s)', (value1, value2))
            conn.commit()
            logging.info('Data inserted successfully: %s, %s', value1, value2)
    except psycopg2.Error as e:
        logging.error('Error inserting data into the database: %s', e)
        raise
    finally:
        conn.close()


