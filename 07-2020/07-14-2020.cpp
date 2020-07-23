// Author: John Furlong (Help from Geeksforgeeks)
// # Given the root of a binary search tree, and a target K, return two nodes in the tree whose sum equals K.

// # For example, given the following tree and K of 20

// #     10
// #    /   \
// #  5      15
// #        /  \
// #      11    15
// # Return the nodes 5 and 15.

/* 
    Solution:
        The key is using the structure of a BST to your advantage -- the idea is same as finding the pair in a sorted array.
        We traverse the BST in a Forward In-Order traversal, and a Reversed In-Order traversal simultaneously.

    Time Complexity: O(n) 
        Since we use a stack to mimic the problem of finding a pair inside of a sorted array, we are able to pair nodes in O(N) time, 
        where N is the number of nodes in the BST.

    Space Complexity: O(Logn)
        Assuming that the BST is balanced, the height will always be O(Logn), and therefore the number of functions in the call stack
        will never be more than O(Logn)
*/

#include <iostream>
using namespace std;
#define MAX_SIZE 100

// BST Node
struct Node{
    int data;
    Node* left;
    Node* right;
};

// Utility Function to add new nodes
struct Node *newNode(int data){
    struct Node *temp = (struct Node *)malloc(sizeof(struct Node));
    temp->data = data;
    temp->left = temp->right = NULL;
    return temp;
};

// Insert new nodes into a BST
struct Node *insertBST(struct Node *node, int data){
    if(node == NULL) return newNode(data);

    else{
        struct Node *temp;

        if(data < node->data){
            temp = insertBST(node->left, data);
            node->left = temp;
        }
        else if(data > node->data){
            temp = insertBST(node->right, data);
            node->right = temp;
        }
        return node;
    }
}

// Implementation of a stack (of Nodes)
class Stack{
    private:
        int top;
        int maxSize;
        // Pointer to the array of Nodes
        Node* data;

    public:
        // Constructor
        Stack(int size){
            top = -1;
            maxSize = MAX_SIZE;
            // Stack will use an array of Nodes
            data = new Node[maxSize];
        }
        // Deconstructor
        ~Stack(){
            delete data;
        }

        // Is the stack full?
        bool isFull(){
            return true ? (top == maxSize - 1) : false;
        }

        // Is the stack empty?
        bool isEmpty(){
            return true ? (top == -1) : false;
        }

        // Push
        int push(Node value){
            if(isFull())
                return -1;
            
            top++;
            data[top] = value;
            
            return 0;
        }

        // Pop
        Node* pop(){
            if(isEmpty())
                return NULL;
            
            return &data[top--];
        }
};

// Function searches for a pair of nodes from the same level in a BST which sum to a given target
// If no pair exists, returns false.
bool findPair(Node* root, int target){
    // 
    Stack s1 = Stack(MAX_SIZE);
    Stack s2 = Stack(MAX_SIZE);

    // Flags indicate whether to continue (forwards/reverse) in-order traversal
    bool flag1 = false, flag2 = false;
    // Val holds the value of the current node
    int val1 = 0, val2 = 0;
    // Temporary node pointers for each traversal
    Node *tmp1 = root, *tmp2 = root;

    while(1){
        // Forwards in-order traversal
        while(!flag1){
            if(tmp1 != NULL){
                s1.push(*tmp1);
                tmp1 = tmp1->left;
            }
            else{
                if(s1.isEmpty())
                    flag1 = true;
                else{
                    tmp1 = s1.pop();
                    val1 = tmp1->data;
                    tmp1 = tmp1->right;
                    flag1 = true;
                }
            }
        }

        // Reversed, in-order traversal (right subtree before left)
        while(!flag2){
            if(tmp2 != NULL){
                s2.push(*tmp2);
                tmp2 = tmp2->right;
            }
            else{
                if(s2.isEmpty())
                    flag2 = true;
                else{
                    tmp2 = s2.pop();
                    val2 = tmp2->data;
                    tmp2 = tmp2->left;
                    flag2 = true;
                }
            }
        }

        // If a pair was found, check if the sum is equal to target
        if((val1 != val2) && (val1 + val2) == target){
            cout << "Pair Found: " << val1 << " + " << val2 << " = " << target << endl;
            return true;
        }

        // If the sum of the current pair is smaller, then go to next node in the (forwards) in-order traversal
        else if ((val1 + val2) < target)
            flag1 = false;

        // If the sum of the current pair is bigger, then go to next node in the (reverse) in-order traversal
        else if ((val1 + val2) > target)
            flag2 = false;

        // If either traversal completes without finding a pair, then there is no pair.
        if(val1 >= val2)
            return false;
    }
}

// Utility function that performs an in-order traversal
void inorder(struct Node *root){
    if(root != NULL){
        inorder(root->left);
        printf("%d \n", root->data);
        inorder(root->right);
    }
}

int main(){
    // Construct a BST
    /*  
                15  
                / \  
            10 20  
            / \ / \  
           8 12 16 25 */
    struct Node* root = NULL;

    root = insertBST(root, 15);
    root = insertBST(root, 10);
    root = insertBST(root, 20);
    root = insertBST(root, 8);
    root = insertBST(root, 12);
    root = insertBST(root, 16);
    root = insertBST(root, 25);
    
    findPair(root, 24);

    return 0;
}