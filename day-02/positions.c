#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BUFFER_LENGTH 255

struct sub_data {
  int depth;
  int horizontal;
};

// Initialize a sub_data struct. The returned struct is created with calloc()
// and must be freed appropriately after use.
struct sub_data *new_sub_data() {
  struct sub_data *out = calloc(1, sizeof(*out));
  out->depth = 0;
  out->horizontal = 0;
  return out;
}

// Do the final multiplication of the challenge.
int multiply_positions(struct sub_data *data) {
  return data->horizontal * data->depth;
}

int main(int argc, char *argv[]) {
  char *name; // File name of input
  FILE *file; // File stream of all input data

  name = "input.txt";
  if (argc > 1)
    name = argv[1];

  file = fopen(name, "r");
  if (file == NULL) {
    printf("%s: Error, file %s not found\n", argv[0], name);
    fclose(file);
    return 1;
  }

  struct sub_data *part_1 = new_sub_data();
  struct sub_data *part_2 = new_sub_data();

  int aim = 0;
  char *direction = calloc(8, sizeof(*direction)); // Direciton in input line
  int *amount = calloc(1, sizeof(*amount));        // Amount in input line

  // Current line being read
  char *line = calloc(BUFFER_LENGTH, sizeof(*line));
  while (fgets(line, BUFFER_LENGTH, file)) {

    // Parse the current line into direction and amount
    sscanf(line, "%s %i", direction, amount);

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

  free(line);
  free(amount);
  free(direction);
  fclose(file);

  printf("Part 1: %i\n", multiply_positions(part_1));
  printf("Part 2: %i\n", multiply_positions(part_2));

  free(part_1);
  free(part_2);

  return 0;
}
