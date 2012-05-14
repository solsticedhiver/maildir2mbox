The script at [jooooooon/maildir2mbox](https://github.com/jooooooon/maildir2mbox) was so slow I had to rewrite it, just because it baffled me to see a script with so horrible performance.

The original script was a *bash* script calling repeatedly a *perl* script, creating many subproccess and pipes; it uses 100% CPU just for nothing.

A simple fix would have been to rewrite the whole thing in **perl** to avoid calls to external script but I know nothing about *perl* so I made it in **python**. *python2* has a bug with *strptime* and *%z* so I had to make it a *python3* script.

Just cd into the directory with the maildir emails.
And pipe the output of the script to your desired mbox file.
For example:

	cd /into/the/directory/with/my/emails/
	./maildir2mbox.py > /tmp/test.mbox

This gives a **mboxrd** file. This is the variant of *mbox* file where every 'From ' line in the message is quoted (even if it is already quoted)

The current script has certainly bugs. It can't handle all the encodings of imported emails for example.
It makes "heavy" use of memory too.

Side-effect: it rewrites the headers of each message in one single line

Another attempt: https://gist.github.com/2693582
This one uses the mailbox python module. Why bother to reinvent the wheel where thereis a module for it ?
But it outputs mboxo only format and is slow.
However it converts all mboxes in a given directory and its submail folders directly to /tmp
