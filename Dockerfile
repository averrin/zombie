FROM python
EXPOSE 80
COPY . /src
WORKDIR /src
RUN pip install bottle
CMD ["python", "main.py"]
