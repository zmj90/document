# FROM scratch
FROM 90e8568ba1cf

WORKDIR /home
COPY *.tar.gz *.sh *.war *.conf *.tgz *.txt .

RUN chmod +x *.sh

ARG DEBIAN_FRONTEND=noninteractive
ENV LANG=en_US.UTF-8
ENV TZ=Asia/Shanghai
ENV JAVA_HOME=/usr/local/jdk-11.0.15
ENV CLASS_PATH=.:${JAVA_HOME}/lib
ENV PATH=${JAVA_HOME}/bin:$PATH
ENV TOMCAT_HOME=/usr/local/apache-tomcat-8.5.81

RUN ./ubuntu-config.sh && ./install-software.sh && mv jenkins.war $TOMCAT_HOME/webapps

VOLUME /root/.jenkins

EXPOSE 8080/tcp
EXPOSE 8080/udp

ENTRYPOINT ./run.sh
