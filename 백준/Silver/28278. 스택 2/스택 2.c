#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef int element;
typedef struct {
    element *data;
    int capacity;
    int top;
} StackType;

void init_stack(StackType *s) {
    s->top = -1;
    s->capacity = 1;
    s->data = (element *)malloc(s->capacity * sizeof(element));
    if(s->data == NULL)
        exit(1);
}

int is_empty(StackType *s) {
    return (s->top == -1);
}

int is_full(StackType *s) {
    return (s->top == s->capacity - 1);
}

void push(StackType *s, element item) {
    if(is_full(s)) {
        s->capacity *= 2;
        s->data = (element *)realloc(s->data, s->capacity * sizeof(element));
    } 
    s->data[++(s->top)] = item;
}

element pop(StackType *s) {
    if(is_empty(s)) 
        return -1;
    return s->data[(s->top)--];
}

element peek(StackType *s) {
    if(is_empty(s))
        return -1;
    return s->data[s->top];
}

int main(void)
{
    StackType s;
    init_stack(&s);
    int T;
    scanf("%d", &T);
    
    for(int i=0 ; i<T ; i++) {
        int op;
        scanf("%d", &op);

        if(op == 1) {
            int item;
            scanf("%d", &item);
            push(&s, item);
        }

        else if(op == 2) {
            printf("%d\n", pop(&s));
        }

        else if(op == 3) {
            printf("%d\n", s.top + 1);
        }

        else if(op == 4) {
            printf("%d\n", is_empty(&s));
        }

        else
            printf("%d\n", peek(&s));
    }
    free(s.data);
    return 0;
}