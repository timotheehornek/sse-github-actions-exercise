FROM ubuntu:20.04

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update
RUN apt install -y python3 python-is-python3 wget python3-distutils

# Cleanup
RUN apt-get clean
RUN rm -rf /tmp/*

# pip should be installed and used as a user. Therefore we
# create a new user "testuser" and change to this user.
ARG USER_NAME=testuser
ARG USER_HOME=/home/${USER_NAME}
#ARG USER_ID=1000
ARG USER_ID=1000
ARG GROUP_ID=1000

RUN groupadd -g $GROUP_ID "$USER_NAME"
RUN adduser \
    --home "$USER_HOME" \
    --uid $USER_ID \
    --gid $GROUP_ID \
    --disabled-password \
    "$USER_NAME"

USER $USER_NAME
WORKDIR "$USER_HOME"

# Install pip, make sure it can be called as `pip` instead of
# `pip3``. The installation location of `pip` has to be added
# to the path. Afterwards, we can install missing tools via
# `pip`.
ENV PATH=/home/$USER_NAME/.local/bin:${PATH}
RUN wget https://bootstrap.pypa.io/get-pip.py && python get-pip.py && rm get-pip.py \
    && ln -sf /home/$USER_NAME/.local/bin/pip3 /home/$USER_NAME/.local/bin/pip \
    && pip install black


CMD ["/bin/sh"]
# Reset frontend for interactive use
ENV DEBIAN_FRONTEND=