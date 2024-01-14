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
    def filter_gross(self, gross):
        """"
        Filter file by gross
        """
        return self.df[self.df['Gross'] >= gross]
    def filter_tickets_sold(self, tickets_sold):
        """"
        Filter file by tickets sold
        """
        return self.df[self.df['Tickets Sold'] >= tickets_sold]

@click.command(short_help="Parser to manage inputs for a Dataset")
@click.option("--input", "-i", required=True, help="Input Dataset")
@click.option("--year", "-y", type=click.INT, help="Choose year to filter by")
@click.option("--genre", "-g", help="Choose genre to filter by (Adventure, Action, Drama, Comedy, Thriller or Suspense, Horror, Romantic Comedy, Musical, Documentary, Dark Comedy, Western, Concert or Performance, Multiple Genres, Reality)")
@click.option("--gross", "-gr", type=click.INT, help="Choose gross amount to filter by (bigger than)")
@click.option("--tickets_sold", "-t", type=click.INT, help="Choose number of tickets sold to filter by (bigger than)")

def main(input,year,genre,gross,tickets_sold):
    """Main function"""
    df = pd.read_csv(input)
    #import pdb; pdb.set_trace() #To check the names of the columns
    print(df.shape)

    if year:
        df = FilteringClass(df).filter_year(year)
    if genre:
        df = FilteringClass(df).filter_genre(genre)
    if gross:
        df = FilteringClass(df).filter_gross(gross)
    if tickets_sold:
        df = FilteringClass(df).filter_tickets_sold(tickets_sold)    
    
    print(df.shape)

if __name__ == "__main__":
    main()