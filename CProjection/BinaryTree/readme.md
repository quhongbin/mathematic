二级指针依次取值
```mermaid
flowchart LR
    id[int** p
    0x003]
    id1[int* p
    0x001
    0x002]
    id2[a
    10
    0x001]
    id--第一次取值为* p的地址-->id1
    id1--第二次取值为a的值-->id2
    id--值相等-->id2
```
> 先取得int*(*p)=int\*(0x002)=10,如果struct不同不知道能否取得

```C
#include<stdio.h>
#include <time.h>

int main(){
int a = 100 ;
&a ;
int* p = &a;
int* p2 = NULL ;
p2 = &a ;
int b = 200 ;
*p2 = b ;
int** p3 = &p2 ;
printf("%d",** p3);
}
```
> 结果为200
```C
#include<stdio.h>
#include <time.h>

int main(){
int a = 100 ;
&a ;
int* p = &a;
int* p2 = NULL ;
p2 = &a ;
char b = 200 ;
*p2 = b ;
int** p3 = &p2 ;
printf("%d",** p3);
}
```
> 结果为-56

```c
typedef struct Node
{
    int data;
    struct Node* next;
}Node;


void headInsert(Node* head_node,int data){
    Node* node=(Node*)malloc(sizeof(Node));
    node->next=head_node->next;             //将头节点的Next*赋给新建Node->next
    node->data=data;                        //
    head_node->next=node;                   //把头节点的Next*指向当前的新建的节点
    head_node->data++;                      //
}
```
Node结构体指针node指向结构体Node
```c
typedef struct BiTree{
    char data;
    struct BiTree* leftChild;
    struct BiTree* rightChild;
}BiTree ;

void createTree(BiTree* *T){   //*T本质上是一个地址
    char ch;
    scanf("%c",&ch);
    if (ch == '#') {
       *T=NULL; 
    }else {
        (*T)=(BiTree*)malloc(sizeof(BiTree));
        (*T)->data=ch;
        createTree(&((*T)->leftChild));      //  (*T)->leftChild访问当前地址，结构体中的leftChild.leftChild嵌在头节点里
        createTree(&((*T)->rightChild));
    }
}
```
BiTree结构体指针*root指针指向结构体BinaryTree



```mermaid
graph LR
    subgraph node1
    direction LR
        p[p]
        add[0x001]
        a[a]
        val1[1]
    end
    subgraph node2
    direction LR
        *p[*p]
        add1[0x002]
        b[b]
        a_addr[0x001]
    end
    subgraph node3
    direction LR
        **p[**p]
        add2[0x003]
        *b[*b]
        b_addr[0x002]
    end
    subgraph node4
    direction LR
        int*[int*]
        add3[0x004]
    end
    subgraph node5
    direction LR
        int[5]
        add4[0x005]
    end
    *b-->a_addr
    b-->val1
    *b--让该指针重新指
        向新开辟的空间-->int*
    add3--**p=3操作让0x004指向的
               对象值为3-->node5
```

```C
#include <stdio.h>
#include <stdlib.h>

void f(int **p){
    **p=2;
    *p=(int*)malloc(sizeof(int));
    **p=3;
    printf("%d\n",**p);
}

int main(){
    int a =1;
    int *b =&a;
    f(&b);
    printf("%d %d",a,a);
}
```