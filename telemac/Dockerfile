FROM alpine:3.11

RUN apk add --no-cache subversion

RUN mkdir /telemac && \
    svn co http://svn.opentelemac.org/svn/opentelemac/tags/v8p1r0/scripts /telemac/scripts --username=ot-svn-public --password=telemac1* && \
    svn co http://svn.opentelemac.org/svn/opentelemac/tags/v8p1r0/sources /telemac/sources --username=ot-svn-public --password=telemac1* && \
    svn co http://svn.opentelemac.org/svn/opentelemac/tags/v8p1r0/optionals/metis-5.1.0 /telemac/metis --username=ot-svn-public --password=telemac1*

RUN apk add --no-cache \
    -X http://dl-cdn.alpinelinux.org/alpine/edge/main \
    -X http://dl-cdn.alpinelinux.org/alpine/edge/testing \
    musl musl-dev libc-dev zlib numactl xz-libs eudev-libs libxml2 \
    git openssh-client openssh-server g++ gfortran make cmake pkgconf openmpi openmpi-dev

RUN echo "**** install Python ****" && \
    apk add --no-cache python3 && \
    if [ ! -e /usr/bin/python ]; then ln -sf python3 /usr/bin/python ; fi && \
    \
    echo "**** install pip ****" && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --no-cache --upgrade pip setuptools wheel && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi

RUN apk add --no-cache \
    -X http://dl-cdn.alpinelinux.org/alpine/edge/community \
    py3-numpy py3-matplotlib py3-numpy-dev py3-numpy-f2py

COPY ./systel.cfg /telemac/systel.cfg

RUN cd /telemac/metis && \
    cmake -D CMAKE_INSTALL_PREFIX='/telemac/metis' . && \
    make && make install

ENV PYTHONUNBUFFERED=1
ENV HOMETEL="/telemac"
ENV SYSTELCFG="/telemac/systel.cfg"
ENV PATH="/telemac/scripts/python3:$PATH"
ENV USETELCFG="gfortranp"
ENV PYTHONPATH="$HOMETEL/scripts/python3:$PYTHONPATH"
ENV LD_LIBRARY_PATH="$HOMETEL/builds/$USETELCFG/wrap_api/lib:$LD_LIBRARY_PATH"
ENV PYTHONPATH="$HOMETEL/builds/$USETELCFG/wrap_api/lib:$PYTHONPATH"
ENV METISHOME="/telemac/metis"

RUN compile_telemac.py

RUN apk add --no-cache \
    -X http://dl-cdn.alpinelinux.org/alpine/edge/community \
    py3-boto3
RUN pwd
RUN pwd
RUN pwd
RUN pwd
RUN pwd
RUN pwd
RUN mkdir /gitlocal && cd /gitlocal && \
    git clone https://github.com/meracan/meracan-api.git && \
    pip3 install --no-cache -e ./meracan-api

ENV TELEMAC_LOCALFOLDER="/data"
RUN mkdir /data
WORKDIR "/data"
COPY ./download.py /data/download.py
# CMD ["python3","download.py"]