|   |   |   |   |   |
|---|---|---|---|---|
|Total client connections|1000|1000|22,500 [[1]](https://docs.confluent.io/cloud/current/clusters/cluster-types.html#id12)|per CKU|
|Connection attempts (per second)|80|80|1,250 [[1]](https://docs.confluent.io/cloud/current/clusters/cluster-types.html#id12)|per CKU|

### Selecting cluster type

With standard, confluent allows 80 connections per second, and enterprise 1250 is supported.
for dedicated 500 per CKU per second and total of 9000 .

We have 4 different types of cluster in confluent cloud
1> Basic
2> Standard
3> Enterprise = 1250 connection per second and total of 22500
4> Dedicated = 500 connection per second per CKU and total of 9000 per cku

We have to select 1 of the above cluster type


### Client Quotas is available with Dedicated and not with Enterprise, standard.

### KsqlDB is available with all except Standard.

### self managed encryption key is available with Dedicated but not with others

### public networking is not available with Standard

### What are the anticipated metrics for inbound (ingress) and outbound (egress) traffic?

### message size is 20 mb for dedicated but for others its 8 mb

## Supported cluster types

A cluster link sends data from a “source cluster” to a “destination cluster”. The supported cluster types are shown in the table below.

Unsupported cluster types and other limits are described in [Limitations](https://docs.confluent.io/cloud/current/multi-cloud/cluster-linking/index.html#cloud-cluster-linking-limits).

|Source Cluster Options|Destination Cluster Options|
|---|---|
|- [Dedicated Confluent Cloud cluster](https://docs.confluent.io/cloud/current/clusters/cluster-types.html#dedicated-cluster) with internet networking<br>- [Standard Confluent Cloud cluster](https://docs.confluent.io/cloud/current/clusters/cluster-types.html#standard-cluster)<br>- [Basic Confluent Cloud cluster](https://docs.confluent.io/cloud/current/clusters/cluster-types.html#basic-cluster)|Any Dedicated Confluent Cloud cluster|
|- [Dedicated Confluent Cloud cluster](https://docs.confluent.io/cloud/current/clusters/cluster-types.html#dedicated-cluster) with private networking<br>- [Enterprise Confluent Cloud cluster](https://docs.confluent.io/cloud/current/clusters/cluster-types.html#enterprise-cluster)|Dedicated Confluent Cloud cluster under certain networking circumstances, see [Manage Private Networking for Cluster Linking on Confluent Cloud](https://docs.confluent.io/cloud/current/multi-cloud/cluster-linking/private-networking.html#cloud-cluster-link-private-networking).|
|Apache Kafka® 2.4+ or Confluent Platform 5.4+ with public internet IP addresses on all brokers|Any Dedicated Confluent Cloud cluster|
|Kafka 2.4 or later without public endpoints|A Dedicated Confluent Cloud cluster with VPC Peering, VNet Peering, or PrivateLink|
|Confluent Platform 7.1+ (even behind a firewall)|Any Dedicated Confluent Cloud cluster under certain networking circumstances, see [Manage Private Networking for Cluster Linking on Confluent Cloud](https://docs.confluent.io/cloud/current/multi-cloud/cluster-linking/private-networking.html#cloud-cluster-link-private-networking).|
|- Any [Dedicated Confluent Cloud cluster](https://docs.confluent.io/cloud/current/clusters/cluster-types.html#dedicated-cluster) under certain networking circumstances, see [Manage Private Networking for Cluster Linking on Confluent Cloud](https://docs.confluent.io/cloud/current/multi-cloud/cluster-linking/private-networking.html#cloud-cluster-link-private-networking).<br>- [Enterprise Confluent Cloud cluster](https://docs.confluent.io/cloud/current/clusters/cluster-types.html#enterprise-cluster)|Confluent Platform 7.0+ (even behind a firewall)|




### Multi-tenancy:

- **Definition:** Running multiple distinct applications on a single Kafka cluster.
    
- **Why Multi-tenancy:**
    
    1. **Lower Cost:** Sharing a single cluster across workloads minimizes fixed costs.
    2. **Simpler Operations:** Managing one cluster simplifies access controls and credentials.
    3. **Greater Reuse:** Teams can reuse existing data by sharing the cluster, delivering value more quickly.

### Application Identity and Principals:

- **Principal Definition:** A unique identity for each tenant, enabling granular monitoring and management.
    
- **Ways to Assign Principals:**
    
    1. **Service Accounts:**
        - Represent application principals programmatically accessing Confluent Cloud.
        - One service account per producer application (or consumer group) is recommended.
        - Can have one or more API keys.
    2. **Identity Pools:**
        - Represent either a single application or a group of applications.
        - Seen as a unique principal inside Confluent Cloud.
        - Support metric visibility and Client Quotas at the identity pool level.

### Monitoring Metrics by Principal:

- **Metrics API:**
    
    - Provides actionable operational metrics about Confluent Cloud deployment.
    - Supports labels, with `principal_id` enabling metric filtering by a specific application.
    - Enables monitoring performance characteristics of specific applications, offering insights into cluster utilization.
- **Metrics Labeled with `principal_id`:**
    
    1. `io.confluent.kafka.server/request_bytes`
    2. `io.confluent.kafka.server/response_bytes`
    3. `io.confluent.kafka.server/active_connection_count`
    4. `io.confluent.kafka.server/request_count`
    5. `io.confluent.kafka.server/successful_authentication_count`

### Client Quotas:

- **Definition:** Cloud-native implementation of Kafka Client Quotas to control application usage.
    
- **Differences from Apache Kafka Quotas:**
    
    1. Apply to Service Accounts or identity pools.
    2. Managed by calling the Confluent Cloud API.
    3. Enforced at the cluster level (not broker level).
- **Key Aspects:**
    
    1. Defined on the cluster level and automatically distributed to the correct brokers.
    2. Can apply to one or more principals.
    3. Each principal assigned to a quota receives the full amount of the quota (not shared).
    4. Defines a throughput maximum but doesn't guarantee a throughput floor.
- **Use Cases:**
    
    - Rate-limiting distinct applications.
    - Creating quotas for different tiers of service.
- **Examples:**
    
    1. Cluster default quota is 10 MBps. A specific 5 MBps quota for Principal 1 is applied. Principal 1 can produce at most 5 MBps.
    2. Cluster default quota is 10 MBps. A specific 50 MBps quota for Principal 1 is applied. Principal 1 can produce at most 50 MBps.
- **Common Approaches:**
    
    - Creating a default quota for specified throughput.
    - Creating quotas for different application priorities or tiers of service.

This setup allows for efficient resource utilization, monitoring, and control over the behavior of applications in a multi-tenant environment on Confluent Cloud.


### confluent support Lets encrypt certificates

https://docs.confluent.io/cloud/current/cp-component/clients-cloud-config.html







