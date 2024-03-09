Load balancing is done to make sure that all app server receives equal or right amount of request, without overburdening any one server.

Advantages:

1. Increase Availability
2. Increase throughput
3. SSL termination
4. compression

To have high availability, we create multiple instance of server, but we have to make sure all server instance receive equal amount of request, so achieve this we use load balancing.

But if we see having single load balancer acts as single point of failure

![[load balancer -1.png]]

SO we can use passive back up load balancer.

in this approach we have 2 load balancer, load balancer 1 is active and will redirect and route all request, and the passive load balancer will do everything except routing. so when active LB goes down, then passive will take over and resume the request routing.

Here we can configure both LB with same IP address.

![[diagram-export-19-01-2024-14_50_35.png]]


We can also use DNS based load balancing.
We can configure DNS to return ip address of n number of LB this way for every request DNS can return direct LB ips and traffic can route based on that

![[diagram-export-19-01-2024-14_56_09.png]]
