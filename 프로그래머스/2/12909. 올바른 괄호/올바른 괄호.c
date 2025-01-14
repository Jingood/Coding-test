#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>
#define MAX_STACK_SIZE 100000

typedef struct {
    char data[MAX_STACK_SIZE];
    int top;
} StackType;

void init_stack(StackType *in)
{
    in->top = -1;
}

int is_empty(StackType *in)
{
    return (in->top == -1);
}

int is_full(StackType *in)
{
    return (in->top == (MAX_STACK_SIZE - 1));
}

void push(StackType *in, char item)
{
    if(is_full(in))
        return;
    else
        in->data[++(in->top)] = item;
        
}

char pop(StackType *in)
{
    if(is_empty(in))
       exit(1);
    else
       return in->data[(in->top)--];
}
       
bool solution(const char* s) {
    StackType in;
    char ch, open_ch;
    int n = strlen(s);
    init_stack(&in);
    for(int i=0 ; i<n ; i++) {
        ch = s[i];
        switch(ch) {
        case '(':
            push(&in, ch);
            break;
        case ')':
            if(is_empty(&in))
                return 0;
            else { 
                open_ch = pop(&in);
                if(open_ch == '(' && ch != ')')
                    return 0;
            }   
            break;
        }
    }
    if(!is_empty(&in))
        return 0;
    return 1;
}