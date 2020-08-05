#include <stdio.h>
#include <stdlib.h>
#include "binary_trees.h"

/**
 * heap_insert - inserts a value into a Max Binary Heap
 *
 * @root: double pointer to the root node of the Heap
 * @value: value store in the node to be inserted
 * Return: a pointer to inserted node
 */
heap_t *heap_insert(heap_t **root, int value)
{
	int saveValue;
	heap_t *newNode;
	heap_t *destNode;
	heap_t *currNode;

	if (root == NULL)
		return (NULL);
	newNode = malloc(sizeof(heap_t));
	if (newNode == NULL)
		return (NULL);
	newNode->n = value;
	newNode->parent = NULL;
	newNode->left = NULL;
	newNode->right = NULL;
	if (*root == NULL)
	{
		*root = newNode;
		return (newNode);
	}
	else if ((*root)->left == NULL || (*root)->right == NULL)
		destNode = *root;
	else
		destNode = traverse((*root)->left, (*root)->right);
	if (destNode->left == NULL)
		destNode->left = newNode;
	else
		destNode->right = newNode;
	newNode->parent = destNode;
	currNode = newNode;
	while (currNode->parent != NULL && currNode->n > currNode->parent->n)
	{
		saveValue = currNode->parent->n;
		currNode->parent->n = currNode->n;
		currNode->n = saveValue;
		currNode = currNode->parent;
	}
	return (currNode);
}

/**
 * traverse - traverse max heap to find parent with empty child
 *
 * @left: pointer to left node of tree root
 * @right: pointer to right node of tree root
 * Return: pointer to node with NULL child
 */
heap_t *traverse(heap_t *left, heap_t *right)
{
	if (left != NULL && (left->left == NULL || left->right == NULL))
		return (left);
	else if (right != NULL && (right->left == NULL || right->right == NULL))
		return (right);
	return (traverse(left->left, right->right));
}
