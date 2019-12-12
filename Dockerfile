FROM python:3.6
RUN apt-get update
RUN apt-get install -y --no-install-recommends \
	python-opencv \
	libvips
ADD . /code
WORKDIR /code
RUN pip install -r requirements/reproducing.txt
CMD jupyter lab --ip 0.0.0.0 --no-browser --allow-root