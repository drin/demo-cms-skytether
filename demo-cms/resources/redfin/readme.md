# Overview

Dataset downloaded from redfin's [data center][web-redfin] in the section labeled `Redfin
Monthly Housing Market Data`. The download was from the `download` tab with only `CA`
selected and all other filters set to `(all)`; data downloaded using the "Crosstab" option
as recommended.


# Data Schema

+--------------------------+-----------------------+
| Column                   | Type                  |
+--------------------------+-----------------------+
| Region                   | String                |
| Month of Period End      | String (Month Year)   |
| Median Sale Price        | String ($[0-9,]+K)    |
| Median Sale Price MoM    | String ([-]?[0-9.]+%) |
| Median Sale Price YoY    | String ([-]?[0-9.]+%) |
| Homes Sold               | Int                   |
| Homes Sold MoM           | String ([-]?[0-9.]+%) |
| Homes Sold YoY           | String ([-]?[0-9.]+%) |
| New Listings             | Int                   |
| New Listings MoM         | String ([-]?[0-9.]+%) |
| New Listings YoY         | String ([-]?[0-9.]+%) |
| Inventory                | Int                   |
| Inventory MoM            | String ([-]?[0-9.]+%) |
| Inventory YoY            | String ([-]?[0-9.]+%) |
| Days on Market           | Int                   |
| Days on Market MoM       | Int                   |
| Days on Market YoY       | Int                   |
| Average Sale To List     | String ([-]?[0-9.]+%) |
| Average Sale To List MoM | String ([-]?[0-9.]+%) |
| Average Sale To List YoY | String ([-]?[0-9.]+%) |
+--------------------------+-----------------------+


<!-- Resources -->
[web-redfin]: https://www.redfin.com/news/data-center/
