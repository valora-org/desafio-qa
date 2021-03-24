# Pull base image.
FROM python

# Install.
RUN apt-get update &&\
      apt-get -y install wget gnupg2 unzip

# ADD Google Chrome Repo
RUN wget https://dl.google.com/linux/linux_signing_key.pub &&\
      apt-key add linux_signing_key.pub &&\
      echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' > /etc/apt/sources.list.d/google-chrome.list

# Instal Chrome
RUN apt-get update &&\
      apt install -y google-chrome-stable

# Install chrome driver
RUN wget https://chromedriver.storage.googleapis.com/89.0.4389.23/chromedriver_linux64.zip &&\
      unzip chromedriver_linux64.zip &&\
      cp chromedriver /usr/sbin/


# Install Selenium and Behave
RUN pip install selenium behave nose

WORKDIR /app
COPY ./features /app/features

CMD behave
