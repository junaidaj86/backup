Imagine we have 2 data center. which are connected with each other.

### usecase 1:  One is 1 leader and and the others are followers.
Imagine 
![[Excalidraw/CAP theorem]]

Imagine one user in data center 1 writes in data center 2. Now there is a network issue and the link between 2 DC are broken.
In this scenarios since the Leader is in other DC, write is not done. so the system is not highly available but since the data is same in both DC, its highly consistent. 
## so this is  CP

### usecase 2:

Here we have multi leader DB setup. now is the same happens, the system is available, but not consistent.
## so this is AP


