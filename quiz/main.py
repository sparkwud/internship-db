import sqlite3 

import pandas as pd

conn = sqlite3.connect("questions_again.db")
cur = conn.cursor()


# creative_multimedia table 
cur.execute("DROP TABLE IF EXISTS creative_multimedia")
cur.execute("CREATE TABLE creative_multimedia (id INTEGER PRIMARY KEY AUTOINCREMENT, questions text, A text, B text, C text, D text, answer text) ")

creative_multimedia = pd.read_csv("creative_multimedia.csv")
creative_multimedia.to_sql('creative_multimedia', conn, if_exists='append', index = False)


# advertising table 
cur.execute("DROP TABLE IF EXISTS advertising")
cur.execute("CREATE TABLE advertising (id INTEGER PRIMARY KEY AUTOINCREMENT, questions text, A text, B text, C text, D text, answer text) ")

advertising = pd.read_csv("advertising.csv")
advertising.to_sql('advertising', conn, if_exists='append', index = False)


# visual_communication table 
cur.execute("DROP TABLE IF EXISTS visual_communication")
cur.execute("CREATE TABLE visual_communication (id INTEGER PRIMARY KEY AUTOINCREMENT, questions text, A text, B text, C text, D text, answer text) ")

visual_communication = pd.read_csv("visual_communication.csv")
visual_communication.to_sql('visual_communication', conn, if_exists='append', index = False)