FROM python as builder
WORKDIR /app
COPY main.py .
RUN ["pip","install","requests"]
RUN ["python","main.py"]
RUN mkdir -p /export && cp  rickandmorty.* /export
#CMD ["sh"]

FROM nginx:alpine
EXPOSE 80

COPY --from=builder /var/www/html/ .




