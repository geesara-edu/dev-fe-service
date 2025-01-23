FROM python:latest

RUN pip install flask requests
WORKDIR /opt
#ENV FLASK_APP app.py
COPY app.py .
EXPOSE 30030

#ENTRYPOINT [ "flask run -h 0.0.0.0 -p 30030" ]
CMD ["python", "app.py"]