"""
Script to filter by X and count the variables
"""

import pandas as pd
import click

class FilteringClass:
    """
    Class for filtering
    """

    def __init__(self,df):
        self.df = df

    def filter_year(self, year):
        """"
        Filter file by year
        """
        return self.df[self.df['Year'] == year]
    def filter_genre(self, genre):
        """"
        Filter file by genre
        """
        return self.df[self.df['Genre'] == genre]

@click.command(short_help="Parser to manage inputs for a Dataset")
@click.option("--input", "-i", required=True, help="Input Dataset")
@click.option("--year", "-y", help="Year", help="Choose year to filter by")
@click.option("--genre", "-g", help="Genre", help="Choose genre to filter by")

def main(input,year,genre):
    """Main function"""
    df = pd.read_csv(input)
    import pdb; pdb.set_trace() #To check the names of the columns
    print(df.shape)

    if year:
        df = FilteringClass(df).filter_year(year)
    if genre:
        df = FilteringClass(df).filter_genre(genre)
    print(df.shape)

if __name__ == "__main__":
    main()