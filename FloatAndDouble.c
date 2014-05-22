//Float and double

#include <stdio.h>
#include <string.h>
#include <time.h>

#define MAXLEN 1000

int main()
{
	float f1 = 0;
	float f2 = 1 / (1 << 127);
	
	double d1;
	printf("Size of float and double: %d %d\n", sizeof(f1), sizeof(d1));
	
	int i = 0;
	char str[MAXLEN] = {"12345678"};
	/*
	double di = 0;
	for (i = - (1 << 30) ; i < 1 << 30; i++)
	{
		di = (double)i;
		if ((float)i != (float)di)
		{
			printf("Not Equal: i\n", i);
		}
	}
	*/
	
	char magic8ball[8][8][8];
	
	int j = 0, k = 0;
	srand(time(NULL));
	
	for (i = 0; i<8; i++)
	{
		for (j = 0; j<8; j++)
		{
			for (k = 0; k<8; k++)
			{
				magic8ball[i][j][k] = (rand() + k) % 255;
			}
		}
	}
	
	printf("%s\n", magic8ball[3][2]);
	strcpy(str, magic8ball[3][2]);
	
	for (i = 0; i < strlen(str); i++)
	{
		printf("%X\t", str[i]);
	}
	printf("\n");
	return 1;
	
}