# Usecase 1 : When the application is read heavy

![[Drawing 2024-01-26 13.45.41.excalidraw]]

Imagine a write request comes to load balancer, load balancer redirects the request to DB1.
Now if we get a read request for the same payload which was written, and load balancer redirect it to DB2, then there it wont find the data.

So to avoid this we have to replicate the data in every DB.

### we also have to consider that application is read heavy.

There is a solution called as 
### Single leader data replication

In this approach, a single database (DB1) functions as the master or leader, while the remaining databases act as followers. The load balancer is responsible for directing **write** requests to the master (DB1) and routing read requests to the followers. After a write operation is executed on the master, followers synchronize with the change log to update their respective databases. This synchronization process introduces a delay, as followers may take some time to reflect the changes made by the master.



### issues

In this strategy, we achieve high throughput at the expense of immediate and highly consistent reads. If a read request follows a write request before the changes are fully propagated, users may not receive the updated data immediately. However, over time, the data consistency improves, demonstrating ### **[eventual consistency]**.

# Usecase 2: Multi leader data replication

Consider a scenario with two data centers, one located in Africa and the other in Asia. In a single leader and follower pattern where the leader is in Asia, if a write request originates from Africa, the delay in writing from Africa to Asia is substantial. Additionally, the propagation of updates to all followers also incurs a significant time delay.

To mitigate this, adopting a multi-leader and follower pattern is recommended.

![[Multi leader replica]]


In this specific scenario, there are two leaders—one based in Africa and the other in Asia. When a request originates from Africa, the African leader manages the write request and disseminates it to all other databases. Conversely, if the request comes from Asia, the leader in Asia handles the write request.

### Issue

What occurs when there are two concurrent write requests for a single key? In such a situation, Asia and Africa may end up with different values. To mitigate this, we employ UTC to compare timestamps and determine the latest record, ensuring consistency across regions.


## Usecase 3:  Leaderless data replication with Qurum read and writes:


A leaderless database setup, also known as a distributed or peer-to-peer database architecture, is a configuration where there is no single designated node (leader) that coordinates and directs the actions of the entire database cluster. Instead, all nodes in the cluster are treated as equals, and they collectively contribute to the distributed data storage and processing.

Key characteristics of a leaderless database setup:

1. **Decentralized Control:**
   - No specific node acts as a central authority or leader. Each node is capable of handling read and write requests independently.

2. **Data Distribution:**
   - Data is distributed across multiple nodes in the cluster. Each node is responsible for a subset of the data, and there is no single point of failure.

3. **Autonomous Nodes:**
   - Nodes operate autonomously and can make decisions locally. They don't rely on a central coordinator for database operations.

4. **High Availability:**
   - Due to the decentralized nature, leaderless databases often exhibit high availability. If one node fails, other nodes can continue serving requests.

5. **Scalability:**
   - The architecture supports horizontal scalability by adding more nodes to the cluster. This allows the system to handle increased load and storage requirements.

6. **Eventual Consistency:**
   - Leaderless databases often embrace eventual consistency, meaning that after a certain period, all replicas of a piece of data will converge to the same state, even if there are temporary inconsistencies.

Example of a leaderless database system:

**Apache Cassandra:**
   - Cassandra is a NoSQL database designed for scalability and high availability. It follows a leaderless architecture, distributing data across multiple nodes in a ring-like fashion.
   - Each node in a Cassandra cluster is equal and can independently handle read and write requests.
   - Cassandra achieves fault tolerance by replicating data across nodes. If one node goes down, data can still be retrieved from other replicas.
   - Cassandra uses a distributed, decentralized mechanism for consensus, often referred to as the gossip protocol, to maintain cluster metadata and detect failures.

In summary, leaderless databases, exemplified by systems like Apache Cassandra, provide a scalable and fault-tolerant solution by distributing control and data across multiple nodes. This architecture is well-suited for applications requiring high availability, horizontal scalability, and decentralized decision-making.



