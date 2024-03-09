When a user wants to connect to a website what happens
sequenceDiagram
actor Alice
actor John
Alice->>John: Hello John, how are you?
John-->>Alice: Great!
Alice-)John: See you later!

``` mermaid
sequenceDiagram
  participant User
  participant Browser
  participant DNS
  participant Server

  User->>Browser: Enter URL
  Browser->>Browser: Check cache
  alt Cache Hit
    Browser-->>User: Use cached IP
  else Cache Miss
    Browser->>DNS: DNS Resolution
    DNS-->>Browser: Resolved IP
  end

  Browser->>Server: Initiate TCP Connection
  Browser-->>Server: Three-Way Handshake

  Browser->>Server: HTTP Request
  Server-->>Browser: Process Request

  Server->>Browser: HTTP Response
  Browser-->>User: Render Content
```

1. **User enters the web address in the browser.**
    - The user types a URL (Uniform Resource Locator) into the browser's address bar.
2. **Browser checks its cache.**
    - The browser checks its local cache to see if it already has the IP address associated with the entered URL. If found, it skips the DNS lookup.
3. **DNS (Domain Name System) resolution.**
    - If the IP address is not found in the cache, the browser sends a DNS request to a DNS server to resolve the domain name to an IP address. The DNS server responds with the IP address associated with the domain.
4. **Browser initiates a TCP connection.**
    - The browser initiates a TCP (Transmission Control Protocol) connection to the web server using the obtained IP address and the default HTTP port (usually port 80).
5. **Three-Way Handshake.**
    - A three-way handshake occurs between the browser and the server to establish a reliable communication channel.
6. **HTTP Request.**
    - The browser sends an HTTP (Hypertext Transfer Protocol) request to the web server. This request includes information such as the method (GET, POST, etc.), headers, and the requested resource.
7. **Server processes the request.**
    - The web server processes the incoming request, which may involve executing server-side code, retrieving data from a database, or other operations based on the nature of the request.
8. **HTTP Response.**
    - The server sends an HTTP response back to the browser. The response includes a status code, headers, and the requested content (HTML, images, etc.).
9. **Browser renders the content.**
    - The browser receives the response and renders the content on the user's screen.
