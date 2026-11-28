#pragma once

#include <vector>

using iterator = std::vector<int>::const_iterator;

// PRE:  for any two indices i and j, v[i] + v[j] <= INT_MAX
// POST: returns the number of indices (i,j), i<j of a vector v
//       that corresponds to the given iterator range such that
//       v[i] + v[j] == sum.
int pairs_with_sum(int sum, iterator begin, iterator end);
