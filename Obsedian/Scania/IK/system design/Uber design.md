## define requirements
## define microservice

## define api
## define data model
## define how much space is required for 3 years

## define how many server are required to achieve required TPS

## Gather metrics from interviewer



Uber is a ride booking service

First a driver has to register his Car
User then register using the App.
Car will call an update service to send their locations
We have to show all drivers within some limit to the user
## Questions to ask:

1. How many cars are registered?
2. How many customers are registered?
3. How many trips per month?

## Functional requirements
1.  Rider: find all the drivers near by
2.  Rider: Request a ride, driver matching
3. Driver: Should be able to see rider req, confirm or deny the req
4. Real time tracking of driver and trip
5. Rider should be able to cancel the trip

## Defining microservice
1. Vehicle tracking service
2. Trip management service
3.  Account management service


## Microservice

1. Search near by rider (currentLocation, destination, cust_id) returns list if drivers
2. requestRide(riderId, )
3. vehicalTracking(driverId, location)

## Data Model
![[Uber Data Model]]

Driver table sizing
we have 10 million drivers
size of each row = int + float + float = 4 + 4 + 4 = 12 bytes
for 10 million record we would need = 12 bytes * 10 million = 12 * 100,00000 = 120000000

1 mega byte = 10^6 byte
120000000 = 12^7 

12^7 / 10^6 = 120 MB
driver table for 1 year would require 120 MB for 5 years = 600 MB



Rider table sizing
we have 40 million riders
size of each row = int + float + float = 4 + 4 + 4 = 12 bytes
for 10 million record we would need = 12 bytes * 40 million = 12 * 400,00000 = 480000000
1 mega byte = 10^6 byte
120000000 = 48 * 10^7 = 

48 * 10^7 / 10^6 = 480 MB
driver table for 1 year would require 480 MB for 5 years = 2.5 GB

Trip table sizing 
we have 80 million trips per month
size of each row = int + float + float = 4 + 4 + 4 +4+4 = 20 bytes
for 80 million records we would need 20 bytes * 80 million = 20 * 800,00000 = 1600000000
1 mega byte = 10^6 byte
1600000000 = 16 * 10^8 byte
16 * 10^8 / 10^6 = 16 * 10^2 MB
1600 MB = 1.6 GB

For 1 month we need 1.6 GB and for years we need 1.6 * 12 = 19 GB

for 5 years we need 96 GB


![[world map segment]]

the above grip is nothing but the world grid divided by 1 mile square.
### Earth has 330 million miles space.
## if we divide by 1 mile grid then we will have 330 million rows.
so we will have a static table called earth segment with locationId for every 1 mile square grid.
![[earth segment table]]
So, the total storage size per record would be:

TIn the Uber system design, the storage requirements for each record are calculated as follows:

**Total Storage Size per Record** = Integer Size + (Float Size × 2)

**Total Storage Size per Record** = *(4 bytes) + (4 bytes × 2)*

**Total Storage Size per Record** = *4 bytes + 8 bytes*

**Total Storage Size per Record** = *12 bytes*

To determine the total data required to store 330 million records:

**Total Data Required** = Total Storage Size per Record × Total Number of Records

**Total Data Required** = *12 bytes × 330,000,000*

**Total Data Required** = *3,960,000,000 bytes*

**Total Data Required** = *3.96 gigabytes (GB)*



## Throughput

We have 10 million drivers.
They update database every 5 seconds
so we have 10 million / 5 = 2 million updates per seconds.

1 commodity server has handles 1000 action / time
we have 100 - 200 threads per server, lets asume its 100 thtreads = 100000 action / time unit

but cpu runs at 30 to 40 percent so assume 30000 action / time unit

lets assume each action takes 20 ms so tps per server = 30000 / 20 = 1500 tps per server

## Total server = 2 million / 1500 = 2000000 / 1500 = 1350 servers









When a rider opens the Uber app to find a cab to reach their destination, the system retrieves the rider's current location and identifies the corresponding location ID within the world segment, returning the Segment ID.
World segments are stored in database and shared as per geo location.

Similarly, drivers continuously update their current locations. Upon receiving a driver's current location, the system stores this data in a Kafka queue and updates the driver table with the updated location.

In addition to the driver table, the system maintains two more internal records:

1. **Driver to Location Reverse Index**: This index facilitates quick retrieval of drivers based on their current location. It maps each driver's ID to the corresponding location or segment ID, enabling efficient driver allocation and matching with rider requests. This index will be stored in a distributed key-value store for fast access and scalability.

2. **Driver and Location Forward Index**: This index provides a reverse mapping, linking each location or segment ID to the drivers currently present in that area. It helps in optimizing driver allocation by identifying areas with high demand or insufficient supply, allowing for strategic deployment of drivers to meet rider demands effectively. This index will also be stored in a distributed key-value store for efficient access.









