#include <stdio.h>
#include <objpak.h>
int main(int argc,char **argv)
{
    id set = [Set new];
    [set do:{ :each | printf("hello, World!\n"; }];
    return 0;
}