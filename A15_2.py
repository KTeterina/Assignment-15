# SQL

#3
!pip install ipython-sql

%load_ext sql

!env | grep POST

import os
USER = os.environ['POSTGRESQL_USER']
PASSWORD = os.environ['POSTGRESQL_PASSWORD']
POSTGRESQL_HOST = '10.129.0.25'
DBASE_NAME = 'demo'

CONNECT_DATA = 'postgresql://{}:{}@{}/{}'.format(
    USER,
    PASSWORD,
    POSTGRESQL_HOST,
    DBASE_NAME
)

%sql SELECT tablename AS table FROM pg_tables WHERE tablename !~ '^(pg_|sql_)'

%sql SELECT * FROM boarding_passes LIMIT 5

%sql SELECT ticket_no FROM boarding_passes LIMIT 5

%sql SELECT * FROM flights LIMIT 5

%sql SELECT departure_airport FROM flights LIMIT 5

#4
%sql SELECT passenger_name FROM tickets WHERE ticket_no='0005432312164'