#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BUFFER_LENGTH 255

struct sub_data {
  int depth;
  int horizontal;
};

// Must be freed.
struct sub_data *new_sub_data() {
  struct sub_data *out = calloc(1, sizeof(*out));
  out->depth = 0;
  out->horizontal = 0;
  return out;
}

int multiply_positions(struct sub_data *data) {
  return data->horizontal * data->depth;
}

int main(int argc, char *argv[]) {
  char *name;
  FILE *file;
  char buffer[BUFFER_LENGTH];

  name = "input.txt";
  if (argc > 1) {
    name = argv[1];
  }

  file = fopen(name, "r");
  if (file == NULL) {
    printf("%s: Error, file %s not found\n", argv[0], name);
    fclose(file);
    return 1;
  }

  int aim = 0;
  struct sub_data *part_1 = new_sub_data();
  struct sub_data *part_2 = new_sub_data();

  int *amount = calloc(1, sizeof(*amount));
  char *direction = calloc(8, sizeof(*direction));

  while (fgets(buffer, BUFFER_LENGTH, file)) {
    sscanf(buffer, "%s %i", direction, amount);
    if (strcmp(direction, "forward") == 0) {
      part_1->horizontal += *amount;
      part_2->horizontal += *amount;
      part_2->depth += (aim * *amount);
    } else if (strcmp(direction, "up") == 0) {
      aim -= *amount;
      part_1->depth -= *amount;
    } else if (strcmp(direction, "down") == 0) {
      aim += *amount;
      part_1->depth += *amount;
    }
  }

  free(amount);
  free(direction);
  fclose(file);

  printf("part_1: %i\n",  multiply_positions(part_1));
  printf("part_2: %i\n",  multiply_positions(part_2));

  free(part_1);
  free(part_2);

  return 0;
}
