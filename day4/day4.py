#############
# Common Code
#############

import pandas as pd
import numpy as np
from datetime import datetime

INPUT_FILE = "input.txt"

# Read input to get an ordered list of records
records = []
with open(INPUT_FILE) as f:
    for entry in f:
        date, time, record = entry.split(' ', 2)
        date = ' '.join([date, time]).strip('[]')
        records.append([datetime.strptime(date, "%Y-%m-%d %H:%M"), record])

# Create a Dataframe with the date and records and order by date
df = pd.DataFrame(records, columns=["Date", "Record"])
df = df.sort_values("Date")

# Add a shift columns to know which guard does what
df["Shift"] = df["Record"].apply(lambda x: x.split(' ')[1])
df["Shift"] = df["Shift"][df["Shift"].str.contains('#')]
df["Shift"] = df["Shift"].fillna(method="ffill")
df["Shift"] = df["Shift"].apply(lambda x: int(x.strip('#')))

# Add a State column
# 0 = falls asleep
# 1 = wakes up
df["State"] = np.nan
df["State"][df["Record"].str.contains("falls")] = 0
df["State"][df["Record"].str.contains("wakes")] = 1

# Clean the dataframe
df = df.dropna()
df["State"] = df["State"].astype(int)
df["Shift"] = df["Shift"].astype(int)
del(df["Record"])

##########
# Part One
##########

# Add a column with the slept time
df["Slept"] = abs(df["Date"] - df["Date"].shift(1)).dt.seconds / 60
df["Slept"] = df["Slept"].fillna(value = 0)

# Keep only the slept time
df["Slept"] = df["Slept"][df["State"] == 1]
df["Slept"] = df["Slept"].fillna(value = 0)

# Sum of slept minutes by guard
slept_df = df.loc[:, ["Shift", "Slept"]].groupby("Shift").sum()

# Get the id of the guard that slept the most
ID_max_slept = slept_df.loc[slept_df["Slept"].idxmax()].name

# Make a list of sleep/wake minutes
sleep_df = df[df["Shift"] == ID_max_slept]
sleep_list = [time.minute for time in list(sleep_df.loc[:, "Date"])]

# Traverse the list pairwise to build a number of time which minute is lept
sleep_of_max_slept = pd.Series([0] * 60)
for sleep, wake in zip(sleep_list[0::2], sleep_list[1::2]):
    sleep_of_max_slept[sleep:wake] += 1

# Get the most slept minute
minute_most_slept = sleep_of_max_slept.idxmax()

print("Part One:", ID_max_slept * minute_most_slept)

##########
# Part Two
##########

# Slept time by guards
slept_df = df.pivot(index="Date", columns="Shift")
slept_df = slept_df["State"]

# For each guard find the most slept minute
slept_minute = []
for ID in slept_df.columns:
    sleep_df = slept_df[ID].dropna()
    sleep_list = [time.minute for time in list(sleep_df.index)]

    # Traverse the list pairwise to build a number of time which minute is slept
    sleep_of_max_slept = pd.Series([0] * 60)
    for sleep, wake in zip(sleep_list[0::2], sleep_list[1::2]):
        sleep_of_max_slept[sleep:wake] += 1

    # Get the most slept minute along with the number of time it was slept
    minute_most_slept = sleep_of_max_slept.idxmax()
    num = sleep_of_max_slept.max()

    slept_minute.append((ID, minute_most_slept, num))

# The minute that was the most slept is the one we choose
ID, most_slept_minute, _ = max(slept_minute, key=lambda x: x[2])

print("Part Two:", ID * most_slept_minute)
