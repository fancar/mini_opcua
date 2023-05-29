
# build image

docker build -t opc_server .

# run container
docker run --network=host -d --name opc_server_1 opc_server

# or 
docker run -d -p 8070:8080 --name opc_server_1 opc_server