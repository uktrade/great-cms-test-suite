FROM python:3.9.2

RUN mkdir -p /app
WORKDIR /app
ADD . /app/

# necessary for browserstack-sdk
RUN apt-get update -y
RUN apt-get install libstdc++6-amd64-cross -y
RUN ln -s /usr/x86_64-linux-gnu/lib64/ /lib64
ENV LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/lib64:/usr/x86_64-linux-gnu/lib"

RUN pip install -U pip
RUN pip install pip-tools
RUN make requirements
RUN make install_requirements
