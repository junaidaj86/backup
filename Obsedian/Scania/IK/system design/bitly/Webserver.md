Imagine er have a web application, this application is nothing but our url shorter application.
We deploy this in our multi core machine, since the application will be using 1 cpu or process, other cores will be free. To utilise it, we will deploy as many instance of application as the number of CPU.

## in 4 core cpu, we will deploy 4 instance.

Now since we have many instance and counter and hash table is stored inside each instance. , if we make any change in one instance, it is not visible ion other instance.

## so we store counter and url short key and long url in database

````mermaid
graph TD
  subgraph Database
    db[Database]
  end

  subgraph ApplicationServer1
    as1[App Server 1]
  end

  subgraph ApplicationServer2
    as2[App Server 2]
  end

  subgraph ApplicationServer3
    as3[App Server 3]
  end

  subgraph ApplicationServer4
    as4[App Server 4]
  end

  as1 -->|Query/Update| db
  as2 -->|Query/Update| db
  as3 -->|Query/Update| db
  as4 -->|Query/Update| db

  style db fill:yellow,stroke:black,stroke-width:2px
  style as1 fill:#green,stroke:#2E86C1,stroke-width:2px

````


Now if there is load of load coming to application we need a load balancer, which can distribute the load.

````mermaid
graph TD
  subgraph Database
    db[Database]
  end

  subgraph ApplicationServer1
    as1[App Server 1]
  end

  subgraph ApplicationServer2
    as2[App Server 2]
  end

  subgraph ApplicationServer3
    as3[App Server 3]
  end

  subgraph ApplicationServer4
    as4[App Server 4]
  end

  subgraph LoadBalancer
    lb[Load Balancer]
  end

  lb -->|Load Balance| as1
  lb -->|Load Balance| as2
  lb -->|Load Balance| as3
  lb -->|Load Balance| as4

  as1 -->|Query/Update| db
  as2 -->|Query/Update| db
  as3 -->|Query/Update| db
  as4 -->|Query/Update| db

  style db fill:#F2F2F2,stroke:#D8D8D8,stroke-width:2px
  style as1, as2, as3, as4 fill:#CEF6F5,stroke:#2E86C1,stroke-width:2px
  style lb fill:#58D68D,stroke:#2E6A4F,stroke-width:2px

````

Since our application doesnot store any state, which will impact the application, our application is stateless.

To fasten the processing we can add a cache layer inside our app server, this will maintain the key value pair which are frequently accessed, this will fasten up the processing.

````mermaid
graph TD
  subgraph Database
    db[Database]
  end

  subgraph ApplicationServer1
    as1[App Server 1]
    cache1[Cache]
  end

  subgraph ApplicationServer2
    as2[App Server 2]
    cache2[Cache]
  end

  subgraph ApplicationServer3
    as3[App Server 3]
    cache3[Cache]
  end

  subgraph ApplicationServer4
    as4[App Server 4]
    cache4[Cache]
  end

  subgraph LoadBalancer
    lb[Load Balancer]
  end

  lb -->|Load Balance| as1
  lb -->|Load Balance| as2
  lb -->|Load Balance| as3
  lb -->|Load Balance| as4

  as1 -->|Query/Update| cache1
  as2 -->|Query/Update| cache2
  as3 -->|Query/Update| cache3
  as4 -->|Query/Update| cache4

  cache1 -->|Query/Update| db
  cache2 -->|Query/Update| db
  cache3 -->|Query/Update| db
  cache4 -->|Query/Update| db

  style db fill:#F2F2F2,stroke:#D8D8D8,stroke-width:2px
  style as1, as2, as3, as4 fill:#CEF6F5,stroke:#2E86C1,stroke-width:2px
  style cache1, cache2, cache3, cache4 fill:#FAD02E,stroke:#D4AC0D,stroke-width:2px
  style lb fill:#58D68D,stroke:#2E6A4F,stroke-width:2px

````



