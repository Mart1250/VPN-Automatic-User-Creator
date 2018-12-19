from ftplib import FTP
import os

def grabFile():

    filename = "newusers.txt"
    
    if filename in ftp.nlst():

        localfile = open('data/' + filename, 'wb')

        ftp.retrbinary('RETR ' + filename, localfile.write, 1024)

        ftp.delete(filename)

        ftp.quit()
        localfile.close()

#domain name or server ip:
ftp = FTP('external-ip')
ftp.login(user='username', passwd = 'password')
ftp.cwd('/domains/mijn-privacy.nl/public_html/wp-content/themes/shapely/woocommerce/emails/')

grabFile()

newusers = "data/newusers.txt"

if (os.path.isfile(newusers)):

    ipfile = open("/etc/iptables.rules", "r+")
    userfile = open("/etc/ppp/chap-secrets", "r+")


    with ipfile as f:
        ipfilelist = f.readlines()

    with userfile as g:
        userfilelist = g.readlines();

    number = 0

    with open(newusers) as users:
        for line in users:

            number += 1
        
            if number == 4:
                number = 1

            if number == 1:

                if not any(line in s for s in ipfilelist):

                    ipfilelist.insert(9, line)
                    ipfile = open("/etc/iptables.rules", "r+")

                    for item in ipfilelist:

                        ipfile.write("%s" % item)

            if number == 2: 

                userfilelist.insert(0, line)
                userfile = open("/etc/ppp/chap-secrets", "r+")

                for item in userfilelist:

                    #ipfile.write("\n")
                    userfile.write("%s" % item)

os.remove(newusers) 
