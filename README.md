#  FPL Player Price Changes Tracker Bot

![FPL Price Change Tracker Twitter account Logo](https://github.com/bhushann7/FPL-Price-Changes-Bot/blob/main/FPL%20X%20logo.jpg?raw=true)

## Overview
The FPL Player Price Change Tracker is a Python application that monitors and reports daily price changes of players in the Fantasy Premier League (FPL). Utilizing the FPL API and Twitter API, this tool fetches player data, identifies price changes, and tweets the results daily at 1:30 AM GMT.

## Features
- Automatically fetches player data from the FPL API.
- Tracks daily price changes for players.
- Tweets updates on price rises and falls.

## Requirements
- Python 3.x
- Libraries:
  - requests
  - pandas
  - tweepy

You can install the required libraries using pip:

```bash
pip install requests pandas tweepy
```

## Setup

1) Clone the Repository

```bash
git clone https://github.com/bhushann7/FPL-Price-Changes-Bot.git
```

2) Navigate to the cloned repository

3) API Keys:
Obtain your Twitter API keys and tokens by creating a Twitter Developer account. Replace the placeholders in the code with your actual keys:

```python
CONSUMER_KEY = 'your_consumer_key'
CONSUMER_SECRET = 'your_consumer_secret'
ACCESS_KEY = 'your_access_key'
ACCESS_SECRET = 'your_access_secret'
```

4) Run the script

```bash
python FPL Price Changes Tracker Bot.py
```

5) Scheduling:
    Currently the code does not support scheduling but it can be added using a task scheduler:
    - Linux: using cron.
    - Windows: Use Task Scheduler

## Usage
Once set up, the script will automatically check for price changes each day. If changes are detected, it will format and tweet them. The output will indicate whether there were any price changes since the last update. Example of an tweeet is as below:

![Screenshot of a tweet using the bot](https://github.com/bhushann7/FPL-Price-Changes-Bot/blob/main/Twitter%20post%20screenshot.png?raw=true)

