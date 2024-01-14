"""
Script to filter by X and count the variables
"""

import pandas as pd
import click

def main():
    """Main function"""
    df = pd.read_csv(datasets/FilmGenreStats.csv)
    print(df.shape)


if __name__ == "__main__":
    main()