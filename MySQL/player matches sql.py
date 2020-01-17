import requests
import pymysql
import json

# Open a connection to MySQL server
connection = pymysql.connect(host='host', user='user',password='password',db='mydb', charset='utf8')
cur = connection.cursor() # Create new cursor
cur.execute('USE mydb')

account_id = 'account id'

session = requests.Session()
url = "https://api.opendota.com/api/players/{}/matches".format(account_id)
response = session.get(url).content.decode("utf-8")
player_matches=json.loads(response)

# load matches into database
for match in player_matches:
    query = """INSERT INTO player_matches(match_id, radiant_win, duration, hero_id, start_time, kills, deaths, assists)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
    query_data = (match['match_id'], match['radiant_win'], match['duration'],
                       match['hero_id'], match['start_time'], match['kills'],
                       match['deaths'], match['assists'])
    cur.execute(query, query_data)
    connection.commit()
    
response = session.get(url, params={"win": 1}).content.decode("utf-8")
matches_won=json.loads(response)

# update matches won
for match in matches_won:
    query = """UPDATE player_matches SET win = 1 WHERE match_id = %s"""
    query_data = match['match_id']
    cur.execute(query, query_data)
    connection.commit()

response = session.get(url, params={"win": 0}).content.decode("utf-8")
matches_lost=json.loads(response)

# update matches lost
for match in matches_lost:
    query = """UPDATE player_matches SET win = 0 WHERE match_id = %s"""
    query_data = match['match_id']
    cur.execute(query, query_data)
    connection.commit()

response = session.get(url, params={"is_radiant": 1}).content.decode("utf-8")
radiant_matches=json.loads(response)

# update matches on radiant team   
for match in radiant_matches:
    query = """UPDATE player_matches SET is_radiant = 1 WHERE match_id = %s"""
    query_data = match['match_id']
    cur.execute(query, query_data)
    connection.commit()


response = session.get(url, params={"is_radiant": 0}).content.decode("utf-8")
dire_matches=json.loads(response)

# update matches on dire team   
for match in dire_matches:
    query = """UPDATE player_matches SET is_radiant = 0 WHERE match_id = %s"""
    query_data = match['match_id']
    cur.execute(query, query_data)
    connection.commit()
        
# Close database connection
connection.close()
