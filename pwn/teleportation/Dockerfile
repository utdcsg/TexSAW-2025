# our local base image
FROM ubuntu:20.04@sha256:e5a6aeef391a8a9bdaee3de6b28f393837c479d8217324a2340b64e45a81e0ef AS base
LABEL description="Container for Ubuntu-20"

FROM pwn.red/jail
COPY --from=base / /srv

RUN mkdir /srv/app
COPY chall /srv/app/run
COPY flag.txt /srv/app/flag.txt

RUN chmod 755 /srv/app/run
RUN chmod 644 /srv/app/flag.txt

ENV JAIL_TIME 60
ENV JAIL_MEM 10M