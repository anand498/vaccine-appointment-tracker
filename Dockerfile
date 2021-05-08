FROM python:3.7
COPY ./ /app
WORKDIR /app
EXPOSE 8000
CMD ["python","main.py"]