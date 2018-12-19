# VPN-Automatic-User-Creator
This python script will read an external file on a ftp server and adds the user in the chap-secret file and adds a iptables rule for this user.

Set a cronjob for this script (for example) every hour. This works in conjunction with my PHP script that creates random user names when an woocommerce order is completed.
