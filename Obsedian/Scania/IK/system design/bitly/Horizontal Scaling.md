Reasons we may go to horizontal scaling

- [ ] Check how much data needs to be stored, May need to scale DB and cache tier if the size of data is too big.
- [ ] f the request per second is too high then we need to scale for throughput.
- [x] If the response time is too low, then we need to scale. 
- [ ] Availability and reliability in case of fault
- [x] GeoLocation, To minimize network latency e may use more than 1 machine.
- [x] Hotspots: Disproportionately high traffic on certain data, like celebrity tweet etc,

## we are not consider low response time in this case is because, its a very simple operations


Metrics for URL shortner is below link
## [[IK/system design/bitly/Main#^68ace5]]


# Lets do the calculation

### Requirement
1. Store data for 3 years
2. Number of reads per second is 8000
3. Number of write is 70


general formula is
### DB size = RPS * B * T
RPS = number of request per second
B = Size of each record
T = time duration for which size has to be calculated.

### lets calculate RPS
 as per the requirement , we have 70 request per second.
 so **Q= 70**

### Lets calculate B

the table has 2 entries
long url will have 2048 char == 2 KB == 10^3
short url will have 6 char == 0.05kb
 B = total size per record is 2 KB

### Lets calculate T for 3 years as per requirement
number of days in a year = 365
Number of seconds in a year = 365 * 24* 60*60 = 864000. lets approx to 1000000
Number of records in 3 years = from metrics give = 3 * 3 = 9, but approx 10 billion = 10 ^8
# DB size = 70 * 2 * 10^3 * 10 * 10^8 =  20 TB


Ideally we will have server with 3 to 4 TB as hard disk space, so we will have  20/ 4 = 5 servers


It is the same for cache, Ideally we will have a server with 128 mb of RAM.

SO should we have 20TB / 128 GB

## No, we should aim to have 10% of data in cache

10% of 20 TB =. 2 TB

2000 GB / 128 = 15 to 17 servers.


# Scaling for throughput

x = time in ms to read or process a given request
how many requests per second

every second has 1000 ms = 1000 / x

every system has 8 to 12 core an each core can handle 8 threads per core
so every server can have 12 * 8 = 96 = 100 threads per machine

if single thread can handle 1000 / x RPS, then
total machine can handle.

100 * 1000 / x

But generally we can only get 30 to 40 % CPU utilization

so divide this by 30 %

## ((100 * 1000) / x) * 0.3 = 100000 * 0.3 = 30000 RPS

if db access takes 10 ms per request, then 
total number of transaction per second = 30000 / 10 = 3000 RPS
cache request tales 2 ms = 30000 / 2 = 15000 RPS
App server tales 1ms. =30000 / 1 = 30000 RPS








