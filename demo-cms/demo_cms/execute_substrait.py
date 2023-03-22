#!/usr/bin/env python

# ------------------------------
# License

# Copyright 2023 Aldrin Montana
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


# ------------------------------
# Module Docstring
"""
A simple script to execute a substrait plan.
"""


# ------------------------------
# Dependencies

from pathlib import Path

import pyarrow
import pandas

from pyarrow import substrait

from demo_cms.etl import TableFromCSV


# ------------------------------
# Module Variables

FilePathsByTable = {
    'sales': Path('resources') / 'redfin' / 'data.csv'
}


# ------------------------------
# Functions

def ExampleTableProvider(table_names, expected_schema=None):
    # table_names is a list of strings representing a single table
    tname = '.'.join(table_names)
    # print(f'Table requested: [{tname}]')

    print('Before Execution')
    source_table = TableFromCSV(FilePathsByTable[tname])
    print(source_table.to_pandas())

    return source_table

def ExecuteSubstrait(substrait_plan: bytes) -> pyarrow.Table:
    print('Executing substrait...')
    result_reader = substrait.run_query(
         substrait_plan
        ,table_provider=ExampleTableProvider
    )

    print('Query plan executed')
    return result_reader.read_all()


# ------------------------------
# Main logic

if __name__ == '__main__':
    # Read the query plan from a file for simplicity into the protobuf structure
    with Path('query-plan.substrait').open('rb') as plan_handle:
        plan_msg = plan_handle.read()

    # Execute the plan and show the results
    query_result = ExecuteSubstrait(plan_msg)

    # pandas prints prettier
    print('After Execution')
    print(query_result.to_pandas())
