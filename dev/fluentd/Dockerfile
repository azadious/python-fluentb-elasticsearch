FROM fluent/fluentd:v1.12.0-debian-1.0
USER root
RUN fluent-gem install fluent-plugin-elasticsearch
USER fluent
COPY ./conf /fluentd/etc
