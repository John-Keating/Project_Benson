import pandas as pd


def get_turnstiles(dates):
    ## this function concatenates different weeks given in dates
    ## dates is a list
    ## dates must be written in yymmdd and must be a Saturday
    url = 'http://web.mta.info/developers/data/nyct/turnstile/turnstile_'
    extension = '.txt'
    url_list = []

    ## create a list of urls for the dates in [dates]
    for date in dates:
        url_list.append(url + date + extension)

    df = pd.DataFrame()
    ## iterate over list reading txt files and concatenating them
    for t in url_list:
        week = pd.read_csv(t)
        frames = [df, week]
        df = pd.concat(frames, axis=0, ignore_index=True)

    return df
