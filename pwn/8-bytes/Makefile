CC=gcc
CFLAGS=-no-pie

TARGET=8_Bytes

all: $(TARGET)

$(TARGET): 8_Bytes.c
	$(CC) $(CFLAGS) 8_Bytes.c -o $(TARGET)

clean:
	rm -f $(TARGET)
