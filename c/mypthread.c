#include <stdio.h>
#include <pthread.h>
#include <sys/time.h>
#include <string.h>
#define MAX 10

pthread_t thread[2];
pthread_mutex_t mut;
int number = 0, i;

void *thread1()
{
    printf("thread1 : I'm thread1 \n");

    for(i = 0; i < MAX; i++)
    {
        printf("thread1 : number = %d\n", number);
        pthread_mutex_lock(&mut);
        number++;
        pthread_mutex_unlock(&mut);
        sleep(2);
    }

    printf("thread1 : ä¸ï
}
