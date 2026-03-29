import sys
import pandas as pd

if len(sys.argv) < 2:
  print('Usage: get-return.py [CSV_FILE]')
  exit(1)
df = pd.read_csv(sys.argv[1])

# Filter Transaction Type
reward = df[df['Type'] == "Reward"]

# Calculate Gain/Loss
reward_sum = round(reward['Book Cost'].sum(), 2)
print(reward_sum)