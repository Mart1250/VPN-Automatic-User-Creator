# VPN-Automatic-User-Creator
This python script will read an external file on a ftp server and adds the user in the chap-secret file and adds a iptables rule for this user.

Set a cronjob for this script (for example) every hour.


USE THE RAW FUNCTION ON GITHUB, THAT MAKES THE FORMAT MORE CLEARLY!

The format of the file newusers.txt is as follows:


-A INPUT -s ipadress/32 -j ACCEPT
Username             l2tpd   Password                *
-


And repeat...

SO for example:

-A INPUT -s ipadress/32 -j ACCEPT
Username             l2tpd   Password                *
-
-A INPUT -s ipadress/32 -j ACCEPT
Username             l2tpd   Password                *
-
-A INPUT -s ipadress/32 -j ACCEPT
Username             l2tpd   Password                *
-
