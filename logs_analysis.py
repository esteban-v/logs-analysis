#!/usr/bin/env python
import psycopg2
import datetime


def run_query(query):
    """Perform and return any given query."""
    db = psycopg2.connect(database="news")
    c = db.cursor()
    c.execute(query)
    return c.fetchall()
    db.close()


def query_popular_articles():
    """Query the most popular three articles of all time.
    It's important to note that before running
    this query a view named most_viewed must have been created
    using the following query:
    create view most_viewed as select articles.title, count(*) as visits
    from articles join log on '/article/'||articles.slug = log.path
    group by articles.title order by visits desc;"""
    query = """select * from most_viewed limit 3;"""
    result = run_query(query)
    print("\r\n==== Most popular three articles ====")
    for item in result:
        print(' ' + item[0] + ' -- ' + str(item[1]) + ' views')


def query_popular_authors():
    """Query the most popular article authors of all time."""
    query = """select authors.name, sum(most_viewed.visits) as visits
            from authors, articles, most_viewed
            where authors.id = articles.author
            and most_viewed.title = articles.title
            group by authors.name order by visits desc;
            """
    result = run_query(query)
    print("\r\n==== Most popular article authors ====")
    for item in result:
        print(' ' + item[0] + ' -- ' + str(item[1]) + ' views')


def query_days_with_errors():
    """Query days where more than 1% of requests lead to errors."""
    query = """select time::date as error_date,
            (count(*)*100.0/requests) as error_average
            from log, (select time::date as request_date, count(*) as requests
                from log group by request_date) as all_requests
            where status similar to '4__%|5__%' and time::date = request_date
            group by error_date, requests having (count(*)*100.0/requests) > 1;
            """
    result = run_query(query)
    print("\r\n==== Days where more than 1% of requests lead to errors ====")
    for item in result:
        print(' ' + item[0].strftime('%B %d, %Y') +
              ' -- ' + str(round(item[1], 2)) + '% errors')

# Display the three most popular articles
query_popular_articles()

# Display the most popular authors
query_popular_authors()

# Display days where more than 1% of requests lead to errors
query_days_with_errors()
print("")
