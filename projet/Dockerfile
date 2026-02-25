FROM golang:latest AS builder

WORKDIR /app

COPY clicker_go/go.mod clicker_go/go.sum ./
RUN go mod download

COPY clicker_go/ .

RUN CGO_ENABLED=0 GOOS=linux go build -o server main.go
FROM alpine:latest

WORKDIR /root/

COPY --from=builder /app/server .

COPY static/ ./static

EXPOSE 8888

CMD ["./server"]