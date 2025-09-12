#include <stdio.h>
#include <stdlib.h>

#define MAX 10


int count = 0;

typedef struct stack {
    int items[MAX];
    int top;
} Stack


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
        top++;
    }

    count++;
}

void stackPop(Stack *s) {
    if (stackIsEmpty(s)) {
        printf("The stack is empty.");
    } else {
        
    }
}

void stackPrint(Stack *s) {

}


int main( void ) {
    
}
