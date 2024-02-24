# robovar

A simple script that scans the `.robot` and `.resource` files for "regular" variables.

> Note: The special variable syntax usage (`$my_var`) is ignored in this script since it cannot be used in assignment.
> For this reason, it is unlikely to cause issues due to unintentionally overwriting a variable.

The script checks for variations in how a variable is written and prints such variations.
These variations may be intentional or not.
If not, the runtime behavior of the scripts may not be as intended.

> Note: Robot Framework matches variables and keywords case-insensitive and that single spaces and underscores (`_`) are ignored.
