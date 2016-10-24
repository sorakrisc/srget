# srget

This code was written on Linux. This program is a resumable concurrent file downloader. This program run through command-line and does not support https, and chunked transfer encoding.

OBJECTIVE:
As an example, the command srget -o test.txt http://pantip.com/ will download the page at http://pantip.com and save that into test.txt. Users can optionally ask the program to download from a specific
port by giving the port parameter in the url (e.g., http://pluto.muic.io:3000/).

The -c option is optional. When supplied, the program will download using the specified numConn connec-
tions simultaneously. If only the -c is present but without the number of connections specified, it will use a default
of 5 simultaneous connections. Notice that when used in conjunction with resume, the program may be called
with a different number of connections (which it should respect).

FEATURES:
  1. Download file
  2. Download files in background thread simultaneously
  3. Able to resume the download when interruption occur
  4. Set desired numbers of concurrent (default at 5)

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
  o thread run synchronously
  o when the program cannot be call with different number of connections when resume
  o support link without content length
