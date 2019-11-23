FROM python:3.7.5

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN ls -lh /usr/src/app

CMD [ "python3", "./pv_simulator.py" ]
