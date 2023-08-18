#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

dlistint_t *insert_dnodeint_at_index(dlistint_t **h, unsigned int idx, int n)
{
	dlistint_t *new_node, *current;
	unsigned int current_idx;

	new_node = malloc(sizeof(dlistint_t));

	if (new_node == NULL)
	{
	return (NULL);
	}

	new_node->n = n;

	if (*h == NULL && idx == 0)
	{
	new_node->prev = NULL;
	new_node->next = NULL;
	*h = new_node;
	return (new_node);
	}

	current = *h;
	current_idx = 0;
	while (current != NULL && current_idx < idx)
	{
	current = current->next;
	current_idx++;
	}

	if (current == NULL && current_idx < idx)
	{
	free(new_node);
	return (NULL);
	}

	if (current_idx > 0)
	{
	new_node->prev = current->prev;
	new_node->next = current;
	current->prev->next = new_node;
	current->prev = new_node;
	}
	else
	{
	new_node->prev = NULL;
	new_node->next = current;
	current->prev = new_node;
	*h = new_node;
	}

	return (new_node);
}

