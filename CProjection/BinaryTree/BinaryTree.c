/*************************************************************************
	> File Name: BinaryTree.c
	> Author: quhongbin
	> Mail: 2818777520@qq.com 
	> Created Time: Tue Oct 15 15:12:28 2024
 ************************************************************************/

#include<stdio.h>
#include<stdlib.h>

typedef struct BinaryTree{
    char data;
    struct BinaryTree* lchild;
    struct BinaryTree* rchild;
}BinaryTree;

void createTreeRoot(BinaryTree** T){
    char ch;
    scanf("%c",&ch);
    //ch =data[*index];
    //*index +=1;
    if (ch == '#') {
       *T=NULL;
    }else {
        *T=(BinaryTree*)malloc(sizeof(BinaryTree));
        (*T)->data=ch;
        createTreeRoot(&((*T)->lchild));
        createTreeRoot(&((*T)->rchild));
    }
}

void preOrder(BinaryTree* T){
    if (T == NULL) {
        return;
    }else {
        printf("%c",T->data);
        preOrder(T->lchild);
        preOrder(T->rchild);
    }
}

void postOrder(BinaryTree* T){
    if (T == NULL) {
        return;
    }else {
        postOrder(T->lchild);
        postOrder(T->rchild);
        printf("%c",T->data);
    }
}

void inOrder(BinaryTree* T){
    if (T == NULL) {
        return;
    }else {
        inOrder(T->lchild);
        printf("%c",T->data);
        inOrder(T->rchild);
    }
}
int main(int argc,char* argv[]){
    BinaryTree* T;
    int index=0;
    createTreeRoot(&T);
    preOrder(T); 
    printf("\n");
    inOrder(T); 
    printf("\n");
    postOrder(T); 
    printf("\n");
    return 0;
}
