from pathlib import Path
import pandas as pd


def main():
    # Ricordarsi di uniformare gli header dei due file csv altrimenti le colonne differenti vengono tenute entrambe
    # portando a molti valori null per gli id che hanno solo una o l'altra in restanti o restanti2
    csv1_path = Path('restanti.csv')
    csv2_path = Path('restanti2.csv')
    merged_path = Path('merged.csv')

    df1 = pd.read_csv(csv1_path, header=0)
    df2 = pd.read_csv(csv2_path, header=0)

    merged = pd.concat([df1, df2])

    merged.to_csv(merged_path, index=False)


if __name__ == '__main__':
    main()
