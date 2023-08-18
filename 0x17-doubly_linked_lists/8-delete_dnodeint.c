#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
#include <stddef.h>

int delete_dnodeint_at_index(dlistint_t **head, unsigned int index)
{
	dlistint_t *current;
	dlistint_t *temp;
	unsigned int current_idx;
	if (*head == NULL)
	{
	return (-1);
	}

	if (index == 0)
	{
	temp = *head;
	*head = (*head)->next;
	if (*head != NULL)
	{
	    (*head)->prev = NULL;
	}
	free(temp);
	return (1);
	}

	current = *head;
	current_idx = 0;
	while (current != NULL && current_idx < index)
	{
	current = current->next;
	current_idx++;
	}

	if (current == NULL && current_idx < index)
	{
	return (-1);
	}

	current->prev->next = current->next;
	if (current->next != NULL)
	{
	current->next->prev = current->prev;
	}
	free(current);
	return (1);
}
