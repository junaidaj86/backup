![[cache]]

## Good cache can increase throughput of the system. 
We should try to achieve atleast 90 to 95 percent of hit should be from cache.

Cache is stored in RAM and it has finite memory, So when the cache increases beyond its capacity we have to plan to remove some cache.

There are many strategy to handle this
1> LRUC least recently used cache
2> First in first out 
3> etc...

## Caching stratergy
1. Cache aside : here we dont write in cache, we write in DB, then when read request comes, cache will read from db
2. Read -through



