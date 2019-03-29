# adjust_demo
RESTful API which is capable of filtering, grouping and sorting.

## Database
Postgress database is used and following is configuration
```
'NAME': ‘adjust’,
'USER': 'adjust',
'PASSWORD': 'password’,
```
## How to apply grouping, filtering and ordering
Grouping, filtering, fields and ordering can be used at same time and independently
```
/records/?date_from=2017-07-15&country=ca&group_by=country,clicks&ordering=cpi&ordering_type=descending
```
 ### Group By
  ```
  use query param group_by followed by fields to used e.g /records/?group_by=channel,country
  ```
  ### Ordering
  ```
  use query params ordering and ordering_type e.g /records/?ordering=click&ordering_type=descending.
  For ascending use ascending.
  ```
  ### Filtering
  ```
  For filtering user these[date_from, date_to, country, channel, os] fields as query param 
  e.g /records/?date_from=2017-07-15. Date format is [YYYY-MM-DD]
  ```
  ### Get only few fields of object
  ```
  To get few fields use query param fields=clicks,spend. it would return following output 
   [{"clicks": 110, "spend": 44.0}, {"clicks": 99, "spend": 39.6}]
  ```
### Get CPI [Cost Per Install]
cpi = spend/install. Use case: show CPI values for Canada (CA) broken down by channel ordered by CPI in descending order.
```
/records/get_cpi/?country=ca&group_by=country,clicks&ordering=cpi&ordering_type=descending
```
### Get all Records
```
simply hit the /records/
```
