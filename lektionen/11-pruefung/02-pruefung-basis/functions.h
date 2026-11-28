#pragma once

// PRE: A number >= 0 in base 10, and a base 1 < b < 10
//
// POST: Return the number in base b, i.e., return the number whose digits
//       are the digits of the representation of the input number n in base b
//
// Examples:
//    * 10 2 ~~> 1010
//    * 14 9 ~~> 15
int convert_base(int n, int b) {
  // TODO: Ziffern ableiten (n % b, n /= b) und mit dem Stellenwert
  //   (1, 10, 100, ...) zu einer Zahl zusammenbauen — wie in Vorstufe 01.
  return 0;
}
