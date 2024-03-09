
Why do we need URL 
1. To short long url to short url.
2. Some media like twitter has char restriction, so long url cannot be shared, so short url is used.
3. We can get analytics from Bitly, so we generate many short url for same url and give it to influencer, then see which influencer brings in more business.

### Functional Requirement

1.  Given a long url, return a short url
2. When user enters short url, user should be redirected to long url.
3. If the same long url is entered, then it should return different and unique url for every entry.
4. URL can be customised (optional)
5. TTL for the long and short url mapping (optional)
6. Analytics (optional)



### Top-Down steps for system design in an interview
1. Gather functional requirements
		a.  This is the details problem statement
		b. In plain english, describe the user view of the system
		 c. Show that you can communicate and unpack short statement to detailed prolem statement
		 d.Ask clarifying questions

### decide how system will look

1. Monolit 
2. Microservice

### visual representation

Draw architecture digram explaining your thought process.



## Summary of steps

1. Gather functional requirement.
2. Decide if its monolith or Microservice.
3. Draw the architectural diagram.
4. Dive into each Microservice. 

### [[IK/system design/bitly/Implementation]]


### [[Network protocol]]

### [[Webserver]]

### [[database Index]]

### scaling
 ###  Reasons to scale
 1. Huge data
 2. Large number of request per second
 3. High response time per request
 4. Single point of failure
 5. High latency for users on other side of the world
 6. Hotspot data

There are 2 types of Scaling
### [[Vertical Scaling]]
### [[Horizontal Scaling]]


### Non-Functional Requirements

^68ace5

1. 2 Billion short link create request. = 2000000000 request/year / 365/ 24 /60 / 60 = 60 to 70 RPS 
2. 20 billion request click per month = 20000000000 RPY / 30 / 60 / 60 =  7770 RPS



### [[Performance Metrics]]

[[Latency vs response time]]

## [[Forward and Reverse Proxy]]

###  [[Load balancing]]

## [[Any Cast IP]]

## [[database replication]]

## [[IK/system design/bitly/CAP Theorem]]

### [[IK/system design/bitly/CDN]]

### [[cache tier]]

### [[IK/system design/bitly/sharding]]










