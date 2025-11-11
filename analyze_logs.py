#!/usr/bin/env python3
import pandas as pd
import argparse

def safe_parse_duration(x):
    try:
        if pd.isna(x): return None
        val = float(x)
        if val < 0: return None
        return val
    except:
        return None

def safe_parse_timestamp(s):
    try:
        return pd.to_datetime(s)
    except:
        return None

def analyze(path):
    df = pd.read_csv(path)
    expected = {'user','task_type','start','duration_min'}
    if not expected.issubset(set(df.columns)):
        raise SystemExit(f"CSV missing columns: {expected - set(df.columns)}")

    df['duration_min'] = df['duration_min'].apply(safe_parse_duration)
    df['start_parsed'] = df['start'].apply(safe_parse_timestamp)
    df['row_status'] = 'ok'
    df.loc[df['duration_min'].isna(), 'row_status'] = 'bad_duration'
    df.loc[df['start_parsed'].isna(), 'row_status'] = 'bad_timestamp'

    good = df[df['row_status']=='ok']
    total_user = good.groupby('user', as_index=False)['duration_min'].sum()
    total_task = good.groupby('task_type', as_index=False)['duration_min'].sum()
    top3 = total_task.sort_values('duration_min', ascending=False).head(3)

    print("SUMMARY REPORT")
    print("--------------")
    print(f"Valid rows: {len(good)} / {len(df)}\n")
    print("Time per user:\n", total_user)
    print("\nTime per task type:\n", total_task)
    print("\nTop 3 task types:\n", top3)

    total_user.to_csv('summary_time_per_user.csv', index=False)
    total_task.to_csv('summary_time_per_task.csv', index=False)
    df.to_csv('logs_processed.csv', index=False)
    print("\nFiles saved: summary_time_per_user.csv, summary_time_per_task.csv, logs_processed.csv")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="logs_sample.csv")
    args = parser.parse_args()
    analyze(args.input)
