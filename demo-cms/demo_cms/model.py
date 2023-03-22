#!/usr/bin/env python
'''
Convenience functions and classes for tables.
This mostly contains schemas for now.
'''

# ------------------------------
# Dependencies

import ibis
import pyarrow


# ------------------------------
# Module Variables

# Schema for median house sales
SalesSchema = ibis.table(
    # Column names and types
     [
          ('region'              , 'string')
         ,('end_month'           , 'string')
         ,('end_year'            , 'int   ')
         ,('median_price'        , 'int   ')
         ,('homes_sold'          , 'int   ')
         ,('new_listings'        , 'int   ')
         ,('inventory'           , 'int   ')
         ,('days_on_market'      , 'int   ')
         ,('average_sale_to_list', 'float ')
     ]
    # primary key
    ,name='sales'
)

# Column types using pyarrow types
SalesArrowTypes = [
     pyarrow.utf8()
    ,pyarrow.utf8()
    ,pyarrow.int64()
    ,pyarrow.int64()
    ,pyarrow.int64()
    ,pyarrow.int64()
    ,pyarrow.int64()
    ,pyarrow.int64()
    ,pyarrow.float64()
]

SalesArrowSchema = pyarrow.schema([
     ('region'              , pyarrow.utf8())
    ,('end_month'           , pyarrow.utf8())
    ,('end_year'            , pyarrow.int64())
    ,('median_price'        , pyarrow.int64())
    ,('homes_sold'          , pyarrow.int64())
    ,('new_listings'        , pyarrow.int64())
    ,('inventory'           , pyarrow.int64())
    ,('days_on_market'      , pyarrow.int64())
    ,('average_sale_to_list', pyarrow.float64())
])
