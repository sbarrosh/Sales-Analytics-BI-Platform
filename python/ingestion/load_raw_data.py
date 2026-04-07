import pandas as pd
from python.utils.db import get_engine


class LoadRawData():
    @staticmethod
    def run():
        # -------------------------
        # CONNECTION
        # -------------------------
        engine = get_engine()

        # -------------------------
        # LOAD DATA
        # -------------------------
        df = pd.read_csv("data/raw/train.csv", encoding="latin1")
        df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

        # -------------------------
        # WRITE TO RAW
        # -------------------------
        df.to_sql(
            name="superstore_raw",
            con=engine,
            schema="raw",
            if_exists="replace",
            index=False
        )

        print("Loaded into raw.superstore_raw")