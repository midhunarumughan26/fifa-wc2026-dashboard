import pandas as pd
import mysql.connector

df = pd.read_csv(r'C:\Users\Midhun\OneDrive\Desktop\fifa_world_cup_2026_player_performance.csv')

conn = mysql.connector.connect(
    host='localhost', user='root',
    password='9571', database='fifa_wc2026'
)
cursor = conn.cursor()


players = df[['player_id','player_name','age','nationality','team',
              'jersey_number','position','height_cm','weight_kg',
              'preferred_foot','club_name','market_value_eur']].drop_duplicates('player_id')
for _, row in players.iterrows():
    cursor.execute("""
        INSERT IGNORE INTO dim_players VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """, tuple(row))


matches = df[['match_id','match_date','stadium','city','tournament_stage']].drop_duplicates('match_id')
for _, row in matches.iterrows():
    cursor.execute("""
        INSERT IGNORE INTO dim_matches VALUES (%s,%s,%s,%s,%s)
    """, tuple(row))

conn.commit()

from sqlalchemy import create_engine
engine = create_engine('mysql+mysqlconnector://root:9571@localhost/fifa_wc2026')
fact_cols = [c for c in df.columns if c not in
             ['player_name','age','nationality','team','jersey_number','position',
              'height_cm','weight_kg','preferred_foot','club_name','market_value_eur',
              'match_date','stadium','city','tournament_stage']]
df[fact_cols].to_sql('fact_performance', engine, if_exists='append', index=False)
print("Done!")

password='9571',

engine = create_engine('mysql+mysqlconnector://root:9571@localhost/fifa_wc2026')

