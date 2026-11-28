#include <iostream>
#include <cassert>
#include "functions.h"

// ----------------------------------------------------------------------
// NOTE: You most likely don't need to read and understand
// the content of this file
// ----------------------------------------------------------------------

int main() {
  std::cout << "Enter a number to convert, followed by the base to convert it to\n";
  int value;
  std::cin >> value;
  assert (0 <= value);
  int base;
  std::cin >> base;
  assert (1 < base && base < 10);

  std::cout << "convert_base = "
            << convert_base(value, base) << '\n';
  return 0;
}
