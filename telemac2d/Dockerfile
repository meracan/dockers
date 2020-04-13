FROM alpine:3.11
ENV PYTHONUNBUFFERED=1
ENV SYSTELCFG="/telemac/systel.cfg"
ENV PATH="/telemac/scripts/python3:$PATH"

RUN apk add --no-cache \
    -X http://dl-cdn.alpinelinux.org/alpine/edge/main \
    -X http://dl-cdn.alpinelinux.org/alpine/edge/testing \
    musl musl-dev libc-dev zlib numactl xz-libs eudev-libs libxml2 \
    git openssh-client openssh-server subversion g++ make cmake gfortran pkgconf openmpi openmpi-dev 

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
    py3-numpy

RUN mkdir /telemac && \
    svn co http://svn.opentelemac.org/svn/opentelemac/tags/v8p1r0/scripts /telemac/scripts --username=ot-svn-public --password=telemac1* && \
    svn co http://svn.opentelemac.org/svn/opentelemac/tags/v8p1r0/sources /telemac/sources --username=ot-svn-public --password=telemac1* && \
    svn co http://svn.opentelemac.org/svn/opentelemac/tags/v8p1r0/optionals/metis-5.1.0 /telemac/metis --username=ot-svn-public --password=telemac1*


COPY ./systel.cfg /telemac/systel.cfg


RUN cd /telemac/metis && \
    cmake -D CMAKE_INSTALL_PREFIX='/telemac/metis' . && \
    make && make install

RUN compile_telemac.py

RUN git clone git@github.com:meracan/s3-telemac.git
RUN pip3 install --no-cache -e ./s3-telemac

RUN mkdir /data
WORKDIR "/data"
COPY ./run.py /model/run.py
CMD ["python3","run.py"]