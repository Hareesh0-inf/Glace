glace: glace.c
	$(CC) glace.c -o glace -I/usr/include/python3.12 -lpython3.12 -Wall -Wextra -pedantic -std=c99 && ./glace test.txt
