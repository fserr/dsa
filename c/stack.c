#include <stdio.h>
#include <stdlib.h>

#define MAX 10


int count = 0;

typedef struct stack {
    int items[MAX];
    int top;
} Stack;


void stackInit(Stack *s) {
    s->top = -1;    
}

int stackIsFull(Stack *s) {
    if (s->top == MAX-1)    return 1;
    return 0;
}

int stackIsEmpty(Stack *s) {
    if (s->top == -1)   return 1;
    return 0;
}

void stackPush(Stack *s, int newItem) {
    if (stackIsFull(s)) {
        printf("The stack is full.\n");
    } else {
        s->items[s->top+1] = newItem;
        s->top++;
    }

    count++;
}

int stackPop(Stack *s) {
    if (stackIsEmpty(s)) {
        printf("The stack is empty.");
        return -1;
    }
    
    int popped = s->top;
    s->top--;        

    return popped;
}

void stackPrint(Stack *s) {
    printf("[");
    for (int i = 0; i <= s->top; i++) {
        printf(" %d ", s->items[i]);
    }

    printf("]\n");
}

void stackPeek(Stack *s) {
    printf("Stack top element: %d\n", s->items[s->top]);
}


int main( void ) {
    Stack s;
    stackInit(&s);

    stackPush(&s, 1);
    stackPush(&s, 2);
    stackPush(&s, 3);
    stackPush(&s, 4);
    stackPeek(&s);

    stackPrint(&s);

    stackPop(&s);
    stackPop(&s);

    stackPeek(&s);

    stackPrint(&s);
}
