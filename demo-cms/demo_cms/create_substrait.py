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
A simple script to create substrait from an ibis query expression.
"""



# ------------------------------
# Dependencies

from pathlib import Path

import ibis
from ibis_substrait.compiler.core import SubstraitCompiler

from demo_cms.model import SalesSchema


# ------------------------------
# Main logic

if __name__ == '__main__':
    # Define the query
    query_expr = SalesSchema['region', 'end_month', 'end_year', 'median_price']

    # SubstraitCompiler takes an ibis expr and creates a substrait plan
    substrait_compiler = SubstraitCompiler()
    proto_msg = substrait_compiler.compile(query_expr.unbind())

    # Take a peek at the result
    print(proto_msg)

    # Write the query plan to a file for simplicity
    with open('query-plan.substrait', 'wb') as plan_handle:
        plan_handle.write(proto_msg.SerializeToString())
