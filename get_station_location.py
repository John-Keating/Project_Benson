import pandas as pd


def get_station_locations():
    url = "http://web.mta.info/developers/data/nyct/subway/StationEntrances.csv"
    df = pd.read_csv(url)
    return df
