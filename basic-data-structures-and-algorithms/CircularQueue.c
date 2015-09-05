#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//Entry: Apr 30th, 11:00PM, low status, finished 11:18PM, submitted 11:20PM
//Array based CircularQueue:

#define MAXSIZE 10

struct data
{
	int x;
	int y;
};

struct queueStruct
{
	struct data * queueData;
	int head;
	int tail;
};

int enqueue(struct queueStruct *queue, struct data in)
{
	if ((queue->tail + 1) % MAXSIZE == queue->head)
	{
		printf("Queue full.\n");
		return 0;
	}
	else
	{
		memcpy(&(queue->queueData[(queue->head + 1) % MAXSIZE]), &in, sizeof(struct data));
		queue->tail = (queue->tail + 1) % MAXSIZE;
		return 1;
	}
}

int dequeue(struct queueStruct *queue, struct data *out)
{
	if (queue->tail == queue->head)
	{
		printf("Queue empty.\n");
		return 0;
	}
	else
	{
		memcpy(out, &(queue->queueData[queue->head]), sizeof(struct data));
		queue->head = (queue->head + 1) % MAXSIZE;
		return 1;
	}
}

int debug(struct queueStruct *queue)
{
	int i = 0;
	for (i = queue->head; i != queue->tail; i = (i + 1) % MAXSIZE)
	{
		printf("%d %d\n", queue->queueData[i].x, queue->queueData[i].y);
	}
	return 1;
}

int main()
{
	struct queueStruct * queue = (struct queueStruct *)malloc(sizeof(struct data) * MAXSIZE);
	
	queue->queueData = (struct data *)malloc(sizeof(struct data) * MAXSIZE);
	queue->head = 0;
	queue->tail = 0;

	struct data in, out;
	in.x = 1;
	in.y = 2;

	enqueue(queue, in);
	dequeue(queue, &out);
	enqueue(queue, in);
	
	debug(queue);

	return 1;
}

