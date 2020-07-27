#include <stdlib.h>
#include <stdio.h>
#include "lists.h"


/**
 * insert_node - inserts node into linked list
 * @head: pointer to first pointer in array
 * @number: value to be inserted
 * Return: pointer to inserted node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *curr;
	listint_t *save;

	if ((head == NULL) || (*head == NULL))
		return (NULL);

	curr = *head;
	save = NULL;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	while ((curr->next != NULL) && (number > curr->next->n))
	{
		curr = curr->next;
	}
	if (curr == *head)
	{
		save = *head;
		*head = new;
		new->next = save;
		return (new);
	}
	else if (curr->next == NULL)
	{
		curr->next = new;
		return (new);
	}
	save = curr->next;
	curr->next = new;
	new->next = save;

	return (new);
}
