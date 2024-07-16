FROM python:3.12.4-bullseye
ENV TZ=Europe/Saratov
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

ARG USER=oinkuser
ARG GROUP=oinkgroup
ARG USER_ID=1000
ARG GROUP_ID=1000

RUN addgroup --system --gid $GROUP_ID $GROUP && \
    adduser --system --uid $USER_ID --ingroup $GROUP $USER

# Install dependencies (Meteo)
RUN apt-get -qq update
RUN apt-get -qq install -y --no-install-recommends \
    curl \
    wget \
    jq \
    nano \
    netcat \
    cron \
    binutils \
    libproj-dev \
    gdal-bin \
    gettext

# Clean up
RUN apt-get -qq clean

RUN mkdir -p /backend /logs /static

COPY ./requirements.txt /backend/requirements.txt
WORKDIR /backend

RUN chown -R $USER:$GROUP /backend

# Install Python dependencies (Meteo)
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

STOPSIGNAL SIGQUIT

COPY . /backend
RUN chown -R $USER:$GROUP /backend /logs

USER $USER

ENV PYTHONUNBUFFERED=TRUE
ENV PYTHONDONTWRITEBYTECODE=1
ENV STAGE=dev
