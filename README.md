#fping-scan

Scan subnets with Python for hosts that are up. Useful in convoluted network DHCP scope schemas (like ours).
Currently, this works on Mac OSx. I fully intend to see if this script will also work on Linux, whether or not
it requires alterations to universalize it. Hmm, that is a word -- *universalize*.

**Requires** fping, a nice take on the traditional `ping` command to be installed.

How to install fping (on Mac OSx -- I'm on 10.11.3 El Capitan) from Terminal:

```ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" < /dev/null 2> /dev/null```

```brew install fping```

If you have issues (as I did, with a "*cannot create link*" error, do this:

```sudo chown your_username_here /usr/local/share/man/man8```

