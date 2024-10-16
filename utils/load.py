import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
import logging

load_dotenv()

DATABASE_LOCATION = os.getenv('DATABASE_LOCATION')
print(f"DATABASE_LOCATION: {DATABASE_LOCATION}")

def load_data(song_df: pd.DataFrame):
    engine = create_engine(DATABASE_LOCATION) 
    try:
        song_df.to_sql('tracks_table_with_genres_october1', con=engine, if_exists='replace', index=True)
        logging.info("Data written to database successfully.")
    except Exception as e:
        logging.info(f"An error occurred while writing to the database: {e}")