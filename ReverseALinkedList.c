#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct data
{
	int x;
	int y;
};

struct node
{
	struct data nodeData;
	struct node *next;
};

//issue: initialize can not be used to initialize head, temp, or tail.
//malloced in initialize is freed after returning?
int initialize(struct node * temp)
{
	temp = (struct node *)malloc(sizeof(struct node));
	temp->next = NULL;
	return 1;
}

int append(struct node *tail, struct data dataIn)
{
	struct node * temp = (struct node *)malloc(sizeof(struct node));
	temp->next = NULL;
	memcpy(&(temp->nodeData), &dataIn, sizeof(dataIn));

	tail->next = temp;
	tail = tail->next;
	return 1;
}

int debug(struct node *head)
{
	struct node *temp = head->next;
	while (temp!=NULL)
	{
		printf("%d %d\n", temp->nodeData.x, temp->nodeData.y);
		temp = temp->next;
	}
}

int main()
{
	struct node *head, *tail, *temp;
//	initialize(head);
//	initialize(tail);

	tail = (struct node *)malloc(sizeof(struct node));
	tail->next = NULL;

	head = (struct node *)malloc(sizeof(struct node));
	head->next = NULL;

	struct data dataIn;
	dataIn.x = 1;
	dataIn.y = 1;

	temp = (struct node *)malloc(sizeof(struct node));
	temp->next = NULL;
	memcpy(&(temp->nodeData), &dataIn, sizeof(dataIn));

	tail->next = temp;
	tail = tail->next;
	head->next = tail;

	append(tail, dataIn);
	append(tail, dataIn);
	debug(head);

	return 1;
}
