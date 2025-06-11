FROM debian:stable-slim
RUN apt update && apt upgrade -y
RUN apt install -y build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev wget libbz2-dev
RUN apt install -y software-properties-common
RUN apt update
RUN apt install -y python3-dev python3-distutils
COPY main.py main.py
COPY books / books/
CMD ["python3", "main.py"]
