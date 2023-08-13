#include "lists.h"

/**
 * check_cycle - function that checks for a cycle in a linked list
 * using Floyd’s Cycle Finding Algorithm
 * @list: pointer to start of the list
 * Return: 0 if there is no cycle, 1 if there is
*/
int check_cycle(listint_t *list)
{
	listint_t *tortoise, *hare;

	if (list == NULL)
		return (0);

	tortoise = list;
	hare = list;
	while (hare != NULL && hare->next != NULL)
	{
		tortoise = tortoise->next;
		hare = hare->next->next;
		if (tortoise == hare)
			return (1);
	}
	return (0);
}
