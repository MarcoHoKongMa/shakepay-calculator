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
cashback_sum = round(reward[reward['Description'] == 'Bitcoin cashback']['Book Cost'].sum(), 2)
gain_loss = round(btc_sell_sum + eth_sell_sum - (btc_buy_sum + eth_buy_sum), 2)

# Summarize Results
print('Shakepay Gain/Loss Summary (in CAD):')
print('BTC Cost: $' + str(btc_buy_sum))
print('ETH Cost: $' + str(eth_buy_sum))
print('BTC Reward (Taxable): $' + str(round(reward_sum - cashback_sum, 2)))
print('BTC Cashback (Non-taxable): $' + str(cashback_sum))
print()
print('BTC Sold (Includes Reward): $' + str(btc_sell_sum))
print('ETH Sold: $' + str(eth_sell_sum))
print()
print('Net Gain/Loss: (BTC Sold + ETH Sold) - (BTC Cost + ETH Cost)')
print('Net Gain/Loss: $' + str(gain_loss))
print('Net Gain/Loss - Cashback: $' + str(gain_loss - cashback_sum))