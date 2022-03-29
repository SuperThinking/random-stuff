FROM sosedoff/pgweb

RUN apk add --no-cache bash

COPY wait-for-it.sh entrypoint.sh ./

RUN ["chmod", "+x", "./entrypoint.sh"]
ENTRYPOINT ["./entrypoint.sh"]

EXPOSE 8081
CMD ["/usr/bin/pgweb", "--bind=0.0.0.0", "--listen=8081"]
