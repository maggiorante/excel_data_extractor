from pathlib import Path
import pandas as pd


def main():
    csv1_path = Path('merged.csv')
    csv2_path = Path('but.csv')
    csv3_path = Path('ysqs3.csv')
    joined_path = Path('join.csv')

    df1 = pd.read_csv(csv1_path, header=0, index_col='ID')
    df2 = pd.read_csv(csv2_path, header=0, index_col='ID')
    df3 = pd.read_csv(csv3_path, header=0, index_col='ID')

    joined = df1.join(df2, how='outer')
    joined = joined.join(df3, how='outer')

    joined.to_csv(joined_path)


if __name__ == '__main__':
    main()
