FROM ubuntu:20.04
USER root
SHELL ["/bin/bash", "-l", "-c"]

RUN apt -y update && apt install -y wget vim git curl make sudo locales build-essential checkinstall libffi-dev libssl-dev zlib1g-dev libbz2-dev libreadline-dev && localedef -f UTF-8 -i ja_JP ja_JP.UTF-8

ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

RUN apt install -y vim less
RUN apt install -y python3-pip
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install pipenv

RUN git clone https://github.com/pyenv/pyenv.git ~/.pyenv
RUN touch ~/.bash_profile
RUN echo -e "# pyenv paths" >> ~/.bash_profile
RUN echo "#!/bin/bash" >> ~/.bash_profile
RUN echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
RUN echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
RUN echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
RUN bash ~/.bash_profile
RUN pyenv -v

RUN pyenv install 3.8.2
RUN pyenv global 3.8.2

ENTRYPOINT ["/usr/src/sharetech/entrypoint.sh"]