# OpenSea NFT Drop Monitoring Bot

A Python script to monitor public NFT drops on OpenSea and send alerts via Twitter when a drop starts.

## Features
- Monitors a specified OpenSea collection for new sales.
- Sends Twitter notifications when a drop is detected.
- Uses OpenSea API for real-time data.

## Setup
1. Obtain an OpenSea API key from [OpenSea API](https://docs.opensea.io/reference/api-overview).
2. (Optional) Set up a Twitter API bearer token for notifications.
3. Replace `API_KEY` and `TWITTER_BEARER_TOKEN` in `bot.py` with your credentials.
4. Run the script in a Python environment with `requests` and `tweepy` libraries installed.

## Usage
```bash
python bot.py
