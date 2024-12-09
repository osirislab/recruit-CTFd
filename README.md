# OSIRIS Recruit CTFd 

Hello current **Infrastructure Manager**, or wandering lab member!<br>
This is the official setup guide for OSIRIS RECRUIT @ 128.238.62.253 hosted on ISIS-host.

Previously, there wasn't too much documentation surrounding CTFd and how it's SSL certificates worked, so this is how you do it.

## Prerequisites
1. Install `docker`. Good guide for ubuntu-server-22 [here](https://docs.docker.com/engine/install/ubuntu/).

## Renew Certificates
1. Clone the repo <br>
```bash
git clone git@github.com:osirislab/recruit-CTFd.git
```
2. Stop nginx
```bash
sudo systemctl stop nginx
```
4. Generate certificates via. Certbot
```bash
sudo certbot certonly --standalone
```
Enter the domain name (`recruit.osiris.cyber.nyu.edu`).
5. Verify it is working at your domain. Make sure to set the admin password and no one got to it before you did 💯.
6. Set up a cronjob to renew the certificates every 3 months!


## Reminders
Set up a cronjob to renew the certs. Please.<br>
DNS is controlled by greater powers. Reach out to @Infrastrukture if you need help.<br>

Cheers ❤️ @davidchiii (@scriiible)
