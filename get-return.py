import sys
import pandas as pd

if len(sys.argv) < 2:
  print('Usage: get-return.py [CSV_FILE]')
  exit(1)
df = pd.read_csv(sys.argv[1])

reward = round(df[df['Type'] == "Reward"]['Book Cost'].sum(), 2)
print(reward)