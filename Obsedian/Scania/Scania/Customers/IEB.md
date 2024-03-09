
## KSQLDB
| Sl No | Item | Numbers |
| ---- | ---- | ---- |
| 1 | Number of transaction per week | TBD (< 0.5 million) |
| 2 | Size of payload | 10 KB |
| 3 | How often do you read the data | Weekly |
| 4 | What is the hot set data size | N/A |
| 5 | Should data be encrypted | End to End |
| 6 | Should data be isolated | No |
| 7 | Dedicated cluster | Separate cost |
| 8 | Cluster type | Shared |
|  |  |  |
|  |  |  |
|  |  |  |

Estimate for China = 7 PRU with 30 MB = 210 MB / day


![[IEB KSQLDB]]


## POC

1. Check if we restart ksql cluster, will the offset be retained
2. If the offset is retained, where is it stored
3. Can we schedule a ksql stream?


### How many streams do we need

We need 3 stream for IEB as we want to split the data into 3 topics based on PRU.



