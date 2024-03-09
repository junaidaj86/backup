Sharding or partitioning involves dividing a large database into smaller ones based on specific keys or criteria.

For instance, consider our application with a data volume of 12TB. We determine the number of shards or partitions by dividing the total data volume by the size of each community server. In this case:

12TB / 1TB (size of each community server) = 12 shards

To handle the distribution of requests effectively, we implement a partition-aware load balancer. This load balancer ensures that requests are directed to the appropriate shards based on the partitioning scheme in use.
![[Excalidraw/Sharding]]

## replication of shrads

replication happens irrespective if the db is sharded or not.
Replication is used to server many read request.

If the write happens on [[shard 1]] , then the data gets replicated in other shards, if the read query is not very huge, but if its very huge, we replicate them into many individual DB

## Determine number of shards

1. If its only storage based = Best practise to have 1 shard per 1 TB
2. If its QPS based, then find how many QPS we should support, then find max QPS per machine. Total = QPS total / max QPS per machine
