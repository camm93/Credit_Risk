"""All queries, either SQL or Pandas queries are processed here.
"""
from typing import List, Union
import pandas as pd
from enums import AllFeature


def equal_to_filter(df: pd.DataFrame, col_filtered: AllFeature, columns: List[AllFeature], value: Union[str, int, float, bool]) -> pd.DataFrame:
    return df[columns][df[col_filtered]==value]
