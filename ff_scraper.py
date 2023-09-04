import requests
from bs4 import BeautifulSoup
import pandas as pd

urls_cbs = {
    'QB': "https://www.cbssports.com/fantasy/football/stats/QB/2023/season/projections/nonppr/",
    'WR': "https://www.cbssports.com/fantasy/football/stats/WR/2023/season/projections/nonppr/",
    'TE': "https://www.cbssports.com/fantasy/football/stats/TE/2023/season/projections/nonppr/",
    'K': "https://www.cbssports.com/fantasy/football/stats/K/2023/season/projections/nonppr/",
    'RB': "https://www.cbssports.com/fantasy/football/stats/RB/2023/season/projections/nonppr/",
    'DST': "https://www.cbssports.com/fantasy/football/stats/DST/2023/season/projections/nonppr/"
}

import requests
from bs4 import BeautifulSoup
import pandas as pd

def extract_headers(soup):
    header_tags = soup.select('.TableBase-headTr .TableBase-headTh')
    headers = [tag.text.strip() for tag in header_tags]
    return headers

team_df = pd.read_csv('team_fantasy_points.csv')

def integrate_team_data(df, team_df):
    team_df = team_df.rename(columns={'Fantasy Points': 'PlayerValue'})
    team_df['Position'] = 'DST'
    return pd.concat([df, team_df], ignore_index=True)

def get_all_players():
    return df['Player'].tolist()

def extract_player_stats(row, headers):
    player_name_tag = row.find('span', class_='CellPlayerName--long')
    if not player_name_tag:
        return None
    
    td_elements = row.find_all('td')
    stats = [td.text.strip() for td in td_elements]
    
    if player_name_tag and player_name_tag.a:
        player_name = player_name_tag.a.text.strip()
    else:
        player_name = None

    player_dict = {headers[i]: stat for i, stat in enumerate(stats)}
    if player_name:
        player_dict["Player"] = player_name

    return player_dict

def fetch_stats_from_cbs(url, position):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    headers = extract_headers(soup)
    headers.append('Position')  # Add the Position column
    
    table_rows = soup.select('.TableBase-bodyTr')
    
    all_stats = []
    for row in table_rows:
        player_data = extract_player_stats(row, headers)
        if player_data:
            player_data['Position'] = position
            all_stats.append(player_data)
            
    return all_stats

all_players = []

for position, url in urls_cbs.items():
    print(f"Fetching data for {position}...")
    players = fetch_stats_from_cbs(url, position)
    all_players.extend(players)

df = pd.DataFrame(all_players)

stat_values = {
    'QB': {
        'yds\n                            Passing Yards': 0.04, 
        'td\n                            Touchdowns Passes': 4, 
        'int\n                            Interceptions Thrown': -2, 
        'fl\n                            Fumbles Lost': -2
    },
    'RB': {
        'yds\n                            Rushing Yards': 0.1, 
        'td\n                            Rushing Touchdowns': 6, 
        'rec\n                            Receptions': 1, 
        'yds\n                            Receiving Yards': 0.1, 
        'td\n                            Receiving Touchdowns': 6, 
        'fl\n                            Fumbles Lost': -2
    },
    'WR': {
        'yds\n                            Receiving Yards': 0.1, 
        'td\n                            Receiving Touchdowns': 6, 
        'rec\n                            Receptions': 1, 
        'fl\n                            Fumbles Lost': -2
    },
    'TE': {
        'yds\n                            Receiving Yards': 0.1, 
        'td\n                            Receiving Touchdowns': 6, 
        'rec\n                            Receptions': 1, 
        'fl\n                            Fumbles Lost': -2
    },
    'K': {
        '20-29\n                            Field Goals 20-29 Yards': 3, 
        '30-39\n                            Field Goals 30-39 Yards': 3, 
        '40-49\n                            Field Goals 40-49 Yards': 4, 
        '50+\n                            Field Goals 50+ Yards': 5, 
        'xpm\n                            Extra Points Made': 1
    },
    'DST': {
        'int\n                            Interceptions': 2,
        'sfty\n                            Safeties': 2,
        'sck\n                            Sacks': 1,
        'tk\n                            Tackles': 0.1,
        'frec\n                            Defensive Fumbles Recovered': 2,
        'fum\n                            Forced Fumbles': 2,
        'dtd\n                            Defensive Touchdowns': 6
    }
}

# Compute PlayerValue before integrating team data
df['PlayerValue'] = 0
for position, values in stat_values.items():
    for stat, value in values.items():
        if stat in df.columns:
            df[stat] = df[stat].replace('—', '0').astype(float)
            df.loc[df['Position'] == position, 'PlayerValue'] += df[stat] * value

df = integrate_team_data(df, team_df)

print(df)

# Print the DST dataframe
print("\nDST Data:")
print(df[df['Position'] == 'DST'])

df.columns = df.columns.str.strip()

def get_trade_evaluation(players_team_a, players_team_b):
    df_team_a = df[df['Player'].isin(players_team_a)]
    df_team_b = df[df['Player'].isin(players_team_b)]
    
    print("\nTeam A Player Values:")
    for index, row in df_team_a.iterrows():
        # Handle potential NaN values
        value = 0 if pd.isna(row['PlayerValue']) else row['PlayerValue']
        print(f"{row['Player']} - {value}")
    
    value_team_a = df_team_a['PlayerValue'].sum()
    print(f"\nTotal Value for Team A: {value_team_a:.2f}")

    print("\nTeam B Player Values:")
    for index, row in df_team_b.iterrows():
        # Handle potential NaN values
        value = 0 if pd.isna(row['PlayerValue']) else row['PlayerValue']
        print(f"{row['Player']} - {value}")
    
    value_team_b = df_team_b['PlayerValue'].sum()
    print(f"\nTotal Value for Team B: {value_team_b:.2f}")

    if value_team_a > value_team_b:
        return ("Team A has a better trade value.", value_team_a, value_team_b)
    elif value_team_b > value_team_a:
        return ("Team B has a better trade value.", value_team_a, value_team_b)
    else:
        return ("Both teams have equal trade value.", value_team_a, value_team_b)


result = get_trade_evaluation(["Derek Carr", "Justin Jefferson", "Jordan Akins", "Green Bay"], ["Bijan Robinson", "Alvin Kamara", "Travis Kelce", 'Cincinnati'])
print(result)