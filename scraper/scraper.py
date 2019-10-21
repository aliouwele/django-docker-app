#!/usr/bin/env python3
"""python command-line utility for scrap files."""
import glob, os

import pandas as pd
from sqlalchemy import create_engine


def main():
	
	df = pd.concat(map(pd.read_csv, glob.glob(os.path.join('', "*.csv"))))
	df = df.dropna(axis=0)
	
	engine = create_engine('postgres://postgres@db:5432/postgres', echo=False)
	df.to_sql('app_opencellid', con=engine, if_exists='append', index=False)


if __name__ == '__main__':
    main()