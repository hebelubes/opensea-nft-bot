import requests
import time
import tweepy  # Twitter için (opsiyonel, uyarı için)

# Ayarlar
API_KEY = 'your_opensea_api_key'  # OpenSea API anahtarı
COLLECTION_SLUG = 'boredapeyachtclub'  # İzleyecek koleksiyon (örn: boredapeyachtclub)
POLL_INTERVAL = 1  # Saniye (FCFS için düşük tutun, ama rate limit'e dikkat)

# Twitter API (uyarı için, opsiyonel)
TWITTER_BEARER_TOKEN = 'your_twitter_bearer_token'
client = tweepy.Client(bearer_token=TWITTER_BEARER_TOKEN)

headers = {
    'X-API-KEY': API_KEY,
    'Accept': 'application/json'
}

def check_drop():
    url = f'https://api.opensea.io/api/v2/collections/{COLLECTION_SLUG}/nfts?limit=1'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        nfts = data.get('nfts', [])
        if nfts:
            latest_nft = nfts[0]
            if latest_nft.get('last_sale', {}).get('event_timestamp'):  # Satış varsa drop aktif
                print(f"Drop aktif! Son satış: {latest_nft['last_sale']['event_timestamp']}")
                # Twitter uyarı (opsiyonel)
                try:
                    client.create_tweet(text=f"🚨 {COLLECTION_SLUG} drop başladı! Hemen kontrol et: https://opensea.io/collection/{COLLECTION_SLUG}")
                except Exception as e:
                    print(f"Twitter hatası: {e}")
                return True
    return False

# Ana döngü
print(f"{COLLECTION_SLUG} drop'unu izliyorum...")
while True:
    if check_drop():
        break  # Drop başladıysa dur
    time.sleep(POLL_INTERVAL)
