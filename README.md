### Folders

***

>/click

Where you put click raw data, format should be 2013-05-06

>/install
 
Where you put install raw data, format should be 2013-05-06

>/report/Daily

Report separated by day

>/report/Monthly

Report separated by month

### Format of raw data

***

##### Example of click raw_data:  


>2013-05-18	-3	2631	1548	PHONE	0


##### Example of install raw_data:  

>2013-04-24	990	1546	iPHONE	250

### How to run

***

1.set up folders

```
/click
/install
/report/Daily
/report/Monthly
```

2.Run ```gree.py```

>python gree.py 2013-05-06  

3.Then check report folder, you can see the csv report