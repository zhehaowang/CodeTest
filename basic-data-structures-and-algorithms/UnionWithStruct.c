#include <stdio.h>
#include <string.h>

union ele 
{
    struct 
    {
		int * p;
		int y;
	} e1;
    struct 
    {
        int x;
        union ele *next;
    } e2;
};

union interesting
{
	struct
	{
		int *i2;
		int i1;
	} e1;
};

union ele1
{
	char x1;
	char c1;
	char c2;
};

int main()
{
	union ele e;
	union ele1 e1;
	int x = 0xFF;
	int i = 0;
	
	char dump[100] = "";
	
	
	e.e1.p = 0x5432121110203040;
	e.e1.y = 0x0801020304;
	
	memcpy(dump, &e, sizeof(e));
	
	for (i = 0; i < sizeof(e); i++)
	{
		printf("%X\t", dump[i]);
	}
	printf("\n");

	e.e2.x = 0x1A1B1C1D;
	e.e2.next = 0x112233441E1F1819;
	
	/*
	printf("Size of int*: %d.\n", sizeof(int *));
	printf("Size of next: %d.\n", sizeof(union ele *));
	printf("Size of test union: %d.\n", sizeof(union interesting));
	
	printf("Size of ele: %d.\n", sizeof(e));
	printf("Size of ele1: %d.\n", sizeof(e1));
	*/
	
	memcpy(dump, &e, sizeof(e));
	
	for (i = 0; i < sizeof(e); i++)
	{
		printf("%X\t", dump[i]);
	}
	printf("\n");
	
	return 1;
}

/*
A.
e2.x 	:	0 byte
e2.next : 	8(4) byte
e1.p	:	0 byte
e1.y	: 	8(4) byte

B. 
16 (imagining that pointers take 8 bytes) : what's actually happening
struct e1 takes 8 + 4 bytes, because of alignment of structs, becomes 16 bytes
struct e2 takes 4 + 8 bytes, because of alignment of structs, becomes 16 bytes
Union does not expand the memory used.

Or
8/16 : what should be happening;
According to C, it seems to be 8.

C.
(up->e1.p->e2.next->e1.y) = *(up->e1.p->e2.next->e1.p) - (up->e1.p->e2.x)
*/