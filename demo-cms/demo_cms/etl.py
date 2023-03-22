#!/usr/bin/env python
'''
Convenience functions for ETL (extract transform load).
'''


# ------------------------------
# Dependencies

import re
from pathlib import Path

import pyarrow
from demo_cms.model import SalesArrowTypes, SalesArrowSchema


# ------------------------------
# Functions


def ParseRegion(region: str):
    ''' Take 'region' as is. '''

    return region.strip()


def ParsePeriodEnd(period_end: str):
    ''' Split 'Period End' into 2 fields. '''

    date_fields = period_end.strip().split(' ')
    return [date_fields[0], int(date_fields[1])]


def ParseSalePrice(tuple_price: str):
    '''
    Normalize 'Median Sale Price' into an int representing USD.
    '''

    price_re     = r'^\$([0-9,]+)K'
    match_result = re.match(price_re, tuple_price.strip())
    price_str    = match_result.group(1)

    return int(price_str.replace(',', '')) * 1000


def ParseSimpleFields(csv_tuple: list[str]):
    '''
    Simple conversion of integer fields
    '''

    # grab fields 5, 8, 11, and 14 and convert to ints
    return [
        0
        if not field_val
        else int(field_val.replace(',', ''))

        for field_val in csv_tuple[5:15:3]
    ]


def ParseSaleListRatio(avg_sale_list: str):
    '''
    Convert 'Average Sale to List' to a float for simplicity
    '''

    if not avg_sale_list: return float(0)
    return float(avg_sale_list.strip().replace('%', '')) / 100


def NormalizeTupleFields(csv_tuple: list[str]):
    tuple_fields = []

    tuple_fields.append(ParseRegion(csv_tuple[0]))
    tuple_fields.extend(ParsePeriodEnd(csv_tuple[1]))
    tuple_fields.append(ParseSalePrice(csv_tuple[2]))
    tuple_fields.extend(ParseSimpleFields(csv_tuple))
    tuple_fields.append(ParseSaleListRatio(csv_tuple[17]))

    return tuple_fields


def DataFromCSV(csv_fpath: Path, skip_lines=1):
    '''
    :csv_fpath: is a path-like object providing the path to the CSV file to read data
    from.
    :skip_lines: is an integer representing how many lines to skip at the beginning of the
    CSV file. The default value of 1 assumes the first line lists column names (which we
    don't need because we have them hardcoded).
    '''

    normalized_tuples = None

    with csv_fpath.open('r', encoding='utf-16') as csv_handle:
        for ndx, line in enumerate(csv_handle):
            if ndx < skip_lines: continue

            csv_tuple        = line.strip('\n').split('\t')
            normalized_tuple = NormalizeTupleFields(csv_tuple)

            # initialize each column array with the first tuple
            if not normalized_tuples:
                normalized_tuples = [[col_val] for col_val in normalized_tuple]
                continue

            # otherwise, append to each column array
            for col_ndx, col_val in enumerate(normalized_tuple):
                normalized_tuples[col_ndx].append(col_val)

    return normalized_tuples


def TableFromCSV(data_fpath: Path) -> pyarrow.Table:
    """
    Convenience function that creates an arrow table from :data_fpath: using hard-coded
    assumptions.
    """

    # read data from the given file
    data_by_col = DataFromCSV(data_fpath)

    # construct the table and return it
    return pyarrow.Table.from_arrays(
         [
             pyarrow.array(
                  data_by_col[col_ndx]
                 ,type=col_type
             )
             for col_ndx, col_type in enumerate(SalesArrowTypes)
         ]
        ,schema=SalesArrowSchema
    )
