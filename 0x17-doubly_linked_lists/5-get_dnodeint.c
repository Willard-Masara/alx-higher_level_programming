#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

dlistint_t *get_dnodeint_at_index(dlistint_t *head, unsigned int index)
{
	unsigned int count;
	count = 0;

	while (head != NULL)
	{
	if (count == index)
	{
		return (head);
	}

	head = head->next;
	count++;
	}

	return (NULL);
}
