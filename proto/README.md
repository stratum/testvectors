# Proto Definitions

## Running protoc compiler to generate go code
Build docker container
```bash
docker build -t protoc-go .
```

Run docker container by mounting 'proto' directory and using 'compile-protos.sh' as entrypoint
```bash
docker run -it --rm -v `pwd`:/root -w /root --entrypoint ./compile-protos.sh protoc-go
```