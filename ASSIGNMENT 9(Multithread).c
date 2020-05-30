//ASSIGNMENT 9 
#include <stdio.h> 
#include<stdlib.h>
#include<unistd.h>
#include <time.h> 
#include<pthread.h>

//declaring globally to use in both threads ssame value
time_t s;                         // time_t is a datatype to store system time.
struct tm* current_time;          // struct tm is a structure used to hold the time and date.

pthread_mutex_t lock = PTHREAD_MUTEX_INITIALIZER;  //initialize mutex


  
void *thread1(void *vargp){

pthread_mutex_lock(&lock); 
printf("--INSIDE THREAD 1-- \nThread 1 calculates calendar time in seconds using time() function.\n\n");
s = time(NULL);       // returns current calendar time in seconds since 1 JAN 1970  
pthread_mutex_unlock(&lock); 
}

void *thread2(void *vargp){

printf("--INSIDE THREAD 2-- \nThread 2 converts calendar time in seconds to current time in HH:MM:SS using localtime() function \n\n");
pthread_mutex_lock(&lock); 
current_time = localtime(&s);  
// the localtime function converts a calendar time and returns a pointer to a structure 									
printf("Current Time : %02d:%02d:%02d\n\n", current_time->tm_hour, current_time->tm_min, current_time->tm_sec);
							 			 // print time in hours, minutes and seconds

pthread_mutex_unlock(&lock);
}


int main(){

	pthread_t thread_id1, thread_id2;
	printf("\n-----INSIDE MAIN(BEFORE THREADS)-----\n\n");
	
	pthread_create(&(thread_id1), NULL, thread1, NULL);
	pthread_create(&(thread_id2), NULL, thread2, NULL);
	
	pthread_join(thread_id1, NULL);
	pthread_join(thread_id2, NULL);
	
	printf("-----INSIDE MAIN(AFTER THREADS)-----\n\n");
	return 0;
}

  
