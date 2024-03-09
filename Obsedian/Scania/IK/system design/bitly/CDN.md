imagine we have an application which has more read and less write.
Most of the data which the application serves to the reader is static data like videos and images.

We have 2 data centre across different region, one DC is used for write and the others are used for read.

If the users in different region wants to read the data, they have to go cross region to read it, which will increase the response time.

SO what we can do is, have one or 2 DC as write enabled and others. should be only sued for reading.
But there should not be any DB in read region, but instead only have cache which has 90 to 95 % of traffic. SO when user wants to read the content, it can be served from read servers adn this decreases response time.

## this is called as CDNs

![[Excalidraw/CDN]]

When the clients in region A request for content, of the content is not present, then this app pull data from main Region and stores in cache. But when other users request same content, then we use the cache and serve them.

