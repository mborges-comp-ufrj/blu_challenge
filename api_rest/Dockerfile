FROM python:3.9
ADD . ./api_rest
WORKDIR /api_rest
ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN pip install -r requirements.txt
CMD ["flask", "run"]