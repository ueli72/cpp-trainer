#pragma once

#include <cassert>

// Ein Baumknoten hat Daten (eine Ziffer zwischen 0 und 9), einen Zeiger
// auf das linke und einen auf das rechte Kind.
struct TreeNode {
  int data;              // INV: zwischen 0 und 9
  TreeNode *left;
  TreeNode *right;
};


/***
 * PRE: node is a valid pointer to a TreeNode, or nullptr (empty subtree)
 * POST: returns the number of nodes in the tree starting from node
 *
 * Examples:
 *
 *      3     -> 1
 *
 *
 *      5
 *     / \
 *    2   7   -> 3
 ***/
int count_nodes(TreeNode* node){
  // TODO: nullptr abfangen (leerer Teilbaum = 0 Knoten), dann
  //   1 + linke Knoten + rechte Knoten — rekursiv
  return 0;
}
