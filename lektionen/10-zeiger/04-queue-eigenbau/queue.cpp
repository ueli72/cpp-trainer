#include <iostream>
#include <cassert>
#include "queue.h"

/////////////////////////////////////////////////////////////////////////////
// IMPLEMENTATION
/////////////////////////////////////////////////////////////////////////////

Queue::Queue() {
  // TODO: leere Queue — beide Zeiger auf nullptr
}

void Queue::enqueue(int value) {
  // TODO: neuen Knoten am ENDE anhaengen (Invariante halten!)
}

int Queue::dequeue() {
  // TODO: ersten Knoten entfernen, Wert zurueckgeben, Knoten freigeben
  return 0;
}

bool Queue::is_empty() const {
  // TODO
  return false;
}

void Queue::print_reverse() const {
  // TODO: Werte in umgekehrter Reihenfolge, jeder mit einem Leerzeichen
  //   davor — Rekursiv-Muster wie bei print_node, nur umgekehrt
}

// PRE: -
// POST: print the sequence of integers in nodes reachable from n,
//       in order, with one space before each integer.
void print_node(Node* n) {
  if (n != nullptr) {
    std::cout << " " << n->value;
    print_node(n->next);
  }
}


void Queue::print() const {
  std::cout << "[";
  if (first != nullptr) {
    std::cout << first->value;
    print_node(first->next);
  }
  std::cout << "]";
}
