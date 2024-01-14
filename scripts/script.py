"""
Script to filter by X and count the variables
"""

import pandas as pd
import click

@click.command(short_help="Parser to manage inputs for a Dataset")
@click.option("--input", "-i", required=True, help="Input Dataset")

def main(input):
    """Main function"""
    df = pd.read_csv(input)
    print(df.shape)


if __name__ == "__main__":
    main()