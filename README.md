# opc mini tits

the thing dynamicaly generates an opc-tree based on objectJSON recieved via HTTP-server by:
 POST on http://localhost:8072

opcua server endpoint
"opc.tcp://0.0.0.0:4840/freeopcua/server/"

## to build the image

docker build -t opc_server .

## to run the container
docker run --network=host -d --name opc_server_1 opc_server

## or 
docker run -d -p 8070:8072 -p 4840:4840 --name opc_server_1 opc_server