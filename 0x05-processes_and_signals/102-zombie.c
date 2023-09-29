#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>

/**
 * infinite_while - creates an infinite loop to make the program hang
 * Return: always 0
 */
int infinite_while(void)
{
    while (1)
    {
        sleep(1);
    }
    return (0);
}

/**
 * main - Program enty point
 * Discription: A program descripe zombie process
 * Return: 0
 */
int main(void)
{
    int count;
    pid_t pid;

    for (count = 0 ; count < 5 ; count++)
    {
        /* Forking to get parent child */
        pid = fork();

        if (pid < 0)
        {
            /* If pid < 0 so there is fork error */
            perror("Fork error");
            exit(0);
        }

        else if (pid == 0)
        {
            /* Child process */
            /* Terminate it to become zombie */
            exit(0);
        }

        else
        {
            /* Print the parent process */
            printf("Zombie process created, PID: %d\n", pid);
            /* Sleep for a while to indecate the zombie process */
            sleep(2);
        }
    }
    infinite_while();
    return (0);
}
