glace: glace.c
	$(CC) glace.c -o glace -Wall -Wextra -pedantic -std=c99 && ./glace test.txt
