A "getting started" manual for Dockers. CIS 322, Introduction to Software Engineering, at the University of Oregon. Reference: https://docs.docker.com/engine/reference/builder/

# Basic commands

* Command to get information about docker setup on your machine

  ~~~~
  docker info
  ~~~~

* List of docker containers running can be found using

  ~~~~
  docker ps -a
  ~~~~

* Remove containers using

  ~~~~
  sudo docker rm <Container Name>
  ~~~~

* To run docker container use

  ~~~~
  docker run -h CONTAINER1 -i -t debian /bin/bash
  docker run -h CONTAINER1 -i -t ubuntu /bin/bash
  ~~~~

  Here, -h is used to specify a container name, -t to start with tty, and -i means interactive. Note: second times will be quick because of caching.

* Docker with networking

  ~~~~
  docker run -h CONTAINER2 -i -t --net="bridge" debian /bin/bash
  ~~~~

* When the containers are not running and when you're done, kill them using

  ~~~~
  docker rm `docker ps --no-trunc -aq`
  ~~~~

* Rename using

  ~~~~
  docker rename name_v0 name_v1
  ~~~~

