#include <string>
#include <iostream>
#include <cassert>
#include "binary_tree.h"


// ----------------------------------------------------------------------
// NOTE: You most likely don't need to read and understand
// the content of this file
// ----------------------------------------------------------------------

// function to return the index of closing parenthesis matching open parenthesis
// at position si
int findIndex(std::string str, int si, int ei)
{
    if (si > ei){
      return -1;
    }

    int counter = 0;
    for (int i = si; i <= ei; i++) {
      if (str[i] == '(') {
        ++counter;
      } else if (str[i] == ')') {
        --counter;
        // if counter is 0, we found the right closing paranthesis
        if (counter == 0){
          return i;
        }

      }
    }
    // if not found the input string is invalid
    assert(false);
}

// function to construct tree from string
TreeNode* treeFromString(std::string str, int si, int ei)
{
  // Base case
  if (si > ei)
      return NULL;

  //check that input is a digit
  assert(str[si] - '0' >= 0 && str[si] - '0' <= 9);

  // new node
  TreeNode* root = new TreeNode{(int) str[si] - '0', nullptr, nullptr};

  int index = -1;

  // if the next char is '(' find the index of its complement ')'
  if (si + 1 <= ei && str[si + 1] == '(')
      index = findIndex(str, si + 1, ei);

  // if valid index was found, build left and right subtrees
  if (index != -1) {
      root->left = treeFromString(str, si + 2, index - 1);
      root->right = treeFromString(str, index + 2, ei - 1);
  }
  return root;
}

int main()
{
    std::cout << "Enter a binary tree in bracket notation:\n";
    std::string str;
    std::cin >> str;
    TreeNode* root = treeFromString(str, 0, str.length() - 1);
    int count = count_nodes(root);

    const char marker = '|';
    std::cout << "Number of nodes = "
            << marker
            << count
            << marker
            << '\n';

  return 0;
}
