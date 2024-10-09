#include<stdio.h>
#include<stdlib.h>
typedef struct Node
{
    int data;
    struct Node* next;
}Node;

Node* initLinkList(){
    Node* init_node=(Node*)malloc(sizeof(Node));
    init_node->data=0;
    init_node->next=NULL;
    return init_node;
};

void headInsert(Node* head_node,int data){
    Node* node=(Node*)malloc(sizeof(Node));
    node->next=head_node->next;
    node->data=data;
    head_node->next=node;  //
    head_node->data++;
};

void tailInsert(Node* head_node,int data){
    Node* head=head_node;
    Node* node=(Node*)malloc(sizeof(Node));
    node->data=data;
    node->next=NULL;
    head_node=head_node->next;
    while (head_node->next)
    {
        head_node=head_node->next;
    }
    head_node->next=node;
    head->data++;
}

void Delete(Node* head_node,int data){
    Node* current = head_node->next;
    Node* pre_node= head_node; 
    while (current){
        if (current->data==data){
           pre_node->next=current->next; 
           free(current);
           break;
        }
        pre_node=current;
        current=current->next;
    }
    
}



void printList(Node* input_list){
    input_list=input_list->next;
    while (input_list)
    {
        printf("%d",input_list->data);
        input_list=input_list->next;
    }
    printf("\n");
}

int main(){
    Node* List=initLinkList();
    headInsert(List,1);
    headInsert(List,2);
    tailInsert(List,3);
    tailInsert(List,4);
    Delete(List,3);
    printList(List);
    return 0;
}
