The script at `https://github.com/jooooooon/maildir2mbox` was so slow I had to rewrite it just because it baffled me to see a script with so horrible performance.

The original script is a *bash* script calling repeatedly a perl script, creating many subprocess and pipes; it uses 100% cpu just for nothing.

A simple fix would have been to rewrite the whole thing in **perl** to avoid calls to external script but I know nothing about **perl** so I made it in **python**. **python2** has a bug with *strptime* and *%z* so I had to make it a *python3* script.

It certainly has bug. It can't handle all the encoding for example.
