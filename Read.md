

docker image build -t flask_docker_test .

docker run -p 5007:5000 -d flask_docker_test