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