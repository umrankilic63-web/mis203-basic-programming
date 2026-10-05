# Lab 03 - Order Approval

## Test Table

| Order Amount | Available Stock | Requested Quantity | Member | Expected Result |
|---:|---:|---:|---|---|
| 499 TRY | 10 | 2 | yes | Approved, no discount |
| 500 TRY | 10 | 2 | yes | Approved, 10% discount |
| 501 TRY | 10 | 2 | yes | Approved, 10% discount |

## Test Note

I tested the program with an order amount of 500 TRY. The order was approved and the 10% member discount was applied.

After testing, I changed the program to validate invalid quantities and insufficient stock before calculating the final price.
