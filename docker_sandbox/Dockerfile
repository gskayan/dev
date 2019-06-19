FROM gcc:7
WORKDIR /gleb_app
ADD ./test_docker.cpp /gleb_app
RUN g++ -o test_docker test_docker.cpp
CMD ["./test_docker"]
