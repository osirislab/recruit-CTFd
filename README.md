# OSIRIS Recruit CTFd 

Hello current **Infrastructure Manager**, or wandering lab member!<br>
This is the official setup guide for OSIRIS RECRUIT @ 128.238.62.253 hosted on ISIS-host.

Previously, there wasn't too much documentation surrounding CTFd and how it's SSL certificates worked, so this is how you do it.

## Prerequisites
1. Install `docker`. Good guide for ubuntu-server-22 [here](https://docs.docker.com/engine/install/ubuntu/).

## Install
1. Clone the repo <br>
```bash
git clone git@github.com:osirislab/recruit-CTFd.git
```
2. Set up Certbot with certificates with its docker image. It will prompt your to set up a **standalone** server. Choose that option. Additionally, enter the domain that is used for recruit. Here it is `recruit.osiris.bar` (Thanks Ruarua!) <br>
```bash
docker run -it --rm --name certbot \
        -v "/etc/letsencrypt:/etc/letsencrypt" \
        -v "/var/lib/letsencrypt:/var/lib/letsencrypt" \
        certbot/certbot certonly
```
3. Copy the certificates from the `/etc/letsencrypt/live` directory
```bash
cp /etc/letsencrypt/live/recruit.osiris.bar/privkey.pem /home/manager/recruit-ctfd/conf/nginx/privkey.pem
cp /etc/letsencrypt/live/recruit.osiris.bar/fullchain.pem /home/manager/recruit-ctfd/conf/nginx/fullchain.pem
```
4. Return to `/recruit-ctfd` and run the `docker-compose.yml` file. `-d` for detached.
```bash
docker-compose up -d
```
5. Verify it is working at your domain. Make sure to set the admin password and no one got to it before you did 💯.
6. Set up a cronjob to renew the certificates every 3 months!


## Reminders
Set up a cronjob to renew the certs. Please.<br>
DNS is controlled by greater powers. Reach out to @Infrastrukture if you need help.<br>

Cheers ❤️ @davidchiii (@scriiible)