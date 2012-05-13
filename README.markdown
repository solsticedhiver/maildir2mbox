The script at [jooooooon/maildir2mbox](https://github.com/jooooooon/maildir2mbox) was so slow I had to rewrite it, just because it baffled me to see a script with so horrible performance.

The original script was a *bash* script calling repeatedly a perl script, creating many subproccess and pipes; it uses 100% cpu just for nothing.

A simple fix would have been to rewrite the whole thing in **perl** to avoid calls to external script but I know nothing about **perl** so I made it in **python**. **python2** has a bug with *strptime* and *%z* so I had to make it a *python3* script.

The current script has certainly bugs. It can't handle all the encodings of imported emails for example.
It makes heavy use of memory too.

Just cd into the directory with the maildir emails.
And pipe the output of the script to your desired mbox file.
For example:

	cd /into/the/directory/with/my/emails/
	./maildir2mbox.py > /tmp/test.mbox
