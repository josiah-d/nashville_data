# Nashville EDA

EDA of data from the Nashville Open Data Portal

## TODO

1. Convert `Call Received` to `DateTime` object
2. Count duplicates
    A. Keep most recent
3. Make separate data of location data
    1. Make heat maps of the Nashville area (categorize by type)
4. Look for anomolies in different regions or responding officers

## Notes (DELME)

1. Complaint number: MNPD incident number for the call, if an incident is generated for the call (not all calls generate incident reports)
    1. Could be a clue as to whether in incident was more severe
2. Only 17 entries in slice without missing data
3. Duplicate entries (determined by `Event Number`) were removed. Kep the one with the fewest NaNs.


## Data

There are 6,374,126 rows and 19 features containing details about emergency and non-emergency calls for Metro Nashville Police Department service received by the Emergency Communications Center. The data is complied daily and was last updated on January 17, 2022.

A sample of the data (10,000 rows) was used to perform initial exploratory data analyses (EDA). Four of the features (`Tencode Description`, `Tencode Suffix Description`, `Disposition Description`, `Mapped Location`) were excluded from the analyses since they are redundant.


**Feature Manipulation**



| # |  Column |                     Non-Null Count | Dtype |
| --- | ------ |                     -------------- | ----- |
| 0 |  Event Number |               10000 non-null | object |
| 1 |  Call Received |              10000 non-null | object |
| 2 |  Complaint Number |           851 non-null |   float64 |
| 3 |  Tencode |                    10000 non-null | int64 |
| 4 |  Tencode Suffix |             6031 non-null |  object |
| 5 |  Disposition Code |           9960 non-null |  object |
| 6 |  Block |                      2260 non-null |  float64 |
| 7 | Street Name |                2699 non-null |  object |
| 8 | Unit Dispatched |            9309 non-null |  object |
| 9 | Shift |                      10000 non-null | object |
| 10 | Sector |                     7773 non-null |  object |
| 11 | Zone |                       8727 non-null |  object |
| 12 | RPA |                        7996 non-null |  float64 |
| 13 | Latitude |                   1312 non-null |  float64 |
| 14 | Longitude |                  1312 non-null |  float64 |
