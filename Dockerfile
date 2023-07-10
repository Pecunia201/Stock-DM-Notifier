FROM python:3.11.4

WORKDIR /app

COPY . /app

#TA-LIB
# Install system dependencies for ta-lib
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install ta-lib
RUN curl -L http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz -o ta-lib.tar.gz \
    && tar -xvf ta-lib.tar.gz \
    && cd ta-lib \
    && ./configure --prefix=/usr \
    && make \
    && make install \
    && cd .. \
    && rm -r ta-lib ta-lib.tar.gz
    

RUN pip install -r requirements.txt

CMD [ "python", "main.py" ]