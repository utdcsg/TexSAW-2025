FROM pwn.red/jail

COPY --from=python:slim / /srv

COPY main.py /srv/app/run
COPY flag.txt /srv/flag.txt
ENV JAIL_MEM=20M JAIL_PIDS=20 JAIL_TMP_SIZE=64K JAIL_ENV_PATH=/usr/local/bin:/usr/bin:/bin
