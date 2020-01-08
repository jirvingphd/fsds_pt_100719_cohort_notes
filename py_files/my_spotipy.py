try:
    import spotipy
except:
    print('run: !pip install spotipy')
    
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials 

def load_spotify_api_login(auth_location="/Users/jamesirving/.secret/spotify_api.json"):
    """
    [summary]
    
    Args:
        auth_location (str, optional): [description]. Defaults to "/Users/jamesirving/.secret/spotify_api.json".
    
    Returns:
        [type]: [description]
    """
    import json
    with open(auth_location,'r') as f:
        api_login =  json.loads(f.read())
    return api_login
    
def connect_to_spotify(auth_location="/Users/jamesirving/.secret/spotify_api.json"):
    """
    [summary]
    
    Args:
        auth_location (str, optional): [description]. Defaults to "/Users/jamesirving/.secret/spotify_api.json".
    
    Returns:
        [type]: [description]
    """
    import json
    import spotipy
    import spotipy.util as util
    from spotipy.oauth2 import SpotifyClientCredentials 
    
    api_login = load_spotify_api_login(auth_location=auth_location)

    client_creds = SpotifyClientCredentials(**api_login)
    sp = spotipy.Spotify(client_credentials_manager=client_creds)
    return sp

def clean_results_row(row):
    """
    [summary]
    
    Args:
        row ([type]): [description]
    
    Returns:
        [type]: [description]
    """
    ### Meant to clean the entire dataframe, using .apply functions already defined below
    row_in=row.copy()
    # row['external_urls']=row['external_urls']['spotify']
    if 'artists' in row.index:
        x = row['artists'][0].copy()

        row['song_artist']=x['name']
        row['song_id'] =x['id']
        row=row_in.drop('artists')

    if 'album' in row.index:
        x = row['album'].copy()
        row['album_title']  = x['name']
        row['album_artist'] = x['artists'][0]['name']
        row['release_date'] = x['release_date']
        row['total_tracks'] =x['total_tracks']
        row['album_url'] = x['external_urls']['spotify']

        row = row.drop('album')

    ## Reorder output
    order = ['name', 'song_artist','album_title','track_number','duration_ms', 'popularity',
        'song_id', 'album_artist', 'release_date','total_tracks', 'explicit',   'album_url']
    order = list(filter(lambda x: x in order,row.index))
    ## add any columns not already listed
    cols = list(row.index)
    add_cols = list(filter(lambda x: x not in order, cols))
    
    order = [*order,*add_cols]
    row_out= row[order].copy()
    # print(order)

    return row_out

# def clean_results_row(row):
#     ### Meant to clean the entire dataframe, using .apply functions already defined below
#     row_in=row.copy()
#     # row['external_urls']=row['external_urls']['spotify']
    
#     x = row['artists'][0].copy()

#     row['song_artist']=x['name']
#     row['song_id'] =x['id']
#     row=row.drop('artists')

#     x = row['album'].copy()
#     row['album_title']  = x['name']
#     row['album_artist'] = x['artists'][0]['name']
#     row['release_date'] = x['release_date']
#     row['total_tracks'] =x['total_tracks']
#     row['album_url'] = x['external_urls']['spotify']

#     row = row.drop('album')

#     ## Reorder output
#     order = ['name', 'song_artist','album_title','track_number','duration_ms', 'popularity',
#         'song_id', 'album_artist', 'release_date','total_tracks', 'explicit',   'album_url']
#     ## add any columns not already listed
#     cols = list(row.index)
#     add_cols = list(filter(lambda x: x not in order, cols))
    
#     order = [*order,*add_cols]
#     row_out= row[order].copy()
#     # print(order)

#     return row_out

def response_to_df(res,drop_cols=[
    'available_markets','external_ids', 'is_local', 'preview_url']):
    """
    [summary]
    
    Args:
        res ([type]): [description]
        drop_cols (list, optional): [description]. Defaults to ['available_markets','external_ids', 'is_local', 'preview_url'].
    
    Returns:
        [type]: [description]
    """

    import pandas as pd
    df = pd.DataFrame.from_records(res['tracks']['items'])
    df = df.drop(drop_cols,axis=1)
    return df


def get_all_albums_for_artist(sp,artist_id):
    """
    [summary]
    
    Args:
        sp ([type]): [description]
        artist_id ([type]): [description]
    
    Returns:
        [type]: [description]
    """
    import pandas as pd
    import time
    offset = 0
    limit=20

    res_list= []
    res_artist = sp.artist_albums(artist_id,limit=limit,offset=offset)
    total_results = res_artist['total']
    print(f'[i] Found {total_results} results.')
    next_offset = res_artist['offset']+limit#len(res_artist['items'])

    res_list.append(res_artist['items'])


    while next_offset<=(total_results):
        time.sleep(1)
        print(f'- Retrieving offset {next_offset}')
        res_aritst = sp.artist_albums(artist_id,limit=limit,offset=next_offset)
        res_list.append(res_artist['items'])
        next_offset += limit
    return res_list
    # df = pd.DataFrame(res_list)#.from_records(res_list)
    # return df

## EXAMPLE SEARCH
if __name__ == '__main__':
        
    sp = connect_to_spotify()
    res = sp.search('Panic at the disco')
    df = response_to_df(res)
    df=df.apply(clean_results_row,axis=1)
    # print(df.head())