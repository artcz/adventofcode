#include <stdio.h>
#include <stdlib.h>

#define ARRSIZE 300

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}


void bubble_sort(int array[], int n) {
    int i, j;
    for (i = 0; i < n; i++) {
        for (j = 0; j < n-i-1; j++) {
            if (array[j] > array[j+1]) {
                swap(&array[j], &array[j+1]);
            }
        }
    }
}

int main() {
    int arr[ARRSIZE];
    int i = 0;
    int part1 = 0;
    int part2 = 0;

    for(i = 0; i < ARRSIZE; i++) {
        arr[i] = 0;
    }

    int number;
    int curr = 0;
    int acc = 0;
    char *line = NULL;
    size_t len = 0;
    FILE *fp;

    fp = fopen("./input", "r");
    while(getline(&line, &len, fp) != EOF) {
        if(line[0] == '\n') {
            arr[curr] = acc;
            curr++;
            acc = 0;
            continue;
        }

        number = atoi(line);
        acc += number;
    }
    fclose(fp);

    bubble_sort(arr, ARRSIZE);

    part1 = arr[ARRSIZE-1];
    part2 = 0;
    for(i=1; i<=3; i++) part2 += arr[ARRSIZE-i];

    printf("Part1: %d\n", part1);
    printf("Part2: %d\n", part2);

}
