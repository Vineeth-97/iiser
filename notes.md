# NOTES

## Listing installed packages

To create a txt file **pkginstalls.txt** containing the list of all packages installed, run (from home folder)
```
./pkginstalls.sh
```
The simple command to grab from the current log is:
```
grep " install " /var/log/dpkg.log
```
The previous log:
```
grep " install " /var/log/dpkg.log.1
```
And archived logs:
```
zgrep " install " /var/log/dpkg.log.2.gz
```
```
history | grep "apt-get install"
```
---
## Removing installed packages

To remove an installed package run,
```
sudo apt-get --purge remove package
```
If your program isn't properly removed using the `apt-get` command, try using:
```
sudo aptitude remove program
```
---
## Cyberoam Login Client

To login through Cyberoam Client, run `login_wifi` which is an alias for,
```
./crclient -u vineethbannu14 -i wlp2s0
```
crclient and its config files are located in home directory and **server : 172.16.31.101 port 6060**

To logout from the server run `logout_wifi` which is also an alias for
```
./crclient -l vineethbannu14
```
---
## History in bash

To increase the history buffer size append the following line in `\etc\profile` :
```
export HISTSIZE = 5000
```
More options are explained [here](http://linux-training.be/funhtml/ch16.html).