import requests
import json
import tweepy
import pandas as pd

def fplpc_bot():
    #API Keys and Tokens
    CONSUMER_KEY = 'Your_token'
    CONSUMER_SECRET = 'Your_token'
    ACCESS_KEY = 'Your_token'
    ACCESS_SECRET = 'Your_token'
   

    #auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
    #auth.set_access_token(ACCESS_KEY,ACCESS_SECRET)
    #api = tweepy.API(auth)

    client = tweepy.Client(consumer_key=CONSUMER_KEY,consumer_secret=CONSUMER_SECRET,access_token=ACCESS_KEY,access_token_secret=ACCESS_SECRET)

    base_url = 'https://fantasy.premierleague.com/api/'
    general = 'bootstrap-static/'   

    r = requests.get(base_url+general).json()

    players_df = pd.DataFrame(r['elements'])

    type_mapping = {
        1: "GK",
        2: "DEF",
        3: "MID",
        4: "FWD",
        'u': "Unavailable",
        'a': "Available",
        'd': "Doubtful",
        'NaN': "Info unavailable"
    }

    players_clean_df = players_df[['web_name', 'cost_change_event', 'now_cost']].assign(
        position=players_df['element_type'].map(type_mapping),availability=players_df['status'].map(type_mapping))

    price_changed_players = players_clean_df[players_clean_df['cost_change_event']!=0].assign(
        now_cost=players_clean_df['now_cost']/10,
        prev_cost=players_clean_df['now_cost']/10-players_clean_df['cost_change_event']/10,
        arrow = players_clean_df['cost_change_event'].apply(lambda x: "up" if x > 0 else ("down" if x < 0 else "no_change")))

    #print(price_changed_players)
    

    def format_price_changes(df, change_type):
        arrow = '🔽' if change_type == 'Price Falls' else '🔼'
        message = f"{change_type} {arrow}\n\n"
        message += "Player New Price\n" # Previous
        
        for _, player in df.iterrows():
            message += f"{player['web_name']}  £{player['now_cost']:.1f}\n" # £{player['prev_cost']:.1f}
        return message.strip()  

    price_falls = price_changed_players[price_changed_players['arrow'] == 'down'].sort_values(by='now_cost', ascending=True)
    price_rises = price_changed_players[price_changed_players['arrow'] == 'up'].sort_values(by='now_cost', ascending=True)

    falls_message = format_price_changes(price_falls, 'Price Falls')
    rises_message = format_price_changes(price_rises, 'Price Rises')

    # Combine messages if they fit in one tweet, otherwise keep them separate
    if len(falls_message) + len(rises_message) + 2 <= 280:  # +2 for the newline characters
        final_message = f"{falls_message}\n\n{rises_message}"
        client.create_tweet(text=final_message)
        print("Posted Final Message")
    else:   
        # Handle separately
        if len(falls_message) <= 280:
            client.create_tweet(text=falls_message)
            print("Falls posted")
        if len(rises_message) <= 280:
            client.create_tweet(text=rises_message)
            print("Rises Posted")

if __name__ == '__main__':
    fplpc_bot()