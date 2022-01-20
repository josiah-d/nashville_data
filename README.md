# Nashville EDA

EDA of data from the Nashville Open Data Portal

## Data

There are 6,374,126 rows and 19 features containing details about emergency and non-emergency calls for Metro Nashville Police Department service received by the Emergency Communications Center.

A sample of the data, 10,000 rows, was used to perform initial exploratory data analyses (EDA).

| # |  Column |                     Non-Null Count | Dtype |
| --- | ------ |                     -------------- | ----- |
| 0 |  Event Number |               10000 non-null | object |
| 1 |  Call Received |              10000 non-null | object |
| 2 |  Complaint Number |           851 non-null |   float64 |
| 3 |  Tencode |                    10000 non-null | int64 |
| 4 |  Tencode Description |        9745 non-null |  object |
| 5 |  Tencode Suffix |             6031 non-null |  object |
| 6 |  Tencode Suffix Description | 5237 non-null |  object |
| 7 |  Disposition Code |           9960 non-null |  object |
| 8 |  Disposition Description |    7839 non-null |  object |
| 9 |  Block |                      2260 non-null |  float64 |
| 10 | Street Name |                2699 non-null |  object |
| 11 | Unit Dispatched |            9309 non-null |  object |
| 12 | Shift |                      10000 non-null | object |
| 13 | Sector |                     7773 non-null |  object |
| 14 | Zone |                       8727 non-null |  object |
| 15 | RPA |                        7996 non-null |  float64 |
| 16 | Latitude |                   1312 non-null |  float64 |
| 17 | Longitude |                  1312 non-null |  float64 |
| 18 | Mapped Location |            1312 non-null |  object |
