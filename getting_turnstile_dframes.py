import pandas as pd

## Takes a list of dates and converts them into URL strings that
## then read the data as pandas dataframes
## the list must be of 6 character list of strings


def get_turnstiles(dates):
    url = 'http://web.mta.info/developers/data/nyct/turnstile/turnstile_'
    extension = '.txt'
    url_list = []

    for date in dates:
        url_list.append(url + date + extension)

    df = pd.DataFrame()

    for t in url_list:
        week = pd.read_csv(t)
        frames = [df, week]
        df = pd.concat(frames, axis=0, ignore_index=True)

    return df
