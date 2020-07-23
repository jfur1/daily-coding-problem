// Given a binary tree, return the level of the tree with minimum sum.
// Written in C++ to implement using pointers
#include <iostream>
#include <queue>
using namespace std;

struct Node{
    int data;
    struct Node *left, *right;
};

struct Node *newNode(int data){
    struct Node * node = new Node;
    node->data = data;
    node->left = node->right = NULL;
    return node;
}

int minLevelSum(struct Node *root){
    if(root == NULL)
        return 0;
    
    int result = root->data;
    // Use a queue to perform a level-order traversal
    queue<Node*> q;
    q.push(root);

    int sum = 0;
    while(!q.empty()){
        int count = q.size();

        int sum = 0;
        while(count--){
            Node *tmp = q.front();
            q.pop();

            sum += tmp->data;

            if(tmp->left != NULL)
                q.push(tmp->left);
            if(tmp->right != NULL)
                q.push(tmp->right);
        }
        // Keep track of the minimum sum after each level-traversal
        result = (sum < result) ? sum : result;
    }
    return result;
}

int main(int argc, char* argv[]){
    struct Node *root = newNode(9); 
    root->left        = newNode(2); 
    root->right       = newNode(3); 
    root->left->left  = newNode(4); 
    root->left->right = newNode(5); 
    root->right->right = newNode(8); 
    root->right->right->left  = newNode(6); 
    root->right->right->right  = newNode(7); 
  
    /*   Constructed Binary tree is: 
                 9 
               /   \ 
             2      3 
           /  \      \ 
          4    5      8 
                    /   \ 
                   6     7    */
    cout << "Minimum level sum is "
         << minLevelSum(root) << endl; 
    return 0; 

}