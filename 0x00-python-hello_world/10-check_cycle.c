#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - check if a singly linked list has a cycle
 * @list: the singly linked list
 *
 * Return: 0 it there is no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *tort, *hare;

	if (list == NULL || list->next == NULL)
		return (0);

	tort = list;
	hare = list;
	while (hare != NULL && hare->next != NULL)
	{
		tort = tort->next;
		hare = hare->next->next;

		if (hare == tort)
			return (1);
	}

	return (0);
}
