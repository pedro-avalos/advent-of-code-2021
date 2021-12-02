#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]) {
  char *name;
  FILE *file;
  int horizontal = 0, depth = 0, buffer_length = 255;
  char buffer[buffer_length];

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

  int *amount = calloc(1, sizeof(*amount));
  char *direction = calloc(8, sizeof(*direction));

  while (fgets(buffer, buffer_length, file)) {
    sscanf(buffer, "%s %i", direction, amount);
    if (strcmp(direction, "forward") == 0)
      horizontal += *amount;
    else if (strcmp(direction, "up") == 0)
      depth -= *amount;
    else if (strcmp(direction, "down") == 0)
      depth += *amount;
  }
  free(amount);
  free(direction);
  fclose(file);

  printf("%i\n", horizontal * depth);

  return 0;
}
