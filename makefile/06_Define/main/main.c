/*************************************************************************
	> File Name: main.c
	> Author: kelongwen
	> Mail: kelongwen@huawei.com 
	> Created Time: 2014年10月19日 星期日 11时59分52秒
 ************************************************************************/
#include <stdio.h>

#include "hello.h"

int main()
{
	Hello();
#ifdef ATS_VCU
	printf("ATS_VCU.\n");
#endif
	return 0;
}
