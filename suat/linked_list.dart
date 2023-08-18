void main() {
  MyLinkedList obj = MyLinkedList();
  obj.addAtHead(1);
  // obj.addAtHead(2);
  // obj.addAtHead(1);
  obj.addAtTail(3);
  obj.addAtIndex(3, 2);
  // print(obj.get(1));
  // obj.deleteAtIndex(1);
  // print(obj.get(1));
  // print(obj.get(3));
  // obj.deleteAtIndex(3);
  // obj.deleteAtIndex(0);

  // obj.addAtIndex(0, 20);
  // obj.addAtIndex(1, 30);
  // print(obj.get(1));

  return;
}

class MyLinkedList {
  // MyLinkedList() {}
  MyNode? head;

  int get(int index) {
    if (head == null) {
      return -1;
    }
    int i = 0;
    MyNode pointer = head!;
    while (i < index) {
      if (pointer.next == null) {
        return -1;
      } else {
        pointer = pointer.next!;
      }
      i++;
    }
    return pointer.val;
  }

  void addAtHead(int val) {
    if (head == null) {
      head = MyNode(val: val);
    } else {
      head = MyNode(val: val, next: head);
    }
  }

  void addAtTail(int val) {
    if (head == null) {
      head = MyNode(val: val);
    } else {
      MyNode cur = head!;
      while (cur.next != null) {
        cur = cur.next!;
      }
      cur.next = MyNode(val: val);
    }
  }

  void addAtIndex(int index, int val) {
    if (head == null || index == 0) {
      addAtHead(val);
      return;
    }
    int i = 0;
    MyNode pointer = head!;
    while (i < index - 1) {
      if (pointer.next != null) {
        pointer = pointer.next!;
        i++;
      } else {
        return;
      }
    }
    var newNode = MyNode(val: val, next: pointer.next);
    pointer.next = newNode;
  }

  void deleteAtIndex(int index) {
    if (head == null) {
      return;
    }
    if (index == 0) {
      head = head!.next;
      return;
    }
    int i = 0;
    MyNode? pointer = head;
    while (i < index - 1) {
      if (pointer?.next != null) {
        pointer = pointer?.next;
        i++;
      } else {
        return;
      }
    }
    pointer?.next = pointer.next?.next;
  }
}

class MyNode<T> {
  T val;
  MyNode? next;
  MyNode({required this.val, this.next});
}
