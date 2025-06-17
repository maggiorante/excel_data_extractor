import os
from pathlib import Path
from typing import List, Callable, Optional

import pandas as pd


class BasePair:
    def __init__(self, top: int, left: int, bottom: int, right: int):
        self._top = top
        self._left = left
        self._bottom = bottom
        self._right = right

    def keys(self, df: pd.DataFrame) -> List[str]:
        pass

    def values(self, df: pd.DataFrame) -> List[int]:
        pass

def remove_newlines(string: str):
    return string.replace('\n', ' ').replace('\r', '')

class RowPair(BasePair):
    def __init__(self, top: int, left: int, bottom: int, right: int, allow_next_cell_key: bool = False,
                 process_key_fn: Optional[Callable[[str], str]] = None):
        super().__init__(top, left, bottom, right)
        self._allow_next_cell_key = allow_next_cell_key
        self._process_key_fn = process_key_fn

    def keys(self, df: pd.DataFrame) -> List[str]:
        keys = []
        for i in range(self._top, self._bottom):
            key = df.iat[i, self._left]

            if pd.isna(key) and self._allow_next_cell_key:
                key = df.iat[i, self._left + 1]

            if not pd.isna(key):
                key = remove_newlines(str(key))

                if self._process_key_fn is not None:
                    keys.append(self._process_key_fn(key))
                else:
                    keys.append(key)

        return keys

    def values(self, df: pd.DataFrame) -> List[int]:
        values = []
        for i in range(self._top, self._bottom):
            # Check for key not NaN
            key = df.iat[i, self._left]

            if pd.isna(key) and self._allow_next_cell_key:
                key = df.iat[i, self._left + 1]

            if not pd.isna(key):
                values.append(df.iat[i, self._right])

        return values


class ColumnPair(BasePair):
    def keys(self, df: pd.DataFrame) -> List[str]:
        keys = []

        if self._left == self._right:
            r = [self._left]
        else:
            r = range(self._left, self._right)

        for i in r:
            key = df.iat[self._top, i]
            if not pd.isna(key):
                key = remove_newlines(str(key))

                keys.append(key)

        return keys

    def values(self, df: pd.DataFrame) -> List[int]:
        values = []

        if self._left == self._right:
            r = [self._left]
        else:
            r = range(self._left, self._right)

        for i in r:
            # Check for key not NaN
            key = df.iat[self._top, i]
            if not pd.isna(key):
                values.append(df.iat[self._bottom, i])

        return values


class Shit:
    def __init__(self, name: str, pairs: List[BasePair]):
        self._name = name
        self._pairs = pairs

    def keys(self, df: pd.DataFrame):
        keys = []
        for pair in self._pairs:
            for key in pair.keys(df):
                keys.append(f'{self._name}.{key}')

        return keys

    def values(self, df: pd.DataFrame):
        values = []
        for pair in self._pairs:
            for value in pair.values(df):
                values.append(value)

        return values


def main():
    root_dir_restanti = Path('C:/Users/xho99/Downloads/greta/RESTANTI')
    root_dir_restanti2 = Path('C:/Users/xho99/Downloads/greta/RESTANTI 2')
    root_dir_but = Path('C:/Users/xho99/Downloads/greta/BUT')
    root_dir_ysqs3 = Path('C:/Users/xho99/Downloads/greta/YSQS3')

    sheets_restanti = {
        '1)BPN-I': Shit('BPN-I', [
            RowPair(1, 0, 29, 1),
            RowPair(6, 3, 11, 6, True),
            RowPair(14, 3, 21, 6, True),
        ]),
        '3)CPQ': Shit('CPQ', [
            RowPair(1, 0, 14, 1),
        ]),
        '4)DERS': Shit('DERS', [
            RowPair(1, 0, 19, 1),
            RowPair(4, 6, 11, 11),
        ]),
        '5)EDE-Q': Shit('EDE-Q', [
            RowPair(1, 0, 29, 1),
            RowPair(13, 4, 17, 8),
            ColumnPair(13, 10, 14, 10),
        ]),
        '6)ESS': Shit('ESS', [
            RowPair(1, 0, 27, 1),
        ]),
        '7)HADS': Shit('HADS', [
            RowPair(1, 0, 15, 1),
            RowPair(6, 12, 8, 13),
        ]),
        '8)PCI-Q': Shit('PCI-Q', [
            RowPair(1, 0, 13, 1),
        ]),
        '9)MSAS': Shit('MSAS', [
            RowPair(1, 1, 19, 2),
            # Colonna UNDERSTANDING ONE'S OWN MIND che in restanti2 non c'è
            # ColumnPair(2, 4, 5, 4),
            ColumnPair(3, 4, 4, 4),
            ColumnPair(3, 6, 4, 6),
            ColumnPair(2, 8, 3, 8),
            ColumnPair(2, 12, 3, 12),
        ]),
        '10)RSES': Shit('RSES', [
            RowPair(1, 0, 12, 1),
        ]),
        '11)SCS-SF': Shit('SCS-SF', [
            RowPair(1, 0, 13, 1),
            RowPair(6, 5, 12, 8),
            ColumnPair(5, 9, 6, 9),
        ])
    }

    sheets_restanti2 = {
        '1)BPN-I': Shit('BPN-I', [
            RowPair(1, 0, 29, 1),
            RowPair(6, 3, 11, 6, True),
            RowPair(14, 3, 22, 6, True),
        ]),
        '3)CPQ': Shit('CPQ', [
            RowPair(1, 0, 14, 1),
        ]),
        '4)DERS': Shit('DERS', [
            RowPair(1, 0, 19, 1),
            RowPair(6, 5, 13, 10),
        ]),
        '5)EDE-Q': Shit('EDE-Q', [
            RowPair(1, 0, 29, 1),
            RowPair(10, 12, 17, 16),
            ColumnPair(10, 18, 11, 18),
        ]),
        '6)ESS': Shit('ESS', [
            RowPair(1, 0, 27, 1),
        ]),
        '7)HADS': Shit('HADS', [
            RowPair(1, 0, 15, 1),
            RowPair(6, 12, 8, 13),
        ]),
        '8)PCI-Q': Shit('PCI-Q', [
            RowPair(1, 0, 13, 1),
        ]),
        '9)MSAS': Shit('MSAS', [
            RowPair(1, 1, 19, 2),
            RowPair(9, 15, 19, 20, process_key_fn=lambda x: x.split(':')[0]),
        ]),
        '10)RSES': Shit('RSES', [
            RowPair(1, 0, 12, 1),
        ]),
        '11)SCS-SF': Shit('SCS-SF', [
            RowPair(1, 0, 13, 1),
            RowPair(6, 15, 17, 17),
            ColumnPair(5, 19, 6, 19),
        ])
    }

    sheets_but = {
        'BUT A': Shit('BUT.A', [
            RowPair(2, 0, 36, 2),
        ]),
        'BUT B': Shit('BUT.B', [
            RowPair(2, 0, 39, 2),
        ]),
        'Risultato': Shit('BUT', [
            RowPair(2, 0, 8, 1, process_key_fn=lambda x: 'A.' + x),
            RowPair(12, 0, 14, 1, process_key_fn=lambda x: 'B.' + x),
        ]),
    }

    sheets_ysqs3 = {
        'Sheet1': Shit('YSQS3', [
            RowPair(3, 0, 93, 1),
            RowPair(95, 2, 113, 3),
        ]),
    }

    output_restanti = Path('restanti.csv')
    output_restanti2 = Path('restanti2.csv')
    output_but = Path('but.csv')
    output_ysqs3 = Path('ysqs3.csv')

    configs = [
        (root_dir_restanti, sheets_restanti, output_restanti),
        (root_dir_restanti2, sheets_restanti2, output_restanti2),
        (root_dir_but, sheets_but, output_but),
        (root_dir_ysqs3, sheets_ysqs3, output_ysqs3),
    ]

    for root_dir, sheets, output_path in configs:
        print('{:=^80}'.format(' Merging '))

        print('Root dir: ', root_dir)
        print('Output file: ', output_path)

        files = os.listdir(root_dir)

        files = list(filter(lambda x: not x.startswith('~'), files))

        # Get column names
        xl = pd.ExcelFile(root_dir / files[0])

        columns = ['ID']

        for key, value in sheets.items():
            df = xl.parse(key, header=None)

            columns.extend(value.keys(df))

        # Generate merged dataset
        df_new = pd.DataFrame(columns=columns)

        for filename in files:

            file_path = root_dir / filename

            xl = pd.ExcelFile(file_path)

            values = [file_path.stem.split('_')[-1]]

            for key, value in sheets.items():
                df = xl.parse(key, header=None)

                values.extend(value.values(df))

            df_new.loc[len(df_new)] = values

        # df_new.astype({col: int for col in df_new.columns[1:]})
        df_new.to_csv(output_path, index=False)


if __name__ == '__main__':
    main()
