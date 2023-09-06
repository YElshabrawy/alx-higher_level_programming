#include "lists.h"
/**
 * insert_node - insert node in sorted linked list
 * @head: head
 * @number: new data
 * Return: pointer to the new node or NULL
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head;
	listint_t *new = malloc(sizeof(listint_t));

	if (!new)
		return (NULL);
	new->n = number;
	new->next = NULL;

	if (!node || new->n < node->n)
	{
		new->next = node;
		return (*head = new);
	}
	while (node)
	{
		if (!node->next || new->n < node->n)
		{
			new->next = node->next;
			node->next = new;
			return (node);
		}
		node = node->next;
	}
	return (NULL);
}
