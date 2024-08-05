

How to store passwords safely in the database and how to validate a password?
According to OWASP guidelines, “a salt is a unique, randomly generated string that is added to each password as part of the hashing process”.

How to store a password and salt?

    the hash result is unique to each password.
    The password can be stored in the database using the following format: hash(password + salt).




Microservices: Microservices are designed and deployed in different domains. Each domain has its own database. The API gateway talks to the microservices via REST API or other protocols, and the microservices within the same domain talk to each other using RPC (Remote Procedure Call).


Use separate data storage for each microservice
Keep code at a similar level of maturity
Separate build for each microservice
Assign each microservice with a single responsibility
Deploy into containers
Design stateless services
Adopt domain-driven design
Design micro frontend
Orchestrating microservices


Multiplexing
a system or signal involving simultaneous transmission of several messages along a single channel of communication.

Encrypt and Decrypt

Encryption and decryption are processes used to secure data by converting it into a format that is unreadable without the appropriate key.

    Encrypt:
        Purpose: To convert plain text (readable data) into cipher text (unreadable data) to protect it from unauthorized access.
        Process: Uses an encryption algorithm and a key to transform the data.
        Example: Encrypting a message "Hello" using AES encryption with a key might produce something like "U2FsdGVkX1+fOeVJrHlQzg==".

    Decrypt:
        Purpose: To convert cipher text back into plain text using a decryption algorithm and the appropriate key.
        Process: Uses a decryption algorithm and a key (which must be the same as or a corresponding key to the one used for encryption).
        Example: Decrypting "U2FsdGVkX1+fOeVJrHlQzg==" using the same AES key will give back the original message "Hello".

Encode and Decode

Encoding and decoding are processes used to transform data into a different format for the purposes of data transmission, storage, or compatibility.

    Encode:
        Purpose: To convert data into a specific format using a particular scheme so that it can be properly transmitted or stored.
        Process: Uses an encoding algorithm to transform the data.
        Example: Base64 encoding the string "Hello" produces "SGVsbG8=".

    Decode:
        Purpose: To convert encoded data back into its original format.
        Process: Uses a decoding algorithm to reverse the encoding.
        Example: Base64 decoding "SGVsbG8=" returns the original string "Hello".

Serialize and Deserialize

Serialization and deserialization are processes used to transform data structures or objects into a format that can be easily stored or transmitted and then reconstructed.

    Serialize:
        Purpose: To convert an object or data structure into a format that can be easily stored or transmitted.
        Process: Uses a serialization algorithm to convert the object into a byte stream, JSON, XML, etc.
        Example: Serializing a Python dictionary {"name": "John", "age": 30} to JSON format produces the string '{"name": "John", "age": 30}'.

    Deserialize:
        Purpose: To convert serialized data back into its original object or data structure format.
        Process: Uses a deserialization algorithm to transform the byte stream, JSON, XML, etc., back into the original object.
        Example: Deserializing the JSON string '{"name": "John", "age": 30}' back into a Python dictionary produces {"name": "John", "age": 30}.

Encryption/Decryption: Secure communications, protecting sensitive data, authentication.
Encoding/Decoding: Data transmission over the internet, data storage, converting between different data formats.
Serialization/Deserialization: storing application data, data interchange between different systems, network communication.


Non functional requirements

Availability: Our system should be highly available.
Durability: The data, once uploaded, shouldn’t be lost unless users explicitly delete that data.
Scalability: The system should be capable of handling billions of blobs.
Throughput: For transferring gigabytes of data, we should ensure a high data throughput.
Reliability: Since failures are a norm in distributed systems, our design should detect and recover from failures promptly.
Consistency: The system should be strongly consistent. Different users should see the same view of a blob.


The Open Systems Interconnection (OSI) 
Summary of Layer Functions:

Physical Layer: Concerned with the physical connection between devices and the transmission of 
raw data bits.
Data Link Layer: Responsible for node-to-node data transfer and error detection/correction.
Controls how devices on the network gain access to the data and permission to transmit it.
Network Layer: Manages the routing of data packets between devices on different networks.
Transport Layer: Ensures reliable data transfer with error recovery and flow control.
Session Layer: Manages sessions or connections between applications.
Presentation Layer: Translates, encrypts, and compresses data for the application layer.
Application Layer: Provides network services and applications to the end-user.

Communication Between Layers:

Each layer only interacts directly with the layers immediately above and below it.
Data is encapsulated with relevant protocol information as it moves down the 
layers and decapsulated as it moves up.

Example of Data Flow:

When you access a website:

Application Layer: Your browser (HTTP request) requests a webpage.
Presentation Layer: The request is formatted and encrypted.
Session Layer: A session is established between your computer and the web server.
Transport Layer: The data is broken into segments (TCP/UDP).
Network Layer: Each segment is encapsulated in a packet with a destination IP address.
Data Link Layer: Each packet is framed with a MAC address for the next-hop network device.
Physical Layer: The frames are transmitted as bits over the physical medium (e.g., Ethernet)

Application Layer Protocols

    HTTP (Hypertext Transfer Protocol):
        Purpose: Used for transmitting web pages over the internet. It defines how messages are formatted and transmitted, and how web servers and browsers should respond to various commands.
        Port: 80
        Example: When you type a URL in your web browser, it sends an HTTP request to the server to fetch the web page.

    HTTPS (Hypertext Transfer Protocol Secure):
        Purpose: An extension of HTTP that uses SSL/TLS to encrypt data for secure communication over a computer network.
        Port: 443
        Example: Online banking and shopping websites use HTTPS to securely transfer sensitive data like credit card information.

    FTP (File Transfer Protocol):
        Purpose: Used for transferring files between a client and server on a computer network.
        Ports: 20 (data transfer), 21 (control)
        Example: Uploading files to a web server or downloading files from a server.

    SMTP (Simple Mail Transfer Protocol):
        Purpose: Used for sending emails from clients to servers or between servers.
        Port: 25 (unencrypted), 587 (encrypted with STARTTLS)
        Example: Sending an email from an email client like Outlook or Gmail to an email server.

    IMAP (Internet Message Access Protocol):
        Purpose: Used by email clients to retrieve messages from a mail server, allowing for managing and synchronizing email across multiple devices.
        Port: 143 (unencrypted), 993 (encrypted)
        Example: Accessing your email from multiple devices like a phone and a laptop.

    POP3 (Post Office Protocol version 3):
        Purpose: Another protocol used by email clients to retrieve emails from a server. Unlike IMAP, it typically downloads and deletes the email from the server.
        Port: 110 (unencrypted), 995 (encrypted)
        Example: Accessing your email on a single device and not synchronizing with other devices.

Transport Layer Protocols

    TCP (Transmission Control Protocol):
        Purpose: Provides reliable, ordered, and error-checked delivery of a stream of data between applications running on hosts communicating via an IP network.
        Example: Web browsing(HTTP/HTTPS), email (SMTP, IMAP, POP3), file transfers(FTP) rely on TCP for data integrity and reliability.

    UDP (User Datagram Protocol):
        Purpose: Provides a simpler, connectionless communication model with minimal protocol mechanisms. It does not guarantee delivery, order, or error-checking, making it faster but less reliable than TCP.
        Example: Streaming media, online gaming, and voice over IP (VoIP) where speed is more critical than reliability.

Network Layer Protocols

    IP (Internet Protocol):
        Purpose: Responsible for addressing and routing packets of data so they can travel across networks and arrive at the correct destination.
        Example: Every device connected to the internet has a unique IP address used for identifying and communicating with other devices.

Data Link Layer Protocols

    Ethernet:
        Purpose: Defines the wiring and signaling standards for the physical layer and data link layer’s protocols for controlling access to the physical transmission medium.

Physical Layer Protocols

    Wi-Fi (IEEE 802.11):
        Purpose: Standards for wireless local area networks (WLANs). It defines the protocols for communication over wireless radio frequencies.

API
By Communication Style

    REST APIs (Representational State Transfer):
        Description: Use HTTP requests to perform CRUD operations (Create, Read, Update, Delete) and follow REST architectural principles.
        Examples: JSONPlaceholder API for testing, GitHub API.
    SOAP APIs (Simple Object Access Protocol):
        Description: Use XML for messaging and follow strict standards. SOAP APIs are highly secure and reliable.
        Examples: Payment processing APIs like those from PayPal, some financial services APIs.
    RPC APIs (Remote Procedure Call):
        Description: Invokes methods remotely. It can be based on JSON (JSON-RPC) or XML (XML-RPC).
        Examples: Some internal APIs in distributed systems, certain microservices architectures.

By Use Case

    Web APIs:
        Description: Accessed over a web-based communication protocol, typically HTTP.
        Examples: Google Maps API, YouTube API.
    Library-based APIs:
        Description: Provided by software libraries or frameworks, allowing access to their functionality.
        Examples: jQuery for JavaScript, TensorFlow for machine learning.
    Database APIs:
        Description: Interact with databases, performing operations such as querying, updating, and managing data.
        Examples: SQL-based APIs like JDBC (Java Database Connectivity), MongoDB APIs.

By Protocol

    HTTP/HTTPS APIs:
        Description: Use HTTP or HTTPS for communication.
        Examples: Most modern web APIs, such as REST APIs.
    WebSocket APIs:
        Description: Facilitate real-time communication between client and server over a single, long-lived connection.
        Examples: Real-time chat applications, live sports updates.
    GraphQL APIs:
        Description: Allows clients to request exactly the data they need. Developed by Facebook.
        Examples: GitHub GraphQL API.

By Interaction Type

    Synchronous APIs:
        Description: The client sends a request and waits for a response from the server.
        Examples: Typical REST API calls.
    Asynchronous APIs:
        Description: The client sends a request and continues processing. The server responds when ready, often via a callback mechanism.
        Examples: Webhooks, some messaging APIs.

communication between a client and a server over HTTP
AJAX polling
AJAX polling is a technique where the client repeatedly requests data from the server at regular intervals.

Long polling
Long polling improves on traditional polling by keeping the connection open until the server has new information to send.

Websocket
WebSockets provide a full-duplex communication channel over a single, long-lived connection.
The client establishes a WebSocket connection to the server using the WebSocket handshake protocol.
Once the connection is established, both the client and the server can send and receive messages at any time.
The connection remains open, allowing for continuous real-time communication.

server send event over http
The client establishes an HTTP connection to the server with an EventSource object.
The server keeps the connection open and sends updates as they become available.
The client receives updates in real-time without needing to send repeated requests.
Unidirectional: Only the server can send updates to the client.

non functional charahteristics

Availability is the percentage of time that some service or infrastructure is accessible 
to clients and is operated upon under normal conditions. For example, if a service has
100% availability, it means that the said service functions and responds as intended
(operates normally) all the time.

availability = Total time - sum of down time // Total time

Reliability, R, is the probability that the service will perform its functions for a
specified time. R measures how the service performs under varying operating conditions.
We often use mean time between failures (MTBF) and mean time to repair (MTTR) as metrics to measure R. 

MTBF = Total time - sum of down time // total number of failures
MTTR = Total maintainance time // total number of repairs

Scalability is the ability of a system to handle an increasing amount of workload
 without compromising performance.

Maintainability, M, is the probability that the service will restore its functions
within a specified time of fault occurrence. M measures how conveniently and swiftly
the service regains its normal operating conditions.
For example, suppose a component has a defined maintainability value of 95% for half an hour.
In that case, the probability of restoring the component to its fully active form in half an hour is 0.95.

MTTR = Total maintainance time // total number of repairs

Fault tolerance refers to a system’s ability to execute persistently even if one or more of its components fail.

Replication
One of the most widely-used techniques is replication-based fault tolerance.
With this technique, we can replicate both the services and data. 
We can swap out failed nodes with healthy ones and a failed data store with its replica. 

Checkpointing
Checkpointing is a technique that saves the system’s state in stable storage for later 
retrieval in case of failures due to errors or service disruptions.

A state is consistent in which all the individual processes of a system have a consistent
view of the shared state or sequence of events that have occurred in a system.

Back-of-the-envelope Numbers
The number of concurrent TCP connections a server can support

The number of requests per second (RPS) a web, database, or cache server can handle

The storage requirements of a service

IO bandwidth calculations

Server types
Web servers
Web servers are the first point of contact after load balancers. 
Depending on the service that’s offered, the memory and storage 
resources in web servers can be small to medium. However, such servers 
require good processing resources.

Application servers
Application servers run the core application software and business logic.
They can require extensive computational and storage resources. 

Storage servers
Blob storage: This is used for its encoded videos.

Temporary processing queue storage: This can hold a few 
hundred hours of video content uploaded daily to YouTube for processing.

Bigtable: This is a specialized storage used for storing a large number of thumbnails of videos.

Relational database management system (RDBMS): This is for users’ and videos’ 
metadata (comments, likes, user channels, and so on).

Component
	
Latencies

L1 cache reference 0.9(nanoseconds)

L2 cache reference 2.8(nanoseconds)

L3 cache reference 12.9(nanoseconds)

Main memory reference 100(nanoseconds)

Read 1 MB sequentially from memory (9 microseconds)

Read 1 MB sequentially from SSD (200 microseconds)

Round trip within same datacenter (500 microseconds)

Read 1 MB sequentially from SSD with speed ~1GB/sec SSD (1 milliseconds)

Disk seek (4 milliseconds)

Read 1 MB sequentially from disk (2 milliseconds)

Send packet SF->NYC 71 milliseconds
	
Important Rates (QPS)
QPS handled by MySQL 1000

QPS handled by key-value store 10,000

QPS handled by cache server 100000-1M

CPU-bound request takes 1X time units to complete some work on a node, 
memory-bound workloads are an order of magnitude slower (10X), 
IO-bound workloads are two orders of magnitude slower (100X) than the CPU-bound workload.

Power of Two
10	1 Thousand	    1 Kilobyte	1 KB
20	1 Million	    1 Megabyte	1 MB
30	1 Billion	    1 Gigabyte	1 GB
40	1 Trillion	    1 Terabyte	1 TB
50	1 Quadrillion	1 Petabyte	1 PB
	
Algorithms of load balancers

Round-robin scheduling: In this algorithm, each request is forwarded to a server 
in the pool in a repeating sequential manner.

Weighted round-robin: If some servers have a higher capability of serving clients’ requests,
then it’s preferred to use a weighted round-robin algorithm. 

Least connections: we can use algorithms like least connections where
newer arriving requests are assigned to servers with fewer existing connections. 
LBs keep a state of the number and mapping of existing connections in such a scenario. 

Least response time: In performance-sensitive services, algorithms such as least 
response time are required. This algorithm ensures that the server with the least
response time is requested to serve the clients.

IP hash: Some applications provide a different level of service to users based on 
their IP addresses. In that case, hashing the IP address is performed to 
assign users’ requests to servers.

URL hash: It may be possible that some services within the application are provided
by specific servers only. In that case, a client requesting service from a URL is 
assigned to a certain cluster or set of servers. The URL hashing algorithm is used 
in those scenarios.

Stateful versus stateless LBs

a state is maintained to hold session information of different clients with hosting servers.
a state maintained across different load balancers is considered as stateful load balancing. 
Whereas, a state maintained within a load balancer for internal use is assumed as stateless load balancing.

Layer 4 Load Balancer:

    Scenario: Distributing incoming TCP connections for a database cluster.
    Decision: Routes traffic based on the destination IP and port, using a round-robin algorithm.

Layer 7 Load Balancer:

    Scenario: Managing HTTP traffic for a web application.
    Decision: Inspects the content of the incoming traffic, 
    including HTTP headers, cookies, URLs, and even the data payload.
    Can make decisions based on more granular information such as the requested URL,
    type of content, or user identity.

ACID in detail:

    Atomicity: A transaction is considered an atomic unit. Therefore, either all the statements 
    within a transaction will successfully execute, or none of them will execute.
    If a statement fails within a transaction, it should be aborted and rolled back.

    Consistency: At any given time, the database should be in a consistent state, and it
    should remain in a consistent state after every transaction. For example, 
    if multiple users want to view a record from the database, it should return a
    similar result each time.

    Isolation: In the case of multiple transactions running concurrently, they shouldn’t be 
    affected by each other. The final state of the database should be the same as the
    transactions were executed sequentially.

    Durability: The system should guarantee that completed transactions will survive permanently 
    in the database even in system failure events.

Quorum as a solution

A quorum in a distributed system is the minimal number of replicas on which a distributed operation 
(commit/abort) must be completed before proclaiming the operation’s success.

Selecting quorum number
We should select more than half of the replicas in the cluster. If there are R replicas in the cluster,
we should choose R/2+1 as a quorum number.

ZooKeeper

To track changes in the cluster, many distributed data systems need a separate management server
like ZooKeeper. Zookeeper keeps track of all the mappings in the network, and each node connects 
to ZooKeeper for the information. Whenever there’s a change in the partitioning, or a node is
added or removed, ZooKeeper gets updated and notifies the routing tier about the change.
HBase, Kafka and SolrCloud use ZooKeeper.

Partitioning secondary indexes by document in a database

This approach involves creating secondary indexes that are partitioned according
to the primary key or document ID, ensuring that the index entries related to a 
particular document are stored together. 

Partitioning secondary indexes by the term in a database
Distributing index entries across partitions based on terms helps balance the load, 
preventing any single partition from becoming a bottleneck.
Queries can be processed in parallel across multiple partitions, improving query performance and reducing latency.
For range queries (e.g., finding all emails starting with a particular letter), the partitioning scheme can be 
designed to keep related terms together, optimizing range query performance.

Data cardinality refers to the uniqueness of data values contained in a column (attribute) of a database.
High Cardinality:

    An attribute with high cardinality contains a large number of unique values.
    Examples: Social Security Numbers, email addresses, or user IDs.
Low Cardinality:

    An attribute with low cardinality contains a small number of unique values.
    Examples: Boolean fields (true/false), gender (male/female), or status (active/inactive).
Unique Cardinality:

    Every value in the column is unique.
    Examples: Primary keys, such as user IDs or order IDs.

Non-Unique Cardinality:

    Values in the column are not unique and may repeat.
    Examples: Country names in a customer table, product categories in an inventory table.

Indexing: Indexing is the organization and manipulation of data that’s done to facilitate fast and accurate information retrieval.

    High cardinality attributes are often indexed to improve query performance, as the index 
    can quickly narrow down search results.

Key-value stores are useful in many situations, such as storing user sessions in a
web application and building NoSQL databases.


Consistent hashing
Consistent hashing is an effective way to manage the load over the set of nodes. 
In consistent hashing, we consider that we have a conceptual ring of hashes from 00 to n−1,
where nn is the number of available hash values. We use each node’s ID, calculate its hash, 
and map it to the ring. We apply the same process to requests. Each request is completed by 
the next node that it finds by moving in the clockwise direction in the ring.

Use virtual nodes
We’ll use virtual nodes to ensure a more evenly distributed load across the nodes. 
Instead of applying a single hash function, we’ll apply multiple hash functions onto the same key.

Data versioning
To handle inconsistency, we need to maintain causality between the events

A vector clock is a mechanism for tracking causality and the partial ordering
of events in distributed systems. It helps in understanding the sequence and 
causality of events, allowing the system to determine whether two events are
causally related, concurrent, or if one event happened before another.

Handle temporary failures
Hinted Handoff is a useful mechanism for maintaining high availability and durability in 
distributed systems during transient node failures. It allows write operations to proceed 
even when some nodes are unavailable by storing hints for later delivery. However, it comes
with limitations such as storage overhead, complexity, potential delayed consistency, and
the risk of hinted replicas becoming unavailable before the hints are delivered.

"minimal churn" refers to a situation where there are few changes in the system's membership
over time. This means that the addition, removal, or failure of nodes (servers, computers, 
or other devices) within the network occurs infrequently. Minimal churn is a desirable condition
for many distributed systems because it simplifies the management and coordination of the nodes,
leading to more stable and predictable system behavior.

Handle permanent failures
Merkle tree
the values of individual keys are hashed and used as the leaves of the tree. There are hashes of their children in the parent nodes higher up the tree. There’s no need for synchronization if, for example, the hash values of two trees’ roots are the same and their leaf nodes are also the same.
Each node keeps a distinct Merkle tree for the range of keys that it hosts for each virtual node. The nodes can determine if the keys in a given range are correct. The root of the Merkle tree corresponding to the common key ranges is exchanged between two nodes. 
The disadvantage is that when a node joins or departs the system, the tree’s hashes are recalculated because multiple key ranges are affected.

Decentralized failure detection protocols 
involves updating and maintaining the membership list of nodes in the ring to effectively detect and manage node failures. This process ensures that all nodes in the system are aware of each other’s status and can take appropriate actions in case of failures.
Gossip Protocol:

Distributed systems often use gossip protocols to disseminate membership information and detect node failures.
Gossip protocols allow nodes to periodically exchange state information with a few other nodes, ensuring that knowledge about node status propagates throughout the system.

Nodes use heartbeats or periodic status checks to monitor the health of other nodes.
Handling Failures:

    When a node is detected as failed, the system needs to reassign its responsibilities to other nodes to maintain data availability and consistency.
    The membership list is updated to reflect the failure, and the information is propagated to all nodes.
    Hinted handoff and other replication mechanisms may be used to ensure data integrity during the failure period.

seed nodes are designated nodes in a distributed system that help maintain knowledge about the membership status of other nodes, such as whether they are up or down. We can define a set of nodes as seeds via a configuration service. This set of nodes is known to all the working nodes since they can eventually reconcile their membership with a seed.

a coordinator node is a node that takes on a central role in coordinating certain operations, such as handling client requests, managing distributed transactions, or ensuring consistency across the system. 
Request Handling:

    When a client sends a request to a distributed system, the coordinator node is often the first point of contact.
    The coordinator processes the request and determines how to distribute the work across other nodes.
Transaction Management:

    In distributed databases, the coordinator node manages distributed transactions.
    It ensures that all parts of a transaction are executed correctly across multiple nodes, maintaining consistency and integrity.
Consistency and Replication:

    The coordinator node plays a crucial role in maintaining consistency in replicated databases.
    It coordinates with other nodes to ensure that data is consistently replicated across the system.
Conflict Resolution:

    In systems that allow concurrent updates, the coordinator node may handle conflict resolution to ensure that the system remains in a consistent state.

CDN
CDN is a group of geographically distributed proxy servers. 
CDN brings the content closer to end users.
A proxy server is an intermediate server between a client and the origin server. 
Amazon CloudFront, and Google Cloud CDN

URI Namespace Delegation
The top-level authority owns the root namespace or a large portion of it.
For example, the example.com domain is managed by an organization or individual who has authority over it.
The top-level authority can create sub-namespaces within its domain and delegate authority over these sub-namespaces to other entities.
Example: Delegating http://sub.example.com to another department or organization.
The delegated entity can further delegate parts of its namespace to other entities.
Example: http://sub.example.com/path can be delegated to another team within the organization.

Push CDN

Content gets sent automatically to the CDN proxy servers from the origin server in the push CDN model. The content delivery to the CDN proxy servers is the content provider’s responsibility. Push CDN is appropriate for static content delivery, where the origin server decides which content to deliver to users using the CDN. 

Pull CDN

A CDN pulls the unavailable data from origin servers when requested by a user. The proxy servers keep the files for a specified amount of time and then remove them from the cache if they’re no longer requested to balance capacity and cost. this type of CDN is more suited for serving dynamic content.


Dynamic Adaptive Streaming over HTTP (DASH)

Dynamic Adaptive Streaming over HTTP (DASH) is a streaming technique designed to deliver high-quality media content over the internet in a scalable and efficient manner. It allows video to be streamed to users with varying network conditions, device capabilities, and bandwidth availability, providing an optimal viewing experience.

Segmented Video:

    The video content is divided into small segments, typically a few seconds long.
    Each segment is encoded at multiple quality levels (bitrates).
    The video player can request different segments from different quality levels as needed.
HTTP-Based Delivery:

    DASH uses standard HTTP protocols for delivering video content.
    This allows it to leverage existing web infrastructure, including CDNs (Content Delivery Networks), caching, and load balancing.

Multi-tier CDN architecture

The content provider sends the content to a large number of clients through a CDN. The task of distributing data to all the CDN proxy servers simultaneously is challenging and burdens the origin server significantly. CDNs follow a tree-like structure to ease the data distribution process for the origin server. The edge proxy servers have some peer servers that belong to the same hierarchy. This set of servers receives data from the parent nodes in the tree, which eventually receive data from the origin servers. The data is copied from the origin server to the proxy servers by following different paths in the tree.

Anycast Routing

Anycast is a network addressing and routing methodology where the same IP address is assigned to multiple nodes (or servers) in different locations. The goal is to route the incoming data packets to the nearest or best-performing node based on the routing protocol's criteria, often minimizing latency and optimizing load distribution.
Anycast Address:

    A single IP address is assigned to multiple nodes spread across different geographic locations.
    This IP address is advertised by all these nodes.
Routing Protocols:

    Standard IP routing protocols (like BGP) are used to propagate the routes for the anycast address.
    Routers select the best path to the anycast address based on their routing policies.

DNS Redirection for Network Routing

DNS redirection is a technique used to influence the routing of network traffic by resolving domain names to specific IP addresses. 
Scenario: GeoDNS

    DNS Configuration:
        The authoritative DNS server for www.example.com is configured with GeoDNS rules.
        It has multiple IP addresses for servers located in North America, Europe, and Asia.

    User Request:
        A user in New York enters www.example.com in their browser.
        The browser sends a DNS query to resolve the domain name.

    DNS Query Resolution:
        The DNS resolver forwards the query to the authoritative DNS server for www.example.com.
        The authoritative DNS server detects that the query originates from North America.

    GeoDNS Response:
        The DNS server responds with the IP address of the server located in North America (e.g., 192.0.2.1).

    User Connection:
        The browser receives the IP address (192.0.2.1) and establishes a connection to the North American server.

Split TCP:

    Split TCP is a technique that divides a single TCP connection into two or more segments, each managed separately.
    The client’s TCP connection terminates at an intermediate point (e.g., an IXP-level server), and a new TCP connection is established from this point to the destination server.

User Request:

    A user in New York enters a URL in their browser to access a Google service.
    The browser initiates a TCP connection to resolve the URL and send an HTTP request.

DNS Resolution:

    The browser uses DNS to resolve the domain name (e.g., www.google.com) to an IP address.
    Google's DNS infrastructure can direct the browser to an IP address of a server at a nearby IXP.

TCP Connection to IXP-Level Server:

    The browser establishes a TCP connection to the IXP-level server using the IP address provided by DNS.
    This IXP-level server is a part of Google's edge infrastructure located close to the user to minimize latency.

TCP Termination at IXP:

    The user's TCP connection terminates at the IXP-level server.
    This server processes the request locally as much as possible or forwards it to a Google data center.

Forwarding Request to Data Center:

    The IXP-level server forwards the request to a Google data center over a pre-established, persistent TCP connection.
    This connection is optimized with a large TCP window to handle high throughput and minimize latency.

Data Center Processing:

    The data center processes the request (e.g., fetching search results, retrieving email, or serving a video).

Sending Response Back to IXP-Level Server:

    The data center sends the response back to the IXP-level server over the persistent TCP connection.

Response to User:

    The IXP-level server sends the response back to the user's browser over the original TCP connection.

Random Id
UUID#

A straw man solution for our design uses UUIDs (universally unique IDs). This is a 128-bit number and it looks like 123e4567e89b12d3a456426614174000123e4567e89b12d3a456426614174000 in hexadecimal. It gives us about 10381038 numbers. UUIDs have different versions. We opt for version 4, which generates a pseudorandom number.

Each server can generate its own ID and assign the ID to its respective event. No coordination is needed for UUID since it’s independent of the server.

using a database
Consider a central database that provides a current ID and then increments the value by one. We can use the current ID as a unique identifier for our events.

using a range handler
We can use ranges in a central server. Suppose we have multiple ranges for one to two billion, such as 1 to 1,000,000; 1,000,001 to 2,000,000; and so on. In such a case, a central microservice can provide a range to a server upon request.

Any server can claim a range when it needs it for the first time or if it runs out of the range.

Time sortable IDs
Twitter Snowflake
Time stamp: 41 bits are assigned for milliseconds. The above calculations give us 69 years before we need a new algorithm to generate IDs
Worker number: The worker number is 10 bits. It gives us 210210 = 1,024 worker IDs.
Sequence number: The sequence number is 12 bits. For every ID generated on the server, the sequence number is incremented by one. It gives us 212212 = 4,096 unique sequence numbers.

IDs generated in a dead period are a problem. The dead period is when no request for generating an ID is made to the server. These IDs will be wasted since they take up identifier space. 
Another weak point of this system is its reliance on time. NTP can affect the working of this system. If the clock on one of the servers drifts two seconds in the future, other servers are two seconds behind. The NTP clock recognizes it and recalibrates its clock. Now, all serves will be aligned. However, in that drifting process, IDs could have been generated for a time that hasn’t occurred yet

Vector clocks

Vector clocks maintain causal history—that is, all information about the happened-before relationships of events. So, we must choose an efficient data structure to capture the causal history of each event.

Consider the design shown below. We’ll generate our ID by concatenating relevant information, just like the Twitter snowflake, with the following division:

    Vector clock: This is 53 bits and the counters of each node.

    Worker number: This is 10 bits. It gives us 2^{10} = 1,024 worker IDs.

TrueTime API
Google’s TrueTime API in Spanner is an interesting option. Instead of a particular time stamp, it reports an interval of time.

Time stamp: The time stamp is 41 bits. We use TETE​ as a time stamp.

Uncertainty: The uncertainty is four bits. Since the maximum uncertainty is claimed to be 6–10 ms, we’ll use four bits for storing it.

Worker number: This is 10 bits. It gives us 2^10 = 1,024 worker IDs.

Sequence number: This is eight bits. For every ID generated on the server, the sequence number is incremented by one. It gives us 2^8= 256 combinations.

Distributed Cache


Write-through cache: The write-through mechanism writes on the cache as well as on the database. Writing on both storages can happen concurrently or one after the other. This increases the write latency but ensures strong consistency between the database and the cache.
Write-back cache: In the write-back cache mechanism, the data is first written to the cache and asynchronously written to the database. Although the cache has updated data, inconsistency is inevitable in scenarios where a client reads stale data from the database. However, systems using this strategy will have small writing latency.
Write-around cache: This strategy involves writing data to the database only. Later, when a read is triggered for the data, it’s written to cache after a cache miss. The database will have updated data, but such a strategy isn’t favorable for reading recently updated data.

Cache client
A cache client is a piece of code residing in hosting servers that do (hash) computations to store and retrieve data in the cache servers. Also, cache clients may coordinate with other system components like monitoring and configuration services.

Each cache client will know about all the cache servers.
All clients can use well-known transport protocols like TCP or UDP to talk to the cache servers.

Memcached
Memcached stores data in the form of a key-value pair. Both the key and the value are strings. 
This means that any data that has been stored will have to be serialized. Memcached servers are unaware of each other, and there’s no synchronization, data sharing, and communication between the servers.

Redis

Redis is a data structure store that can be used as a cache, database, and message broker.

Data structure store: Redis understands the different data structures it stores. We don’t have to retrieve data structures from it, manipulate them, and then store them back. We can make in-house changes that save both time and effort.
Database: It can persist all the in-memory blobs on the secondary storage.
Message broker: Asynchronous communication is a vital requirement in distributed systems. Redis can translate millions of messages per second from one component to another in a system.

Distributed Queues

Metadata service#

This component is responsible for storing, retrieving, and updating the metadata of queues in the metadata store and cache. Whenever a queue is created or deleted, the metadata store and cache are updated accordingly. 

Message Broker
The broker server is the core component of our pub-sub system. It will handle write and read requests. A broker will have multiple topics where each topic can have multiple partitions associated with it. We use partitions to store messages in the local storage for persistence.

Tpoic
topic is a persistent sequence of messages stored in the local storage of the broker. 
Reading and writing a message from or to a topic is an I/O task for computers, and scaling such tasks is challenging. This is the reason we split the topics into multiple partitions. The data belonging to a single topic can be present in numerous partitions.

For example, let’s assume have Topic A and we allocate three partitions for it. The producers will send their messages to the relevant topic. The messages received will be sent to various partitions on basis of the round-robin algorithm.

Feature	Message Queue	                                Message Broker
Basic Functionality	Simple enqueue/dequeue operations	Advanced messaging patterns (queues, topics)
Scalability	Limited to basic thread safety	            Supports multiple producers/consumers, load balancing
Message Routing	Basic FIFO ordering	                    Complex routing rules, exchanges
Persistence	Basic in-memory/disk storage	            Durable storage, message acknowledgments
Security	Basic thread safety	                        Authentication, authorization, encryption
Monitoring	Limited	                                    Detailed metrics, logs, management interfaces
Fault Tolerance	Basic redundancy	                    Clustering, replication, failover mechanisms

Message brokers, particularly those designed for high throughput and fault tolerance like Apache Kafka, use partitions and message segmentation to allow parallel reads and writes, ensuring scalability and reliability.

Topic Partitions:

    Definition: A topic in a message broker can be divided into multiple partitions. Each partition is an ordered sequence of messages and can be read and written to independently.
    Parallel Processing: By splitting a topic into multiple partitions, consumers can read from different partitions in parallel. Similarly, producers can write to different partitions simultaneously.
    Scalability: Partitions enable the system to scale horizontally. Adding more partitions allows for more parallelism, which can handle higher throughput and larger volumes of data.
    Fault Tolerance: Partitions can be replicated across multiple brokers (nodes) to ensure fault tolerance. If one broker fails, another broker with a replica can take over.

Message Segmentation:

    Definition: Messages can be split into segments or chunks, especially when dealing with large messages. This allows large messages to be transmitted and processed without overwhelming the system.
    Parallel Reads: By segmenting messages, consumers can read different segments in parallel, improving processing efficiency and speed.
    Efficient Storage and Retrieval: Segmentation allows for more efficient storage and retrieval, as segments can be stored across different nodes and retrieved as needed.

Advanced Message Queues:

Some advanced message queue systems, such as Amazon SQS and RabbitMQ, offer more features that bridge the gap between traditional queues and message brokers.

    Amazon SQS:
        Message Batching: Supports sending and receiving batches of messages to improve throughput.
        Visibility Timeout: Allows a message to be invisible to other consumers for a specified period while it is being processed.
        Scaling: Can scale horizontally, though it doesn't use partitions in the same way as Kafka.

    RabbitMQ:
        Exchanges and Queues: Supports different types of exchanges (direct, topic, fanout) to route messages to different queues.
        Queue Sharding: Can use plugins or extensions to achieve some level of partitioning or sharding.
        Clustering: Supports clustering for high availability and fault tolerance.