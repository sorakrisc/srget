# srget

This code was written on Linux. This program is a resumable concurrent file downloader. This program run through command-line and does not support https, and chunked transfer encoding.

FEATURES:
  1. Download file
  2. Download files in background thread simultaneously
  3. Able to resume the download when interruption occur
  4. Set number of concurrent (default at 5)

SUMMARY OF MY PROGRAM:

Make connection to the server
Receive data with header
Extract the header from the content
Then write the content to output file
Start receiving data then write it in chunk

If there was a disconnection in any aspect the code will
create a file call a call a cache file storing ETag, date
modified, content length, and the number of byte written

Then if the user would want to download the same file the PROGRAM
would find the existence of the cache file and resume download

ROADMAP:
  o Supports chunked transfer encoding
