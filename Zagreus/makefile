all: main

colors.o: colors.c colors.h
	gcc -c colors.c

avx512_vnni.o: avx512_vnni.c avx512_vnni.h
	gcc -c avx512_vnni.c -mavx512f -march=cascadelake

avx512.o: avx512.c avx512.h
	gcc -c avx512.c -mavx512f

main.o: main.c avx512.h
	gcc -c main.c -mavx512f

main: main.o avx512.o avx512_vnni.o colors.o globals.h
	gcc -o main main.o avx512.o avx512_vnni.o colors.o -mavx512f -g

clean:
	rm -f main *.o

exec:
	./main 1 5 16 1