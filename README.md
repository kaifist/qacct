
This program create a csv file that contains the CBLab users' disk usage and the hours of use of cpu (obtained from qacct command).
At the same time estimate of the expenses of each user.

Use:

First, get the file that contain the disk usage of each user (this will take several minutes):

```
python get_du_raw.py
```
Now you can generate the csv
```
python get_csv.py
```
following the instructions of the program.
