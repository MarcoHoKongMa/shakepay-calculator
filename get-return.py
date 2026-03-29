import sys
import pandas as pd

if len(sys.argv) < 2:
  print('Usage: get-return.py [CSV_FILE]')
  exit(1)
df = pd.read_csv(sys.argv[1])

# Filter Transaction Type
buy = df[df['Type'] == 'Buy']
btc_buy = buy[buy['Asset Credited'] == 'BTC']
eth_buy = buy[buy['Asset Credited'] == 'ETH']
sell = df[df['Type'] == 'Sell']
btc_sell = sell[sell['Asset Debited'] == 'BTC']
eth_sell = sell[sell['Asset Debited'] == 'ETH']
reward = df[df['Type'] == 'Reward']

# Calculate Gain/Loss
btc_buy_sum = round(btc_buy['Book Cost'].sum(), 2)
eth_buy_sum = round(eth_buy['Book Cost'].sum(), 2)
btc_sell_sum = round(btc_sell['Book Cost'].sum(), 2)
eth_sell_sum = round(eth_sell['Book Cost'].sum(), 2)
reward_sum = round(reward['Book Cost'].sum(), 2)