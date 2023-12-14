#!/usr/bin/env python3

import psycopg2
from prometheus_client import start_http_server, Summary, Gauge
import random
import time


def queryActiveConnections(cursor):
    # active connections
    sql ='select count(*) from pg_stat_activity;'
    cursor.execute(sql)
    result_active_conn = cursor.fetchone()

    return result_active_conn[0]

def queryMaxConnections(cursor):
    # default max connections
    sql = "SELECT current_setting('max_connections');"
    cursor.execute(sql)
    result_max_conn = cursor.fetchone()

    return result_max_conn[0]

if __name__ == '__main__':


    gauge_active_conn = Gauge('database_connections_active', 'Number of active database connections')
    gauge_max_conn = Gauge('database_connections_max', 'Number of maximum set maximum database ')



    # print(queryActiveConnections())
    # Start up the server to expose the metrics.
    start_http_server(8000)
    # Generate some requests.
    while True:
        try:
            with psycopg2.connect(host = "postgres_db", dbname = "postgres", user = "postgres", password = "password123") as conn:
                with conn.cursor() as cursor:
                    gauge_active_conn.set(queryActiveConnections(cursor))
                    gauge_max_conn.set(queryMaxConnections(cursor))
                    time.sleep(600)
        except Exception as err:
            print("Error while scraping metrics: #{0}#".format(err))
