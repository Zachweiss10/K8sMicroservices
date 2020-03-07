FROM python:alpine3.7
COPY . /app/
COPY templates/ /app/templates
WORKDIR /app/
#RUN mkdir /app/uploads
RUN pip install -r requirements.txt
#RUN ls -l
EXPOSE 5001
ENTRYPOINT [ "python" ]
CMD [ "app.py"]
#ENTRYPOINT [ "ls -l" ]
#CMD [ "-l" ]