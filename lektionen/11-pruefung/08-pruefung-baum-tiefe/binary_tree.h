#include <cassert>

// A binary tree node has data (an integer between 0 and 9), a pointer to the
// left child and a pointer to the right child
struct TreeNode {
  int data; //INV: between 0 and 9
  TreeNode *left;
  TreeNode *right;
};


/***
 * PRE: node is a valid pointer to an instance for kind TreeNode, and not nullptr
 * POST: returns the maximum depth of the binary tree starting from node
 *
 * Examples:
 *
 *      3     -> 1
 *
 *
 *      5
 *     / \
 *    2   7   -> 3
 *       /
 *      4
 ***/
int get_max_depth(TreeNode *node){
  assert(node != nullptr);
  //TODO: maximale Tiefe rekursiv berechnen — siehe Hinweise in der README
  return 0;
}
