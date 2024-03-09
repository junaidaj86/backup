Database stores the record in a disk, in a log file. So we write the record sequentially.

1. We append new record at the end of the file.
2. But if we have to search, then we have to search the entire file.
3. This will be very expensive and slow.

To overcome this, we store an in memory hash map, where we store the key as short url and value as offset in database where the record is stored.