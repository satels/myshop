FROM phusion/baseimage:0.9.21
MAINTAINER Ivan Petukhov <satels@gmail.com>

CMD ["/sbin/my_init"]

RUN sed -i -e 's/archive.ubuntu.com/mirror.yandex.ru/g' /etc/apt/sources.list \
    && export DEBIAN_FRONTEND=noninteractive \
    && apt-get update -qq \
    && locale-gen en_US.UTF-8 ru_RU.UTF-8 \
    && apt-get install -qq \
        git-core \
        python3.5 \
        python3-dev \
        python3-pip \
    && pip3 install --upgrade pip \
    && rm -rf /etc/logrotate.d \
    && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY requirements.txt /var/www/myshop/
RUN pip3 install -r /var/www/myshop/requirements.txt

EXPOSE 80 8020

COPY . /var/www/myshop/

WORKDIR /var/www/myshop

RUN mkdir -p /var/log/myshop \
    && find . -name '*.pyc' -delete \
    && find . -name '*.swp' -delete \
    && python3 -c 'import compileall, os; compileall.compile_dir(os.curdir, force=1)' > /dev/null \
    && rm -rf /var/log/myshop/* \
    && export SERVER_ROLE=dev \
    && python3 ./myshop/manage.py collectstatic --noinput --traceback
