FROM python:3.6
RUN apt-get update
RUN apt-get install -y \
	python-opencv \
	libvips
ADD ./requirements /code
WORKDIR /code
RUN pip install -r requirements/reproducing.txt
CMD ['python test_docker_build.py']